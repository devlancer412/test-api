"""Generated wrapper for CoordinatorRegistry Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for CoordinatorRegistry below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        CoordinatorRegistryValidator,
    )
except ImportError:

    class CoordinatorRegistryValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class GetCoordinatorEndpointMethod(ContractMethod):
    """Various interfaces to the getCoordinatorEndpoint method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, coordinator_operator: str):
        """Validate the inputs to the getCoordinatorEndpoint method."""
        self.validator.assert_valid(
            method_name="getCoordinatorEndpoint",
            parameter_name="coordinatorOperator",
            argument_value=coordinator_operator,
        )
        coordinator_operator = self.validate_and_checksum_address(
            coordinator_operator
        )
        return coordinator_operator

    def call(
        self, coordinator_operator: str, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        Gets the endpoint for a Coordinator.

        :param coordinatorOperator: Operator of the Coordinator endpoint.
        :param tx_params: transaction parameters
        :returns: coordinatorEndpoint Endpoint of the Coordinator as a string.
        """
        (coordinator_operator) = self.validate_and_normalize_inputs(
            coordinator_operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(coordinator_operator).call(
            tx_params.as_dict()
        )
        return str(returned)

    def estimate_gas(
        self, coordinator_operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (coordinator_operator) = self.validate_and_normalize_inputs(
            coordinator_operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(coordinator_operator).estimateGas(
            tx_params.as_dict()
        )


class SetCoordinatorEndpointMethod(ContractMethod):
    """Various interfaces to the setCoordinatorEndpoint method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, coordinator_endpoint: str):
        """Validate the inputs to the setCoordinatorEndpoint method."""
        self.validator.assert_valid(
            method_name="setCoordinatorEndpoint",
            parameter_name="coordinatorEndpoint",
            argument_value=coordinator_endpoint,
        )
        return coordinator_endpoint

    def call(
        self, coordinator_endpoint: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Called by a Coordinator operator to set the endpoint of their
        Coordinator.

        :param coordinatorEndpoint: Endpoint of the Coordinator as a string.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (coordinator_endpoint) = self.validate_and_normalize_inputs(
            coordinator_endpoint
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(coordinator_endpoint).call(tx_params.as_dict())

    def send_transaction(
        self, coordinator_endpoint: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Called by a Coordinator operator to set the endpoint of their
        Coordinator.

        :param coordinatorEndpoint: Endpoint of the Coordinator as a string.
        :param tx_params: transaction parameters
        """
        (coordinator_endpoint) = self.validate_and_normalize_inputs(
            coordinator_endpoint
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(coordinator_endpoint).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, coordinator_endpoint: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (coordinator_endpoint) = self.validate_and_normalize_inputs(
            coordinator_endpoint
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(coordinator_endpoint).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, coordinator_endpoint: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (coordinator_endpoint) = self.validate_and_normalize_inputs(
            coordinator_endpoint
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(coordinator_endpoint).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class CoordinatorRegistry:
    """Wrapper class for CoordinatorRegistry Solidity contract."""

    get_coordinator_endpoint: GetCoordinatorEndpointMethod
    """Constructor-initialized instance of
    :class:`GetCoordinatorEndpointMethod`.
    """

    set_coordinator_endpoint: SetCoordinatorEndpointMethod
    """Constructor-initialized instance of
    :class:`SetCoordinatorEndpointMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: CoordinatorRegistryValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param web3_or_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = CoordinatorRegistryValidator(
                web3_or_provider, contract_address
            )

        web3 = None
        if isinstance(web3_or_provider, BaseProvider):
            web3 = Web3(web3_or_provider)
        elif isinstance(web3_or_provider, Web3):
            web3 = web3_or_provider
        else:
            raise TypeError(
                "Expected parameter 'web3_or_provider' to be an instance of either"
                + " Web3 or BaseProvider"
            )

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware["function"], layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address),
            abi=CoordinatorRegistry.abi(),
        ).functions

        self.get_coordinator_endpoint = GetCoordinatorEndpointMethod(
            web3_or_provider,
            contract_address,
            functions.getCoordinatorEndpoint,
            validator,
        )

        self.set_coordinator_endpoint = SetCoordinatorEndpointMethod(
            web3_or_provider,
            contract_address,
            functions.setCoordinatorEndpoint,
            validator,
        )

    def get_coordinator_endpoint_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for CoordinatorEndpointSet event.

        :param tx_hash: hash of transaction emitting CoordinatorEndpointSet
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=CoordinatorRegistry.abi(),
            )
            .events.CoordinatorEndpointSet()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"coordinatorOperator","type":"address"},{"indexed":false,"internalType":"string","name":"coordinatorEndpoint","type":"string"}],"name":"CoordinatorEndpointSet","type":"event"},{"constant":true,"inputs":[{"internalType":"address","name":"coordinatorOperator","type":"address"}],"name":"getCoordinatorEndpoint","outputs":[{"internalType":"string","name":"coordinatorEndpoint","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"coordinatorEndpoint","type":"string"}],"name":"setCoordinatorEndpoint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
