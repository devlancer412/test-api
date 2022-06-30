"""Generated wrapper for IAssetProxy Solidity contract."""

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
# constructor for IAssetProxy below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IAssetProxyValidator,
    )
except ImportError:

    class IAssetProxyValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class TransferFromMethod(ContractMethod):
    """Various interfaces to the transferFrom method."""

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

    def validate_and_normalize_inputs(
        self, asset_data: Union[bytes, str], _from: str, to: str, amount: int
    ):
        """Validate the inputs to the transferFrom method."""
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="transferFrom", parameter_name="to", argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (asset_data, _from, to, amount)

    def call(
        self,
        asset_data: Union[bytes, str],
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Transfers assets. Either succeeds or throws.

        :param amount: Amount of asset to transfer.
        :param assetData: Byte array encoded for the respective asset proxy.
        :param from: Address to transfer asset from.
        :param to: Address to transfer asset to.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (asset_data, _from, to, amount) = self.validate_and_normalize_inputs(
            asset_data, _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(asset_data, _from, to, amount).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        asset_data: Union[bytes, str],
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Transfers assets. Either succeeds or throws.

        :param amount: Amount of asset to transfer.
        :param assetData: Byte array encoded for the respective asset proxy.
        :param from: Address to transfer asset from.
        :param to: Address to transfer asset to.
        :param tx_params: transaction parameters
        """
        (asset_data, _from, to, amount) = self.validate_and_normalize_inputs(
            asset_data, _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_data, _from, to, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        asset_data: Union[bytes, str],
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_data, _from, to, amount) = self.validate_and_normalize_inputs(
            asset_data, _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_data, _from, to, amount
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        asset_data: Union[bytes, str],
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (asset_data, _from, to, amount) = self.validate_and_normalize_inputs(
            asset_data, _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_data, _from, to, amount
        ).estimateGas(tx_params.as_dict())


class GetProxyIdMethod(ContractMethod):
    """Various interfaces to the getProxyId method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Gets the proxy id associated with the proxy address.

        :param tx_params: transaction parameters
        :returns: Proxy id.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IAssetProxy:
    """Wrapper class for IAssetProxy Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    transfer_from: TransferFromMethod
    """Constructor-initialized instance of
    :class:`TransferFromMethod`.
    """

    get_proxy_id: GetProxyIdMethod
    """Constructor-initialized instance of
    :class:`GetProxyIdMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IAssetProxyValidator = None,
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
            validator = IAssetProxyValidator(
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
            abi=IAssetProxy.abi(),
        ).functions

        self.transfer_from = TransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.transferFrom,
            validator,
        )

        self.get_proxy_id = GetProxyIdMethod(
            web3_or_provider, contract_address, functions.getProxyId
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":false,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"},{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getProxyId","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"payable":false,"stateMutability":"pure","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
