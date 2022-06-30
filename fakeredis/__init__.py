from ._server import FakeServer, FakeRedis, FakeStrictRedis, FakeConnection, FakeRedisConnSingleton  # noqa: F401

try:
    from importlib import metadata
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata
__version__ = metadata.version("fakeredis")
