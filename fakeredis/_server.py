import inspect
import queue
import threading
import time
import warnings
import weakref
from collections import defaultdict

import redis

from fakeredis._helpers import (
    Database, FakeSelector, CONNECTION_ERROR_MSG, FakeSocket, LOGGER)

LOGGER = LOGGER


class FakeServer:
    def __init__(self):
        self.lock = threading.Lock()
        self.dbs = defaultdict(lambda: Database(self.lock))
        # Maps SHA1 to script source
        self.script_cache = {}
        # Maps channel/pattern to weak set of sockets
        self.subscribers = defaultdict(weakref.WeakSet)
        self.psubscribers = defaultdict(weakref.WeakSet)
        self.lastsave = int(time.time())
        self.connected = True
        # List of weakrefs to sockets that are being closed lazily
        self.closed_sockets = []


class FakeConnection(redis.Connection):
    description_format = "FakeConnection<db=%(db)s>"

    def __init__(self, *args, **kwargs):
        self.encoder = None
        self.client_name = None
        self._sock = None
        self._selector = None
        self._server = kwargs.pop('server')
        super().__init__(*args, **kwargs)

    def connect(self):
        super().connect()
        # The selector is set in redis.Connection.connect() after _connect() is called
        self._selector = FakeSelector(self._sock)

    def _connect(self):
        if not self._server.connected:
            raise redis.ConnectionError(CONNECTION_ERROR_MSG)
        return FakeSocket(self._server)

    def can_read(self, timeout=0):
        if not self._server.connected:
            return True
        if not self._sock:
            self.connect()
        # We use check_can_read rather than can_read, because on redis-py<3.2,
        # FakeSelector inherits from a stub BaseSelector which doesn't
        # implement can_read. Normally can_read provides retries on EINTR,
        # but that's not necessary for the implementation of
        # FakeSelector.check_can_read.
        return self._selector.check_can_read(timeout)

    def _decode(self, response):
        if isinstance(response, list):
            return [self._decode(item) for item in response]
        elif isinstance(response, bytes):
            return self.encoder.decode(response, )
        else:
            return response

    def read_response(self, disable_decoding=False):
        if not self._server.connected:
            try:
                response = self._sock.responses.get_nowait()
            except queue.Empty:
                raise redis.ConnectionError(CONNECTION_ERROR_MSG)
        else:
            response = self._sock.responses.get()
        if isinstance(response, redis.ResponseError):
            raise response
        if disable_decoding:
            return response
        else:
            return self._decode(response)

    def repr_pieces(self):
        pieces = [
            ('server', self._server),
            ('db', self.db)
        ]
        if self.client_name:
            pieces.append(('client_name', self.client_name))
        return pieces


class FakeRedisMixin:
    def __init__(self, *args, server=None, connected=True, **kwargs):
        # Interpret the positional and keyword arguments according to the
        # version of redis in use.
        default_args = inspect.signature(redis.Redis.__init__).parameters.values()
        kwds = {p.name: p.default for p in default_args if p.default != inspect.Parameter.empty}
        kwds.update(kwargs)
        # bound = _ORIG_SIG.bind(*args, **params)
        # kwds = bound.arguments['kwds']
        if not kwds['connection_pool']:
            charset = kwds['charset']
            errors = kwds['errors']
            # Adapted from redis-py
            if charset is not None:
                warnings.warn(DeprecationWarning(
                    '"charset" is deprecated. Use "encoding" instead'))
                kwds['encoding'] = charset
            if errors is not None:
                warnings.warn(DeprecationWarning(
                    '"errors" is deprecated. Use "encoding_errors" instead'))
                kwds['encoding_errors'] = errors

            if server is None:
                server = FakeServer()
                server.connected = connected
            kwargs = {
                'connection_class': FakeConnection,
                'server': server
            }
            conn_pool_args = [
                'db',
                # Ignoring because AUTH is not implemented
                # 'username',
                # 'password',
                'socket_timeout',
                'encoding',
                'encoding_errors',
                'decode_responses',
                'retry_on_timeout',
                'max_connections',
                'health_check_interval',
                'client_name'
            ]
            for arg in conn_pool_args:
                if arg in kwds:
                    kwargs[arg] = kwds[arg]
            kwds['connection_pool'] = redis.connection.ConnectionPool(**kwargs)
        super().__init__(*args, **kwds)

    @classmethod
    def from_url(cls, *args, **kwargs):
        server = kwargs.pop('server', None)
        if server is None:
            server = FakeServer()
        pool = redis.ConnectionPool.from_url(*args, **kwargs)
        # Now override how it creates connections
        pool.connection_class = FakeConnection
        pool.connection_kwargs['server'] = server
        # FakeConnection cannot handle the path kwarg (present when from_url
        # is called with a unix socket)
        pool.connection_kwargs.pop('path', None)
        # Using username and password fails since AUTH is not implemented.
        # https://github.com/dsoftwareinc/fakeredis-py/issues/9
        pool.connection_kwargs.pop('username', None)
        pool.connection_kwargs.pop('password', None)
        return cls(connection_pool=pool)


class FakeStrictRedis(FakeRedisMixin, redis.StrictRedis):
    pass


class FakeRedis(FakeRedisMixin, redis.Redis):
    pass


# RQ
# Configuration to pretend there is a Redis service available.
# Set up the connection before RQ Django reads the settings.
# The connection must be the same because in fakeredis connections
# do not share the state. Therefore, we define a singleton object to reuse it.
class FakeRedisConnSingleton:
    """Singleton FakeRedis connection."""

    def __init__(self):
        self.conn = None

    def __call__(self, _, strict):
        if not self.conn:
            self.conn = FakeStrictRedis() if strict else FakeRedis()
        return self.conn
