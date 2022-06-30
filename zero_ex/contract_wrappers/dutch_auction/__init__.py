"""Generated wrapper for DutchAuction Solidity contract."""

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
# constructor for DutchAuction below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DutchAuctionValidator,
    )
except ImportError:

    class DutchAuctionValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class Tuple0xbb41e5b3(TypedDict):
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

    makerAssetFilledAmount: int

    takerAssetFilledAmount: int

    makerFeePaid: int

    takerFeePaid: int


class Tuple0x054ca44e(TypedDict):
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

    left: Tuple0xbb41e5b3

    right: Tuple0xbb41e5b3

    leftMakerAssetSpreadAmount: int


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


class Tuple0xdc58a88c(TypedDict):
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

    beginTimeSeconds: int

    endTimeSeconds: int

    beginAmount: int

    endAmount: int

    currentAmount: int

    currentTimeSeconds: int


class GetAuctionDetailsMethod(ContractMethod):
    """Various interfaces to the getAuctionDetails method."""

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

    def validate_and_normalize_inputs(self, order: Tuple0x260219a2):
        """Validate the inputs to the getAuctionDetails method."""
        self.validator.assert_valid(
            method_name="getAuctionDetails",
            parameter_name="order",
            argument_value=order,
        )
        return order

    def call(
        self, order: Tuple0x260219a2, tx_params: Optional[TxParams] = None
    ) -> Tuple0xdc58a88c:
        """Execute underlying contract method via eth_call.

        Calculates the Auction Details for the given order

        :param order: The sell order
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(order).call(tx_params.as_dict())
        return Tuple0xdc58a88c(
            beginTimeSeconds=returned[0],
            endTimeSeconds=returned[1],
            beginAmount=returned[2],
            endAmount=returned[3],
            currentAmount=returned[4],
            currentTimeSeconds=returned[5],
        )

    def send_transaction(
        self, order: Tuple0x260219a2, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Calculates the Auction Details for the given order

        :param order: The sell order
        :param tx_params: transaction parameters
        """
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order).transact(tx_params.as_dict())

    def build_transaction(
        self, order: Tuple0x260219a2, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, order: Tuple0x260219a2, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order).estimateGas(tx_params.as_dict())


class MatchOrdersMethod(ContractMethod):
    """Various interfaces to the matchOrders method."""

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
        buy_order: Tuple0x260219a2,
        sell_order: Tuple0x260219a2,
        buy_signature: Union[bytes, str],
        sell_signature: Union[bytes, str],
    ):
        """Validate the inputs to the matchOrders method."""
        self.validator.assert_valid(
            method_name="matchOrders",
            parameter_name="buyOrder",
            argument_value=buy_order,
        )
        self.validator.assert_valid(
            method_name="matchOrders",
            parameter_name="sellOrder",
            argument_value=sell_order,
        )
        self.validator.assert_valid(
            method_name="matchOrders",
            parameter_name="buySignature",
            argument_value=buy_signature,
        )
        self.validator.assert_valid(
            method_name="matchOrders",
            parameter_name="sellSignature",
            argument_value=sell_signature,
        )
        return (buy_order, sell_order, buy_signature, sell_signature)

    def call(
        self,
        buy_order: Tuple0x260219a2,
        sell_order: Tuple0x260219a2,
        buy_signature: Union[bytes, str],
        sell_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple0x054ca44e:
        """Execute underlying contract method via eth_call.

        Matches the buy and sell orders at an amount given the following: the
        current block time, the auction start time and the auction begin
        amount. The sell order is a an order at the lowest amount at the end of
        the auction. Excess from the match is transferred to the seller. Over
        time the price moves from beginAmount to endAmount given the current
        block.timestamp. sellOrder.expiryTimeSeconds is the end time of the
        auction. sellOrder.takerAssetAmount is the end amount of the auction
        (lowest possible amount). sellOrder.makerAssetData is the ABI encoded
        Asset Proxy data with the following data appended
        buyOrder.makerAssetData is the buyers bid on the auction, must meet the
        amount for the current block timestamp (uint256 beginTimeSeconds,
        uint256 beginAmount). This function reverts in the following scenarios:
        * Auction has not started (auctionDetails.currentTimeSeconds <
        auctionDetails.beginTimeSeconds) * Auction has expired
        (auctionDetails.endTimeSeconds < auctionDetails.currentTimeSeconds) *
        Amount is invalid: Buy order amount is too low
        (buyOrder.makerAssetAmount < auctionDetails.currentAmount) * Amount is
        invalid: Invalid begin amount (auctionDetails.beginAmount >
        auctionDetails.endAmount) * Any failure in the 0x Match Orders

        :param buyOrder: The Buyer's order. This order is for the current
            expected price of the auction.
        :param buySignature: Proof that order was created by the buyer.
        :param sellOrder: The Seller's order. This order is for the lowest
            amount (at the end of the auction).
        :param sellSignature: Proof that order was created by the seller.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            buy_order,
            sell_order,
            buy_signature,
            sell_signature,
        ) = self.validate_and_normalize_inputs(
            buy_order, sell_order, buy_signature, sell_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            buy_order, sell_order, buy_signature, sell_signature
        ).call(tx_params.as_dict())
        return Tuple0x054ca44e(
            left=returned[0],
            right=returned[1],
            leftMakerAssetSpreadAmount=returned[2],
        )

    def send_transaction(
        self,
        buy_order: Tuple0x260219a2,
        sell_order: Tuple0x260219a2,
        buy_signature: Union[bytes, str],
        sell_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Matches the buy and sell orders at an amount given the following: the
        current block time, the auction start time and the auction begin
        amount. The sell order is a an order at the lowest amount at the end of
        the auction. Excess from the match is transferred to the seller. Over
        time the price moves from beginAmount to endAmount given the current
        block.timestamp. sellOrder.expiryTimeSeconds is the end time of the
        auction. sellOrder.takerAssetAmount is the end amount of the auction
        (lowest possible amount). sellOrder.makerAssetData is the ABI encoded
        Asset Proxy data with the following data appended
        buyOrder.makerAssetData is the buyers bid on the auction, must meet the
        amount for the current block timestamp (uint256 beginTimeSeconds,
        uint256 beginAmount). This function reverts in the following scenarios:
        * Auction has not started (auctionDetails.currentTimeSeconds <
        auctionDetails.beginTimeSeconds) * Auction has expired
        (auctionDetails.endTimeSeconds < auctionDetails.currentTimeSeconds) *
        Amount is invalid: Buy order amount is too low
        (buyOrder.makerAssetAmount < auctionDetails.currentAmount) * Amount is
        invalid: Invalid begin amount (auctionDetails.beginAmount >
        auctionDetails.endAmount) * Any failure in the 0x Match Orders

        :param buyOrder: The Buyer's order. This order is for the current
            expected price of the auction.
        :param buySignature: Proof that order was created by the buyer.
        :param sellOrder: The Seller's order. This order is for the lowest
            amount (at the end of the auction).
        :param sellSignature: Proof that order was created by the seller.
        :param tx_params: transaction parameters
        """
        (
            buy_order,
            sell_order,
            buy_signature,
            sell_signature,
        ) = self.validate_and_normalize_inputs(
            buy_order, sell_order, buy_signature, sell_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            buy_order, sell_order, buy_signature, sell_signature
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        buy_order: Tuple0x260219a2,
        sell_order: Tuple0x260219a2,
        buy_signature: Union[bytes, str],
        sell_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            buy_order,
            sell_order,
            buy_signature,
            sell_signature,
        ) = self.validate_and_normalize_inputs(
            buy_order, sell_order, buy_signature, sell_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            buy_order, sell_order, buy_signature, sell_signature
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        buy_order: Tuple0x260219a2,
        sell_order: Tuple0x260219a2,
        buy_signature: Union[bytes, str],
        sell_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            buy_order,
            sell_order,
            buy_signature,
            sell_signature,
        ) = self.validate_and_normalize_inputs(
            buy_order, sell_order, buy_signature, sell_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            buy_order, sell_order, buy_signature, sell_signature
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DutchAuction:
    """Wrapper class for DutchAuction Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    get_auction_details: GetAuctionDetailsMethod
    """Constructor-initialized instance of
    :class:`GetAuctionDetailsMethod`.
    """

    match_orders: MatchOrdersMethod
    """Constructor-initialized instance of
    :class:`MatchOrdersMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: DutchAuctionValidator = None,
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
            validator = DutchAuctionValidator(
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
            abi=DutchAuction.abi(),
        ).functions

        self.get_auction_details = GetAuctionDetailsMethod(
            web3_or_provider,
            contract_address,
            functions.getAuctionDetails,
            validator,
        )

        self.match_orders = MatchOrdersMethod(
            web3_or_provider,
            contract_address,
            functions.matchOrders,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":false,"inputs":[{"components":[{"name":"makerAddress","type":"address"},{"name":"takerAddress","type":"address"},{"name":"feeRecipientAddress","type":"address"},{"name":"senderAddress","type":"address"},{"name":"makerAssetAmount","type":"uint256"},{"name":"takerAssetAmount","type":"uint256"},{"name":"makerFee","type":"uint256"},{"name":"takerFee","type":"uint256"},{"name":"expirationTimeSeconds","type":"uint256"},{"name":"salt","type":"uint256"},{"name":"makerAssetData","type":"bytes"},{"name":"takerAssetData","type":"bytes"}],"name":"order","type":"tuple"}],"name":"getAuctionDetails","outputs":[{"components":[{"name":"beginTimeSeconds","type":"uint256"},{"name":"endTimeSeconds","type":"uint256"},{"name":"beginAmount","type":"uint256"},{"name":"endAmount","type":"uint256"},{"name":"currentAmount","type":"uint256"},{"name":"currentTimeSeconds","type":"uint256"}],"name":"auctionDetails","type":"tuple"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"components":[{"name":"makerAddress","type":"address"},{"name":"takerAddress","type":"address"},{"name":"feeRecipientAddress","type":"address"},{"name":"senderAddress","type":"address"},{"name":"makerAssetAmount","type":"uint256"},{"name":"takerAssetAmount","type":"uint256"},{"name":"makerFee","type":"uint256"},{"name":"takerFee","type":"uint256"},{"name":"expirationTimeSeconds","type":"uint256"},{"name":"salt","type":"uint256"},{"name":"makerAssetData","type":"bytes"},{"name":"takerAssetData","type":"bytes"}],"name":"buyOrder","type":"tuple"},{"components":[{"name":"makerAddress","type":"address"},{"name":"takerAddress","type":"address"},{"name":"feeRecipientAddress","type":"address"},{"name":"senderAddress","type":"address"},{"name":"makerAssetAmount","type":"uint256"},{"name":"takerAssetAmount","type":"uint256"},{"name":"makerFee","type":"uint256"},{"name":"takerFee","type":"uint256"},{"name":"expirationTimeSeconds","type":"uint256"},{"name":"salt","type":"uint256"},{"name":"makerAssetData","type":"bytes"},{"name":"takerAssetData","type":"bytes"}],"name":"sellOrder","type":"tuple"},{"name":"buySignature","type":"bytes"},{"name":"sellSignature","type":"bytes"}],"name":"matchOrders","outputs":[{"components":[{"components":[{"name":"makerAssetFilledAmount","type":"uint256"},{"name":"takerAssetFilledAmount","type":"uint256"},{"name":"makerFeePaid","type":"uint256"},{"name":"takerFeePaid","type":"uint256"}],"name":"left","type":"tuple"},{"components":[{"name":"makerAssetFilledAmount","type":"uint256"},{"name":"takerAssetFilledAmount","type":"uint256"},{"name":"makerFeePaid","type":"uint256"},{"name":"takerFeePaid","type":"uint256"}],"name":"right","type":"tuple"},{"name":"leftMakerAssetSpreadAmount","type":"uint256"}],"name":"matchedFillResults","type":"tuple"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_exchange","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
