"""Generated wrapper for Forwarder Solidity contract."""

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
# constructor for Forwarder below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ForwarderValidator,
    )
except ImportError:

    class ForwarderValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class LibOrderOrder(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    makerAddress: str

    takerAddress: str

    feeRecipientAddress: str

    senderAddress: str

    makerAssetAmount: int

    takerAssetAmount: int

    makerFee: int

    takerFee: int

    expirationTimeSeconds: int

    salt: int

    makerAssetData: Union[bytes, str]

    takerAssetData: Union[bytes, str]

    makerFeeAssetData: Union[bytes, str]

    takerFeeAssetData: Union[bytes, str]


class ApproveMakerAssetProxyMethod(ContractMethod):
    """Various interfaces to the approveMakerAssetProxy method."""

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

    def validate_and_normalize_inputs(self, asset_data: Union[bytes, str]):
        """Validate the inputs to the approveMakerAssetProxy method."""
        self.validator.assert_valid(
            method_name="approveMakerAssetProxy",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return asset_data

    def call(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Approves the respective proxy for a given asset to transfer tokens on
        the Forwarder contract's behalf. This is necessary because an order fee
        denominated in the maker asset (i.e. a percentage fee) is sent by the
        Forwarder contract to the fee recipient. This method needs to be called
        before forwarding orders of a maker asset that hasn't previously been
        approved.

        :param assetData: Byte array encoded for the respective asset proxy.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(asset_data).call(tx_params.as_dict())

    def send_transaction(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Approves the respective proxy for a given asset to transfer tokens on
        the Forwarder contract's behalf. This is necessary because an order fee
        denominated in the maker asset (i.e. a percentage fee) is sent by the
        Forwarder contract to the fee recipient. This method needs to be called
        before forwarding orders of a maker asset that hasn't previously been
        approved.

        :param assetData: Byte array encoded for the respective asset proxy.
        :param tx_params: transaction parameters
        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_data).estimateGas(
            tx_params.as_dict()
        )


class MarketBuyOrdersWithEthMethod(ContractMethod):
    """Various interfaces to the marketBuyOrdersWithEth method."""

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
        self,
        orders: List[LibOrderOrder],
        maker_asset_buy_amount: int,
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
    ):
        """Validate the inputs to the marketBuyOrdersWithEth method."""
        self.validator.assert_valid(
            method_name="marketBuyOrdersWithEth",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="marketBuyOrdersWithEth",
            parameter_name="makerAssetBuyAmount",
            argument_value=maker_asset_buy_amount,
        )
        # safeguard against fractional inputs
        maker_asset_buy_amount = int(maker_asset_buy_amount)
        self.validator.assert_valid(
            method_name="marketBuyOrdersWithEth",
            parameter_name="signatures",
            argument_value=signatures,
        )
        self.validator.assert_valid(
            method_name="marketBuyOrdersWithEth",
            parameter_name="feePercentage",
            argument_value=fee_percentage,
        )
        # safeguard against fractional inputs
        fee_percentage = int(fee_percentage)
        self.validator.assert_valid(
            method_name="marketBuyOrdersWithEth",
            parameter_name="feeRecipient",
            argument_value=fee_recipient,
        )
        fee_recipient = self.validate_and_checksum_address(fee_recipient)
        return (
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        )

    def call(
        self,
        orders: List[LibOrderOrder],
        maker_asset_buy_amount: int,
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[int, int, int]:
        """Execute underlying contract method via eth_call.

        Attempt to buy makerAssetBuyAmount of makerAsset by selling ETH
        provided with transaction. The Forwarder may *fill* more than
        makerAssetBuyAmount of the makerAsset so that it can pay takerFees
        where takerFeeAssetData == makerAssetData (i.e. percentage fees). Any
        ETH not spent will be refunded to sender.

        :param feePercentage: Percentage of WETH sold that will payed as fee to
            forwarding contract feeRecipient.
        :param feeRecipient: Address that will receive ETH when orders are
            filled.
        :param makerAssetBuyAmount: Desired amount of makerAsset to purchase.
        :param orders: Array of order specifications used containing desired
            makerAsset and WETH as takerAsset.
        :param signatures: Proofs that orders have been created by makers.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        ) = self.validate_and_normalize_inputs(
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        ).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        maker_asset_buy_amount: int,
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Attempt to buy makerAssetBuyAmount of makerAsset by selling ETH
        provided with transaction. The Forwarder may *fill* more than
        makerAssetBuyAmount of the makerAsset so that it can pay takerFees
        where takerFeeAssetData == makerAssetData (i.e. percentage fees). Any
        ETH not spent will be refunded to sender.

        :param feePercentage: Percentage of WETH sold that will payed as fee to
            forwarding contract feeRecipient.
        :param feeRecipient: Address that will receive ETH when orders are
            filled.
        :param makerAssetBuyAmount: Desired amount of makerAsset to purchase.
        :param orders: Array of order specifications used containing desired
            makerAsset and WETH as takerAsset.
        :param signatures: Proofs that orders have been created by makers.
        :param tx_params: transaction parameters
        """
        (
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        ) = self.validate_and_normalize_inputs(
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        maker_asset_buy_amount: int,
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        ) = self.validate_and_normalize_inputs(
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        maker_asset_buy_amount: int,
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        ) = self.validate_and_normalize_inputs(
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders,
            maker_asset_buy_amount,
            signatures,
            fee_percentage,
            fee_recipient,
        ).estimateGas(tx_params.as_dict())


class MarketSellOrdersWithEthMethod(ContractMethod):
    """Various interfaces to the marketSellOrdersWithEth method."""

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
        self,
        orders: List[LibOrderOrder],
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
    ):
        """Validate the inputs to the marketSellOrdersWithEth method."""
        self.validator.assert_valid(
            method_name="marketSellOrdersWithEth",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="marketSellOrdersWithEth",
            parameter_name="signatures",
            argument_value=signatures,
        )
        self.validator.assert_valid(
            method_name="marketSellOrdersWithEth",
            parameter_name="feePercentage",
            argument_value=fee_percentage,
        )
        # safeguard against fractional inputs
        fee_percentage = int(fee_percentage)
        self.validator.assert_valid(
            method_name="marketSellOrdersWithEth",
            parameter_name="feeRecipient",
            argument_value=fee_recipient,
        )
        fee_recipient = self.validate_and_checksum_address(fee_recipient)
        return (orders, signatures, fee_percentage, fee_recipient)

    def call(
        self,
        orders: List[LibOrderOrder],
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[int, int, int]:
        """Execute underlying contract method via eth_call.

        Purchases as much of orders' makerAssets as possible by selling as much
        of the ETH value sent as possible, accounting for order and forwarder
        fees.

        :param feePercentage: Percentage of WETH sold that will payed as fee to
            forwarding contract feeRecipient.
        :param feeRecipient: Address that will receive ETH when orders are
            filled.
        :param orders: Array of order specifications used containing desired
            makerAsset and WETH as takerAsset.
        :param signatures: Proofs that orders have been created by makers.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            signatures,
            fee_percentage,
            fee_recipient,
        ) = self.validate_and_normalize_inputs(
            orders, signatures, fee_percentage, fee_recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, signatures, fee_percentage, fee_recipient
        ).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Purchases as much of orders' makerAssets as possible by selling as much
        of the ETH value sent as possible, accounting for order and forwarder
        fees.

        :param feePercentage: Percentage of WETH sold that will payed as fee to
            forwarding contract feeRecipient.
        :param feeRecipient: Address that will receive ETH when orders are
            filled.
        :param orders: Array of order specifications used containing desired
            makerAsset and WETH as takerAsset.
        :param signatures: Proofs that orders have been created by makers.
        :param tx_params: transaction parameters
        """
        (
            orders,
            signatures,
            fee_percentage,
            fee_recipient,
        ) = self.validate_and_normalize_inputs(
            orders, signatures, fee_percentage, fee_recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, signatures, fee_percentage, fee_recipient
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            signatures,
            fee_percentage,
            fee_recipient,
        ) = self.validate_and_normalize_inputs(
            orders, signatures, fee_percentage, fee_recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, signatures, fee_percentage, fee_recipient
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        signatures: List[Union[bytes, str]],
        fee_percentage: int,
        fee_recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            signatures,
            fee_percentage,
            fee_recipient,
        ) = self.validate_and_normalize_inputs(
            orders, signatures, fee_percentage, fee_recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, signatures, fee_percentage, fee_recipient
        ).estimateGas(tx_params.as_dict())


class OwnerMethod(ContractMethod):
    """Various interfaces to the owner method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class TransferOwnershipMethod(ContractMethod):
    """Various interfaces to the transferOwnership method."""

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

    def validate_and_normalize_inputs(self, new_owner: str):
        """Validate the inputs to the transferOwnership method."""
        self.validator.assert_valid(
            method_name="transferOwnership",
            parameter_name="newOwner",
            argument_value=new_owner,
        )
        new_owner = self.validate_and_checksum_address(new_owner)
        return new_owner

    def call(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_owner).call(tx_params.as_dict())

    def send_transaction(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).transact(tx_params.as_dict())

    def build_transaction(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).estimateGas(
            tx_params.as_dict()
        )


class WithdrawAssetMethod(ContractMethod):
    """Various interfaces to the withdrawAsset method."""

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
        self, asset_data: Union[bytes, str], amount: int
    ):
        """Validate the inputs to the withdrawAsset method."""
        self.validator.assert_valid(
            method_name="withdrawAsset",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        self.validator.assert_valid(
            method_name="withdrawAsset",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (asset_data, amount)

    def call(
        self,
        asset_data: Union[bytes, str],
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Withdraws assets from this contract. It may be used by the owner to
        withdraw assets that were accidentally sent to this contract.

        :param amount: Amount of the asset to withdraw.
        :param assetData: Byte array encoded for the respective asset proxy.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (asset_data, amount) = self.validate_and_normalize_inputs(
            asset_data, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(asset_data, amount).call(tx_params.as_dict())

    def send_transaction(
        self,
        asset_data: Union[bytes, str],
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Withdraws assets from this contract. It may be used by the owner to
        withdraw assets that were accidentally sent to this contract.

        :param amount: Amount of the asset to withdraw.
        :param assetData: Byte array encoded for the respective asset proxy.
        :param tx_params: transaction parameters
        """
        (asset_data, amount) = self.validate_and_normalize_inputs(
            asset_data, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_data, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        asset_data: Union[bytes, str],
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_data, amount) = self.validate_and_normalize_inputs(
            asset_data, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_data, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        asset_data: Union[bytes, str],
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (asset_data, amount) = self.validate_and_normalize_inputs(
            asset_data, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_data, amount).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Forwarder:
    """Wrapper class for Forwarder Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    approve_maker_asset_proxy: ApproveMakerAssetProxyMethod
    """Constructor-initialized instance of
    :class:`ApproveMakerAssetProxyMethod`.
    """

    market_buy_orders_with_eth: MarketBuyOrdersWithEthMethod
    """Constructor-initialized instance of
    :class:`MarketBuyOrdersWithEthMethod`.
    """

    market_sell_orders_with_eth: MarketSellOrdersWithEthMethod
    """Constructor-initialized instance of
    :class:`MarketSellOrdersWithEthMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    withdraw_asset: WithdrawAssetMethod
    """Constructor-initialized instance of
    :class:`WithdrawAssetMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ForwarderValidator = None,
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
            validator = ForwarderValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=Forwarder.abi()
        ).functions

        self.approve_maker_asset_proxy = ApproveMakerAssetProxyMethod(
            web3_or_provider,
            contract_address,
            functions.approveMakerAssetProxy,
            validator,
        )

        self.market_buy_orders_with_eth = MarketBuyOrdersWithEthMethod(
            web3_or_provider,
            contract_address,
            functions.marketBuyOrdersWithEth,
            validator,
        )

        self.market_sell_orders_with_eth = MarketSellOrdersWithEthMethod(
            web3_or_provider,
            contract_address,
            functions.marketSellOrdersWithEth,
            validator,
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
        )

        self.transfer_ownership = TransferOwnershipMethod(
            web3_or_provider,
            contract_address,
            functions.transferOwnership,
            validator,
        )

        self.withdraw_asset = WithdrawAssetMethod(
            web3_or_provider,
            contract_address,
            functions.withdrawAsset,
            validator,
        )

    def get_ownership_transferred_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnershipTransferred event.

        :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Forwarder.abi(),
            )
            .events.OwnershipTransferred()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_exchange","type":"address"},{"internalType":"address","name":"_weth","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":false,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"approveMakerAssetProxy","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256","name":"makerAssetBuyAmount","type":"uint256"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"},{"internalType":"uint256","name":"feePercentage","type":"uint256"},{"internalType":"address payable","name":"feeRecipient","type":"address"}],"name":"marketBuyOrdersWithEth","outputs":[{"internalType":"uint256","name":"wethSpentAmount","type":"uint256"},{"internalType":"uint256","name":"makerAssetAcquiredAmount","type":"uint256"},{"internalType":"uint256","name":"ethFeePaid","type":"uint256"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"},{"internalType":"uint256","name":"feePercentage","type":"uint256"},{"internalType":"address payable","name":"feeRecipient","type":"address"}],"name":"marketSellOrdersWithEth","outputs":[{"internalType":"uint256","name":"wethSpentAmount","type":"uint256"},{"internalType":"uint256","name":"makerAssetAcquiredAmount","type":"uint256"},{"internalType":"uint256","name":"ethFeePaid","type":"uint256"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdrawAsset","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
