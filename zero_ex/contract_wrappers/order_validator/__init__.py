"""Generated wrapper for OrderValidator Solidity contract."""

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
# constructor for OrderValidator below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        OrderValidatorValidator,
    )
except ImportError:

    class OrderValidatorValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class Tuple0x260219a2(TypedDict):
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


class Tuple0xb1e4a1ae(TypedDict):
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

    orderStatus: int

    orderHash: Union[bytes, str]

    orderTakerAssetFilledAmount: int


class Tuple0x8cfc0927(TypedDict):
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

    makerBalance: int

    makerAllowance: int

    takerBalance: int

    takerAllowance: int

    makerZrxBalance: int

    makerZrxAllowance: int

    takerZrxBalance: int

    takerZrxAllowance: int


class GetOrderAndTraderInfoMethod(ContractMethod):
    """Various interfaces to the getOrderAndTraderInfo method."""

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
        self, order: Tuple0x260219a2, taker_address: str
    ):
        """Validate the inputs to the getOrderAndTraderInfo method."""
        self.validator.assert_valid(
            method_name="getOrderAndTraderInfo",
            parameter_name="order",
            argument_value=order,
        )
        self.validator.assert_valid(
            method_name="getOrderAndTraderInfo",
            parameter_name="takerAddress",
            argument_value=taker_address,
        )
        taker_address = self.validate_and_checksum_address(taker_address)
        return (order, taker_address)

    def call(
        self,
        order: Tuple0x260219a2,
        taker_address: str,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[Tuple0xb1e4a1ae, Tuple0x8cfc0927]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (order, taker_address) = self.validate_and_normalize_inputs(
            order, taker_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(order, taker_address).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self,
        order: Tuple0x260219a2,
        taker_address: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (order, taker_address) = self.validate_and_normalize_inputs(
            order, taker_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order, taker_address).estimateGas(
            tx_params.as_dict()
        )


class GetBalanceAndAllowanceMethod(ContractMethod):
    """Various interfaces to the getBalanceAndAllowance method."""

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
        self, target: str, asset_data: Union[bytes, str]
    ):
        """Validate the inputs to the getBalanceAndAllowance method."""
        self.validator.assert_valid(
            method_name="getBalanceAndAllowance",
            parameter_name="target",
            argument_value=target,
        )
        target = self.validate_and_checksum_address(target)
        self.validator.assert_valid(
            method_name="getBalanceAndAllowance",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (target, asset_data)

    def call(
        self,
        target: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (target, asset_data) = self.validate_and_normalize_inputs(
            target, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(target, asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self,
        target: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (target, asset_data) = self.validate_and_normalize_inputs(
            target, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target, asset_data).estimateGas(
            tx_params.as_dict()
        )


class GetOrdersAndTradersInfoMethod(ContractMethod):
    """Various interfaces to the getOrdersAndTradersInfo method."""

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
        self, orders: List[Tuple0x260219a2], taker_addresses: List[str]
    ):
        """Validate the inputs to the getOrdersAndTradersInfo method."""
        self.validator.assert_valid(
            method_name="getOrdersAndTradersInfo",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="getOrdersAndTradersInfo",
            parameter_name="takerAddresses",
            argument_value=taker_addresses,
        )
        return (orders, taker_addresses)

    def call(
        self,
        orders: List[Tuple0x260219a2],
        taker_addresses: List[str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[List[Tuple0xb1e4a1ae], List[Tuple0x8cfc0927]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (orders, taker_addresses) = self.validate_and_normalize_inputs(
            orders, taker_addresses
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(orders, taker_addresses).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self,
        orders: List[Tuple0x260219a2],
        taker_addresses: List[str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (orders, taker_addresses) = self.validate_and_normalize_inputs(
            orders, taker_addresses
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(orders, taker_addresses).estimateGas(
            tx_params.as_dict()
        )


class GetTradersInfoMethod(ContractMethod):
    """Various interfaces to the getTradersInfo method."""

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
        self, orders: List[Tuple0x260219a2], taker_addresses: List[str]
    ):
        """Validate the inputs to the getTradersInfo method."""
        self.validator.assert_valid(
            method_name="getTradersInfo",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="getTradersInfo",
            parameter_name="takerAddresses",
            argument_value=taker_addresses,
        )
        return (orders, taker_addresses)

    def call(
        self,
        orders: List[Tuple0x260219a2],
        taker_addresses: List[str],
        tx_params: Optional[TxParams] = None,
    ) -> List[Tuple0x8cfc0927]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (orders, taker_addresses) = self.validate_and_normalize_inputs(
            orders, taker_addresses
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(orders, taker_addresses).call(
            tx_params.as_dict()
        )
        return [
            Tuple0x8cfc0927(
                makerBalance=element[0],
                makerAllowance=element[1],
                takerBalance=element[2],
                takerAllowance=element[3],
                makerZrxBalance=element[4],
                makerZrxAllowance=element[5],
                takerZrxBalance=element[6],
                takerZrxAllowance=element[7],
            )
            for element in returned
        ]

    def estimate_gas(
        self,
        orders: List[Tuple0x260219a2],
        taker_addresses: List[str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (orders, taker_addresses) = self.validate_and_normalize_inputs(
            orders, taker_addresses
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(orders, taker_addresses).estimateGas(
            tx_params.as_dict()
        )


class GetErc721TokenOwnerMethod(ContractMethod):
    """Various interfaces to the getERC721TokenOwner method."""

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

    def validate_and_normalize_inputs(self, token: str, token_id: int):
        """Validate the inputs to the getERC721TokenOwner method."""
        self.validator.assert_valid(
            method_name="getERC721TokenOwner",
            parameter_name="token",
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        self.validator.assert_valid(
            method_name="getERC721TokenOwner",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (token, token_id)

    def call(
        self, token: str, token_id: int, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (token, token_id) = self.validate_and_normalize_inputs(token, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token, token_id).call(
            tx_params.as_dict()
        )
        return str(returned)

    def estimate_gas(
        self, token: str, token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token, token_id) = self.validate_and_normalize_inputs(token, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, token_id).estimateGas(
            tx_params.as_dict()
        )


class GetBalancesAndAllowancesMethod(ContractMethod):
    """Various interfaces to the getBalancesAndAllowances method."""

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
        self, target: str, asset_data: List[Union[bytes, str]]
    ):
        """Validate the inputs to the getBalancesAndAllowances method."""
        self.validator.assert_valid(
            method_name="getBalancesAndAllowances",
            parameter_name="target",
            argument_value=target,
        )
        target = self.validate_and_checksum_address(target)
        self.validator.assert_valid(
            method_name="getBalancesAndAllowances",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (target, asset_data)

    def call(
        self,
        target: str,
        asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[List[int], List[int]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (target, asset_data) = self.validate_and_normalize_inputs(
            target, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(target, asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self,
        target: str,
        asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (target, asset_data) = self.validate_and_normalize_inputs(
            target, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target, asset_data).estimateGas(
            tx_params.as_dict()
        )


class GetTraderInfoMethod(ContractMethod):
    """Various interfaces to the getTraderInfo method."""

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
        self, order: Tuple0x260219a2, taker_address: str
    ):
        """Validate the inputs to the getTraderInfo method."""
        self.validator.assert_valid(
            method_name="getTraderInfo",
            parameter_name="order",
            argument_value=order,
        )
        self.validator.assert_valid(
            method_name="getTraderInfo",
            parameter_name="takerAddress",
            argument_value=taker_address,
        )
        taker_address = self.validate_and_checksum_address(taker_address)
        return (order, taker_address)

    def call(
        self,
        order: Tuple0x260219a2,
        taker_address: str,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple0x8cfc0927:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (order, taker_address) = self.validate_and_normalize_inputs(
            order, taker_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(order, taker_address).call(
            tx_params.as_dict()
        )
        return Tuple0x8cfc0927(
            makerBalance=returned[0],
            makerAllowance=returned[1],
            takerBalance=returned[2],
            takerAllowance=returned[3],
            makerZrxBalance=returned[4],
            makerZrxAllowance=returned[5],
            takerZrxBalance=returned[6],
            takerZrxAllowance=returned[7],
        )

    def estimate_gas(
        self,
        order: Tuple0x260219a2,
        taker_address: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (order, taker_address) = self.validate_and_normalize_inputs(
            order, taker_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order, taker_address).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class OrderValidator:
    """Wrapper class for OrderValidator Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    get_order_and_trader_info: GetOrderAndTraderInfoMethod
    """Constructor-initialized instance of
    :class:`GetOrderAndTraderInfoMethod`.
    """

    get_balance_and_allowance: GetBalanceAndAllowanceMethod
    """Constructor-initialized instance of
    :class:`GetBalanceAndAllowanceMethod`.
    """

    get_orders_and_traders_info: GetOrdersAndTradersInfoMethod
    """Constructor-initialized instance of
    :class:`GetOrdersAndTradersInfoMethod`.
    """

    get_traders_info: GetTradersInfoMethod
    """Constructor-initialized instance of
    :class:`GetTradersInfoMethod`.
    """

    get_erc721_token_owner: GetErc721TokenOwnerMethod
    """Constructor-initialized instance of
    :class:`GetErc721TokenOwnerMethod`.
    """

    get_balances_and_allowances: GetBalancesAndAllowancesMethod
    """Constructor-initialized instance of
    :class:`GetBalancesAndAllowancesMethod`.
    """

    get_trader_info: GetTraderInfoMethod
    """Constructor-initialized instance of
    :class:`GetTraderInfoMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: OrderValidatorValidator = None,
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
            validator = OrderValidatorValidator(
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
            abi=OrderValidator.abi(),
        ).functions

        self.get_order_and_trader_info = GetOrderAndTraderInfoMethod(
            web3_or_provider,
            contract_address,
            functions.getOrderAndTraderInfo,
            validator,
        )

        self.get_balance_and_allowance = GetBalanceAndAllowanceMethod(
            web3_or_provider,
            contract_address,
            functions.getBalanceAndAllowance,
            validator,
        )

        self.get_orders_and_traders_info = GetOrdersAndTradersInfoMethod(
            web3_or_provider,
            contract_address,
            functions.getOrdersAndTradersInfo,
            validator,
        )

        self.get_traders_info = GetTradersInfoMethod(
            web3_or_provider,
            contract_address,
            functions.getTradersInfo,
            validator,
        )

        self.get_erc721_token_owner = GetErc721TokenOwnerMethod(
            web3_or_provider,
            contract_address,
            functions.getERC721TokenOwner,
            validator,
        )

        self.get_balances_and_allowances = GetBalancesAndAllowancesMethod(
            web3_or_provider,
            contract_address,
            functions.getBalancesAndAllowances,
            validator,
        )

        self.get_trader_info = GetTraderInfoMethod(
            web3_or_provider,
            contract_address,
            functions.getTraderInfo,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":true,"inputs":[{"components":[{"name":"makerAddress","type":"address"},{"name":"takerAddress","type":"address"},{"name":"feeRecipientAddress","type":"address"},{"name":"senderAddress","type":"address"},{"name":"makerAssetAmount","type":"uint256"},{"name":"takerAssetAmount","type":"uint256"},{"name":"makerFee","type":"uint256"},{"name":"takerFee","type":"uint256"},{"name":"expirationTimeSeconds","type":"uint256"},{"name":"salt","type":"uint256"},{"name":"makerAssetData","type":"bytes"},{"name":"takerAssetData","type":"bytes"}],"name":"order","type":"tuple"},{"name":"takerAddress","type":"address"}],"name":"getOrderAndTraderInfo","outputs":[{"components":[{"name":"orderStatus","type":"uint8"},{"name":"orderHash","type":"bytes32"},{"name":"orderTakerAssetFilledAmount","type":"uint256"}],"name":"orderInfo","type":"tuple"},{"components":[{"name":"makerBalance","type":"uint256"},{"name":"makerAllowance","type":"uint256"},{"name":"takerBalance","type":"uint256"},{"name":"takerAllowance","type":"uint256"},{"name":"makerZrxBalance","type":"uint256"},{"name":"makerZrxAllowance","type":"uint256"},{"name":"takerZrxBalance","type":"uint256"},{"name":"takerZrxAllowance","type":"uint256"}],"name":"traderInfo","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"target","type":"address"},{"name":"assetData","type":"bytes"}],"name":"getBalanceAndAllowance","outputs":[{"name":"balance","type":"uint256"},{"name":"allowance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"name":"makerAddress","type":"address"},{"name":"takerAddress","type":"address"},{"name":"feeRecipientAddress","type":"address"},{"name":"senderAddress","type":"address"},{"name":"makerAssetAmount","type":"uint256"},{"name":"takerAssetAmount","type":"uint256"},{"name":"makerFee","type":"uint256"},{"name":"takerFee","type":"uint256"},{"name":"expirationTimeSeconds","type":"uint256"},{"name":"salt","type":"uint256"},{"name":"makerAssetData","type":"bytes"},{"name":"takerAssetData","type":"bytes"}],"name":"orders","type":"tuple[]"},{"name":"takerAddresses","type":"address[]"}],"name":"getOrdersAndTradersInfo","outputs":[{"components":[{"name":"orderStatus","type":"uint8"},{"name":"orderHash","type":"bytes32"},{"name":"orderTakerAssetFilledAmount","type":"uint256"}],"name":"ordersInfo","type":"tuple[]"},{"components":[{"name":"makerBalance","type":"uint256"},{"name":"makerAllowance","type":"uint256"},{"name":"takerBalance","type":"uint256"},{"name":"takerAllowance","type":"uint256"},{"name":"makerZrxBalance","type":"uint256"},{"name":"makerZrxAllowance","type":"uint256"},{"name":"takerZrxBalance","type":"uint256"},{"name":"takerZrxAllowance","type":"uint256"}],"name":"tradersInfo","type":"tuple[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"name":"makerAddress","type":"address"},{"name":"takerAddress","type":"address"},{"name":"feeRecipientAddress","type":"address"},{"name":"senderAddress","type":"address"},{"name":"makerAssetAmount","type":"uint256"},{"name":"takerAssetAmount","type":"uint256"},{"name":"makerFee","type":"uint256"},{"name":"takerFee","type":"uint256"},{"name":"expirationTimeSeconds","type":"uint256"},{"name":"salt","type":"uint256"},{"name":"makerAssetData","type":"bytes"},{"name":"takerAssetData","type":"bytes"}],"name":"orders","type":"tuple[]"},{"name":"takerAddresses","type":"address[]"}],"name":"getTradersInfo","outputs":[{"components":[{"name":"makerBalance","type":"uint256"},{"name":"makerAllowance","type":"uint256"},{"name":"takerBalance","type":"uint256"},{"name":"takerAllowance","type":"uint256"},{"name":"makerZrxBalance","type":"uint256"},{"name":"makerZrxAllowance","type":"uint256"},{"name":"takerZrxBalance","type":"uint256"},{"name":"takerZrxAllowance","type":"uint256"}],"name":"","type":"tuple[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"token","type":"address"},{"name":"tokenId","type":"uint256"}],"name":"getERC721TokenOwner","outputs":[{"name":"owner","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"target","type":"address"},{"name":"assetData","type":"bytes[]"}],"name":"getBalancesAndAllowances","outputs":[{"name":"","type":"uint256[]"},{"name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"name":"makerAddress","type":"address"},{"name":"takerAddress","type":"address"},{"name":"feeRecipientAddress","type":"address"},{"name":"senderAddress","type":"address"},{"name":"makerAssetAmount","type":"uint256"},{"name":"takerAssetAmount","type":"uint256"},{"name":"makerFee","type":"uint256"},{"name":"takerFee","type":"uint256"},{"name":"expirationTimeSeconds","type":"uint256"},{"name":"salt","type":"uint256"},{"name":"makerAssetData","type":"bytes"},{"name":"takerAssetData","type":"bytes"}],"name":"order","type":"tuple"},{"name":"takerAddress","type":"address"}],"name":"getTraderInfo","outputs":[{"components":[{"name":"makerBalance","type":"uint256"},{"name":"makerAllowance","type":"uint256"},{"name":"takerBalance","type":"uint256"},{"name":"takerAllowance","type":"uint256"},{"name":"makerZrxBalance","type":"uint256"},{"name":"makerZrxAllowance","type":"uint256"},{"name":"takerZrxBalance","type":"uint256"},{"name":"takerZrxAllowance","type":"uint256"}],"name":"traderInfo","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_exchange","type":"address"},{"name":"_zrxAssetData","type":"bytes"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
