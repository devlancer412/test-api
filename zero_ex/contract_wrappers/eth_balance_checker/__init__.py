"""Generated wrapper for EthBalanceChecker Solidity contract."""

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
# constructor for EthBalanceChecker below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        EthBalanceCheckerValidator,
    )
except ImportError:

    class EthBalanceCheckerValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


class GetEthBalancesMethod(ContractMethod):
    """Various interfaces to the getEthBalances method."""

    def __init__(
        self,
        provider: BaseProvider,
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, addresses: List[str]):
        """Validate the inputs to the getEthBalances method."""
        self.validator.assert_valid(
            method_name="getEthBalances",
            parameter_name="addresses",
            argument_value=addresses,
        )
        return addresses

    def call(
        self, addresses: List[str], tx_params: Optional[TxParams] = None
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        Batch fetches ETH balances

        :param addresses: Array of addresses.
        :param tx_params: transaction parameters
        :returns: Array of ETH balances.
        """
        (addresses) = self.validate_and_normalize_inputs(addresses)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addresses).call(tx_params.as_dict())

    def send_transaction(
        self, addresses: List[str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Batch fetches ETH balances

        :param addresses: Array of addresses.
        :param tx_params: transaction parameters
        :returns: Array of ETH balances.
        """
        (addresses) = self.validate_and_normalize_inputs(addresses)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addresses).transact(tx_params.as_dict())

    def estimate_gas(
        self, addresses: List[str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addresses) = self.validate_and_normalize_inputs(addresses)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addresses).estimateGas(
            tx_params.as_dict()
        )

    def build_transaction(
        self, addresses: List[str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addresses) = self.validate_and_normalize_inputs(addresses)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addresses).buildTransaction(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class EthBalanceChecker:
    """Wrapper class for EthBalanceChecker Solidity contract."""

    get_eth_balances: GetEthBalancesMethod
    """Constructor-initialized instance of
    :class:`GetEthBalancesMethod`.
    """

    def __init__(
        self,
        provider: BaseProvider,
        contract_address: str,
        validator: EthBalanceCheckerValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param provider: instance of :class:`web3.providers.base.BaseProvider`
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        self.contract_address = contract_address

        if not validator:
            validator = EthBalanceCheckerValidator(provider, contract_address)

        self._web3_eth = Web3(  # type: ignore # pylint: disable=no-member
            provider
        ).eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address),
            abi=EthBalanceChecker.abi(),
        ).functions

        self.get_eth_balances = GetEthBalancesMethod(
            provider, contract_address, functions.getEthBalances, validator
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":true,"inputs":[{"name":"addresses","type":"address[]"}],"name":"getEthBalances","outputs":[{"name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
