"""Generated wrapper for Exchange Solidity contract."""

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
# constructor for Exchange below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ExchangeValidator,
    )
except ImportError:

    class ExchangeValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class LibFillResultsFillResults(TypedDict):
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

    protocolFeePaid: int


class LibFillResultsBatchMatchedFillResults(TypedDict):
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

    left: List[LibFillResultsFillResults]

    right: List[LibFillResultsFillResults]

    profitInLeftMakerAsset: int

    profitInRightMakerAsset: int


class LibFillResultsMatchedFillResults(TypedDict):
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

    left: LibFillResultsFillResults

    right: LibFillResultsFillResults

    profitInLeftMakerAsset: int

    profitInRightMakerAsset: int


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


class LibZeroExTransactionZeroExTransaction(TypedDict):
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

    salt: int

    expirationTimeSeconds: int

    gasPrice: int

    signerAddress: str

    data: Union[bytes, str]


class LibOrderOrderInfo(TypedDict):
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


class Eip1271MagicValueMethod(ContractMethod):
    """Various interfaces to the EIP1271_MAGIC_VALUE method."""

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

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class Eip712ExchangeDomainHashMethod(ContractMethod):
    """Various interfaces to the EIP712_EXCHANGE_DOMAIN_HASH method."""

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

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class AllowedValidatorsMethod(ContractMethod):
    """Various interfaces to the allowedValidators method."""

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

    def validate_and_normalize_inputs(self, index_0: str, index_1: str):
        """Validate the inputs to the allowedValidators method."""
        self.validator.assert_valid(
            method_name="allowedValidators",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="allowedValidators",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)

    def call(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def estimate_gas(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class BatchCancelOrdersMethod(ContractMethod):
    """Various interfaces to the batchCancelOrders method."""

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

    def validate_and_normalize_inputs(self, orders: List[LibOrderOrder]):
        """Validate the inputs to the batchCancelOrders method."""
        self.validator.assert_valid(
            method_name="batchCancelOrders",
            parameter_name="orders",
            argument_value=orders,
        )
        return orders

    def call(
        self, orders: List[LibOrderOrder], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Executes multiple calls of cancelOrder.

        :param orders: Array of order specifications.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (orders) = self.validate_and_normalize_inputs(orders)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(orders).call(tx_params.as_dict())

    def send_transaction(
        self, orders: List[LibOrderOrder], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes multiple calls of cancelOrder.

        :param orders: Array of order specifications.
        :param tx_params: transaction parameters
        """
        (orders) = self.validate_and_normalize_inputs(orders)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(orders).transact(tx_params.as_dict())

    def build_transaction(
        self, orders: List[LibOrderOrder], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (orders) = self.validate_and_normalize_inputs(orders)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(orders).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, orders: List[LibOrderOrder], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (orders) = self.validate_and_normalize_inputs(orders)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(orders).estimateGas(tx_params.as_dict())


class BatchExecuteTransactionsMethod(ContractMethod):
    """Various interfaces to the batchExecuteTransactions method."""

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
        transactions: List[LibZeroExTransactionZeroExTransaction],
        signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the batchExecuteTransactions method."""
        self.validator.assert_valid(
            method_name="batchExecuteTransactions",
            parameter_name="transactions",
            argument_value=transactions,
        )
        self.validator.assert_valid(
            method_name="batchExecuteTransactions",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (transactions, signatures)

    def call(
        self,
        transactions: List[LibZeroExTransactionZeroExTransaction],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Executes a batch of Exchange method calls in the context of signer(s).

        :param signatures: Array of proofs that transactions have been signed
            by signer(s).
        :param transactions: Array of 0x transaction structures.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (transactions, signatures) = self.validate_and_normalize_inputs(
            transactions, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(transactions, signatures).call(
            tx_params.as_dict()
        )
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(
        self,
        transactions: List[LibZeroExTransactionZeroExTransaction],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes a batch of Exchange method calls in the context of signer(s).

        :param signatures: Array of proofs that transactions have been signed
            by signer(s).
        :param transactions: Array of 0x transaction structures.
        :param tx_params: transaction parameters
        """
        (transactions, signatures) = self.validate_and_normalize_inputs(
            transactions, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transactions, signatures).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        transactions: List[LibZeroExTransactionZeroExTransaction],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (transactions, signatures) = self.validate_and_normalize_inputs(
            transactions, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            transactions, signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        transactions: List[LibZeroExTransactionZeroExTransaction],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (transactions, signatures) = self.validate_and_normalize_inputs(
            transactions, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transactions, signatures).estimateGas(
            tx_params.as_dict()
        )


class BatchFillOrKillOrdersMethod(ContractMethod):
    """Various interfaces to the batchFillOrKillOrders method."""

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
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the batchFillOrKillOrders method."""
        self.validator.assert_valid(
            method_name="batchFillOrKillOrders",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="batchFillOrKillOrders",
            parameter_name="takerAssetFillAmounts",
            argument_value=taker_asset_fill_amounts,
        )
        self.validator.assert_valid(
            method_name="batchFillOrKillOrders",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (orders, taker_asset_fill_amounts, signatures)

    def call(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[LibFillResultsFillResults]:
        """Execute underlying contract method via eth_call.

        Executes multiple calls of fillOrKillOrder.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been created by makers.
        :param takerAssetFillAmounts: Array of desired amounts of takerAsset to
            sell in orders.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).call(tx_params.as_dict())
        return [
            LibFillResultsFillResults(
                makerAssetFilledAmount=element[0],
                takerAssetFilledAmount=element[1],
                makerFeePaid=element[2],
                takerFeePaid=element[3],
                protocolFeePaid=element[4],
            )
            for element in returned
        ]

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes multiple calls of fillOrKillOrder.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been created by makers.
        :param takerAssetFillAmounts: Array of desired amounts of takerAsset to
            sell in orders.
        :param tx_params: transaction parameters
        """
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).estimateGas(tx_params.as_dict())


class BatchFillOrdersMethod(ContractMethod):
    """Various interfaces to the batchFillOrders method."""

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
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the batchFillOrders method."""
        self.validator.assert_valid(
            method_name="batchFillOrders",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="batchFillOrders",
            parameter_name="takerAssetFillAmounts",
            argument_value=taker_asset_fill_amounts,
        )
        self.validator.assert_valid(
            method_name="batchFillOrders",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (orders, taker_asset_fill_amounts, signatures)

    def call(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[LibFillResultsFillResults]:
        """Execute underlying contract method via eth_call.

        Executes multiple calls of fillOrder.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been created by makers.
        :param takerAssetFillAmounts: Array of desired amounts of takerAsset to
            sell in orders.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).call(tx_params.as_dict())
        return [
            LibFillResultsFillResults(
                makerAssetFilledAmount=element[0],
                takerAssetFilledAmount=element[1],
                makerFeePaid=element[2],
                takerFeePaid=element[3],
                protocolFeePaid=element[4],
            )
            for element in returned
        ]

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes multiple calls of fillOrder.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been created by makers.
        :param takerAssetFillAmounts: Array of desired amounts of takerAsset to
            sell in orders.
        :param tx_params: transaction parameters
        """
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).estimateGas(tx_params.as_dict())


class BatchFillOrdersNoThrowMethod(ContractMethod):
    """Various interfaces to the batchFillOrdersNoThrow method."""

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
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the batchFillOrdersNoThrow method."""
        self.validator.assert_valid(
            method_name="batchFillOrdersNoThrow",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="batchFillOrdersNoThrow",
            parameter_name="takerAssetFillAmounts",
            argument_value=taker_asset_fill_amounts,
        )
        self.validator.assert_valid(
            method_name="batchFillOrdersNoThrow",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (orders, taker_asset_fill_amounts, signatures)

    def call(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[LibFillResultsFillResults]:
        """Execute underlying contract method via eth_call.

        Executes multiple calls of fillOrder. If any fill reverts, the error is
        caught and ignored.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been created by makers.
        :param takerAssetFillAmounts: Array of desired amounts of takerAsset to
            sell in orders.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).call(tx_params.as_dict())
        return [
            LibFillResultsFillResults(
                makerAssetFilledAmount=element[0],
                takerAssetFilledAmount=element[1],
                makerFeePaid=element[2],
                takerFeePaid=element[3],
                protocolFeePaid=element[4],
            )
            for element in returned
        ]

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes multiple calls of fillOrder. If any fill reverts, the error is
        caught and ignored.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been created by makers.
        :param takerAssetFillAmounts: Array of desired amounts of takerAsset to
            sell in orders.
        :param tx_params: transaction parameters
        """
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amounts: List[int],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            taker_asset_fill_amounts,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amounts, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amounts, signatures
        ).estimateGas(tx_params.as_dict())


class BatchMatchOrdersMethod(ContractMethod):
    """Various interfaces to the batchMatchOrders method."""

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
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the batchMatchOrders method."""
        self.validator.assert_valid(
            method_name="batchMatchOrders",
            parameter_name="leftOrders",
            argument_value=left_orders,
        )
        self.validator.assert_valid(
            method_name="batchMatchOrders",
            parameter_name="rightOrders",
            argument_value=right_orders,
        )
        self.validator.assert_valid(
            method_name="batchMatchOrders",
            parameter_name="leftSignatures",
            argument_value=left_signatures,
        )
        self.validator.assert_valid(
            method_name="batchMatchOrders",
            parameter_name="rightSignatures",
            argument_value=right_signatures,
        )
        return (left_orders, right_orders, left_signatures, right_signatures)

    def call(
        self,
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsBatchMatchedFillResults:
        """Execute underlying contract method via eth_call.

        Match complementary orders that have a profitable spread. Each order is
        filled at their respective price point, and the matcher receives a
        profit denominated in the left maker asset.

        :param leftOrders: Set of orders with the same maker / taker asset.
        :param leftSignatures: Proof that left orders were created by the left
            makers.
        :param rightOrders: Set of orders to match against `leftOrders`
        :param rightSignatures: Proof that right orders were created by the
            right makers.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            left_orders,
            right_orders,
            left_signatures,
            right_signatures,
        ) = self.validate_and_normalize_inputs(
            left_orders, right_orders, left_signatures, right_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            left_orders, right_orders, left_signatures, right_signatures
        ).call(tx_params.as_dict())
        return LibFillResultsBatchMatchedFillResults(
            left=returned[0],
            right=returned[1],
            profitInLeftMakerAsset=returned[2],
            profitInRightMakerAsset=returned[3],
        )

    def send_transaction(
        self,
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Match complementary orders that have a profitable spread. Each order is
        filled at their respective price point, and the matcher receives a
        profit denominated in the left maker asset.

        :param leftOrders: Set of orders with the same maker / taker asset.
        :param leftSignatures: Proof that left orders were created by the left
            makers.
        :param rightOrders: Set of orders to match against `leftOrders`
        :param rightSignatures: Proof that right orders were created by the
            right makers.
        :param tx_params: transaction parameters
        """
        (
            left_orders,
            right_orders,
            left_signatures,
            right_signatures,
        ) = self.validate_and_normalize_inputs(
            left_orders, right_orders, left_signatures, right_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_orders, right_orders, left_signatures, right_signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            left_orders,
            right_orders,
            left_signatures,
            right_signatures,
        ) = self.validate_and_normalize_inputs(
            left_orders, right_orders, left_signatures, right_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_orders, right_orders, left_signatures, right_signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            left_orders,
            right_orders,
            left_signatures,
            right_signatures,
        ) = self.validate_and_normalize_inputs(
            left_orders, right_orders, left_signatures, right_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_orders, right_orders, left_signatures, right_signatures
        ).estimateGas(tx_params.as_dict())


class BatchMatchOrdersWithMaximalFillMethod(ContractMethod):
    """Various interfaces to the batchMatchOrdersWithMaximalFill method."""

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
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the batchMatchOrdersWithMaximalFill method."""
        self.validator.assert_valid(
            method_name="batchMatchOrdersWithMaximalFill",
            parameter_name="leftOrders",
            argument_value=left_orders,
        )
        self.validator.assert_valid(
            method_name="batchMatchOrdersWithMaximalFill",
            parameter_name="rightOrders",
            argument_value=right_orders,
        )
        self.validator.assert_valid(
            method_name="batchMatchOrdersWithMaximalFill",
            parameter_name="leftSignatures",
            argument_value=left_signatures,
        )
        self.validator.assert_valid(
            method_name="batchMatchOrdersWithMaximalFill",
            parameter_name="rightSignatures",
            argument_value=right_signatures,
        )
        return (left_orders, right_orders, left_signatures, right_signatures)

    def call(
        self,
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsBatchMatchedFillResults:
        """Execute underlying contract method via eth_call.

        Match complementary orders that have a profitable spread. Each order is
        maximally filled at their respective price point, and the matcher
        receives a profit denominated in either the left maker asset, right
        maker asset, or a combination of both.

        :param leftOrders: Set of orders with the same maker / taker asset.
        :param leftSignatures: Proof that left orders were created by the left
            makers.
        :param rightOrders: Set of orders to match against `leftOrders`
        :param rightSignatures: Proof that right orders were created by the
            right makers.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            left_orders,
            right_orders,
            left_signatures,
            right_signatures,
        ) = self.validate_and_normalize_inputs(
            left_orders, right_orders, left_signatures, right_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            left_orders, right_orders, left_signatures, right_signatures
        ).call(tx_params.as_dict())
        return LibFillResultsBatchMatchedFillResults(
            left=returned[0],
            right=returned[1],
            profitInLeftMakerAsset=returned[2],
            profitInRightMakerAsset=returned[3],
        )

    def send_transaction(
        self,
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Match complementary orders that have a profitable spread. Each order is
        maximally filled at their respective price point, and the matcher
        receives a profit denominated in either the left maker asset, right
        maker asset, or a combination of both.

        :param leftOrders: Set of orders with the same maker / taker asset.
        :param leftSignatures: Proof that left orders were created by the left
            makers.
        :param rightOrders: Set of orders to match against `leftOrders`
        :param rightSignatures: Proof that right orders were created by the
            right makers.
        :param tx_params: transaction parameters
        """
        (
            left_orders,
            right_orders,
            left_signatures,
            right_signatures,
        ) = self.validate_and_normalize_inputs(
            left_orders, right_orders, left_signatures, right_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_orders, right_orders, left_signatures, right_signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            left_orders,
            right_orders,
            left_signatures,
            right_signatures,
        ) = self.validate_and_normalize_inputs(
            left_orders, right_orders, left_signatures, right_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_orders, right_orders, left_signatures, right_signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        left_orders: List[LibOrderOrder],
        right_orders: List[LibOrderOrder],
        left_signatures: List[Union[bytes, str]],
        right_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            left_orders,
            right_orders,
            left_signatures,
            right_signatures,
        ) = self.validate_and_normalize_inputs(
            left_orders, right_orders, left_signatures, right_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_orders, right_orders, left_signatures, right_signatures
        ).estimateGas(tx_params.as_dict())


class CancelOrderMethod(ContractMethod):
    """Various interfaces to the cancelOrder method."""

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

    def validate_and_normalize_inputs(self, order: LibOrderOrder):
        """Validate the inputs to the cancelOrder method."""
        self.validator.assert_valid(
            method_name="cancelOrder",
            parameter_name="order",
            argument_value=order,
        )
        return order

    def call(
        self, order: LibOrderOrder, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        After calling, the order can not be filled anymore.

        :param order: Order struct containing order specifications.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(order).call(tx_params.as_dict())

    def send_transaction(
        self, order: LibOrderOrder, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        After calling, the order can not be filled anymore.

        :param order: Order struct containing order specifications.
        :param tx_params: transaction parameters
        """
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order).transact(tx_params.as_dict())

    def build_transaction(
        self, order: LibOrderOrder, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, order: LibOrderOrder, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order).estimateGas(tx_params.as_dict())


class CancelOrdersUpToMethod(ContractMethod):
    """Various interfaces to the cancelOrdersUpTo method."""

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

    def validate_and_normalize_inputs(self, target_order_epoch: int):
        """Validate the inputs to the cancelOrdersUpTo method."""
        self.validator.assert_valid(
            method_name="cancelOrdersUpTo",
            parameter_name="targetOrderEpoch",
            argument_value=target_order_epoch,
        )
        # safeguard against fractional inputs
        target_order_epoch = int(target_order_epoch)
        return target_order_epoch

    def call(
        self, target_order_epoch: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Cancels all orders created by makerAddress with a salt less than or
        equal to the targetOrderEpoch and senderAddress equal to msg.sender (or
        null address if msg.sender == makerAddress).

        :param targetOrderEpoch: Orders created with a salt less or equal to
            this value will be cancelled.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (target_order_epoch) = self.validate_and_normalize_inputs(
            target_order_epoch
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(target_order_epoch).call(tx_params.as_dict())

    def send_transaction(
        self, target_order_epoch: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Cancels all orders created by makerAddress with a salt less than or
        equal to the targetOrderEpoch and senderAddress equal to msg.sender (or
        null address if msg.sender == makerAddress).

        :param targetOrderEpoch: Orders created with a salt less or equal to
            this value will be cancelled.
        :param tx_params: transaction parameters
        """
        (target_order_epoch) = self.validate_and_normalize_inputs(
            target_order_epoch
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target_order_epoch).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, target_order_epoch: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (target_order_epoch) = self.validate_and_normalize_inputs(
            target_order_epoch
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target_order_epoch).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, target_order_epoch: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (target_order_epoch) = self.validate_and_normalize_inputs(
            target_order_epoch
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target_order_epoch).estimateGas(
            tx_params.as_dict()
        )


class CancelledMethod(ContractMethod):
    """Various interfaces to the cancelled method."""

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

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str]):
        """Validate the inputs to the cancelled method."""
        self.validator.assert_valid(
            method_name="cancelled",
            parameter_name="index_0",
            argument_value=index_0,
        )
        return index_0

    def call(
        self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class CurrentContextAddressMethod(ContractMethod):
    """Various interfaces to the currentContextAddress method."""

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


class ExecuteTransactionMethod(ContractMethod):
    """Various interfaces to the executeTransaction method."""

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
        transaction: LibZeroExTransactionZeroExTransaction,
        signature: Union[bytes, str],
    ):
        """Validate the inputs to the executeTransaction method."""
        self.validator.assert_valid(
            method_name="executeTransaction",
            parameter_name="transaction",
            argument_value=transaction,
        )
        self.validator.assert_valid(
            method_name="executeTransaction",
            parameter_name="signature",
            argument_value=signature,
        )
        return (transaction, signature)

    def call(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Executes an Exchange method call in the context of signer.

        :param signature: Proof that transaction has been signed by signer.
        :param transaction: 0x transaction structure.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (transaction, signature) = self.validate_and_normalize_inputs(
            transaction, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(transaction, signature).call(
            tx_params.as_dict()
        )
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes an Exchange method call in the context of signer.

        :param signature: Proof that transaction has been signed by signer.
        :param transaction: 0x transaction structure.
        :param tx_params: transaction parameters
        """
        (transaction, signature) = self.validate_and_normalize_inputs(
            transaction, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction, signature).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (transaction, signature) = self.validate_and_normalize_inputs(
            transaction, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            transaction, signature
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction, signature) = self.validate_and_normalize_inputs(
            transaction, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction, signature).estimateGas(
            tx_params.as_dict()
        )


class FillOrKillOrderMethod(ContractMethod):
    """Various interfaces to the fillOrKillOrder method."""

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
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
    ):
        """Validate the inputs to the fillOrKillOrder method."""
        self.validator.assert_valid(
            method_name="fillOrKillOrder",
            parameter_name="order",
            argument_value=order,
        )
        self.validator.assert_valid(
            method_name="fillOrKillOrder",
            parameter_name="takerAssetFillAmount",
            argument_value=taker_asset_fill_amount,
        )
        # safeguard against fractional inputs
        taker_asset_fill_amount = int(taker_asset_fill_amount)
        self.validator.assert_valid(
            method_name="fillOrKillOrder",
            parameter_name="signature",
            argument_value=signature,
        )
        return (order, taker_asset_fill_amount, signature)

    def call(
        self,
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsFillResults:
        """Execute underlying contract method via eth_call.

        Fills the input order. Reverts if exact takerAssetFillAmount not
        filled.

        :param order: Order struct containing order specifications.
        :param signature: Proof that order has been created by maker.
        :param takerAssetFillAmount: Desired amount of takerAsset to sell.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            order,
            taker_asset_fill_amount,
            signature,
        ) = self.validate_and_normalize_inputs(
            order, taker_asset_fill_amount, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            order, taker_asset_fill_amount, signature
        ).call(tx_params.as_dict())
        return LibFillResultsFillResults(
            makerAssetFilledAmount=returned[0],
            takerAssetFilledAmount=returned[1],
            makerFeePaid=returned[2],
            takerFeePaid=returned[3],
            protocolFeePaid=returned[4],
        )

    def send_transaction(
        self,
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Fills the input order. Reverts if exact takerAssetFillAmount not
        filled.

        :param order: Order struct containing order specifications.
        :param signature: Proof that order has been created by maker.
        :param takerAssetFillAmount: Desired amount of takerAsset to sell.
        :param tx_params: transaction parameters
        """
        (
            order,
            taker_asset_fill_amount,
            signature,
        ) = self.validate_and_normalize_inputs(
            order, taker_asset_fill_amount, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_asset_fill_amount, signature
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            order,
            taker_asset_fill_amount,
            signature,
        ) = self.validate_and_normalize_inputs(
            order, taker_asset_fill_amount, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_asset_fill_amount, signature
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            order,
            taker_asset_fill_amount,
            signature,
        ) = self.validate_and_normalize_inputs(
            order, taker_asset_fill_amount, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_asset_fill_amount, signature
        ).estimateGas(tx_params.as_dict())


class FillOrderMethod(ContractMethod):
    """Various interfaces to the fillOrder method."""

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
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
    ):
        """Validate the inputs to the fillOrder method."""
        self.validator.assert_valid(
            method_name="fillOrder",
            parameter_name="order",
            argument_value=order,
        )
        self.validator.assert_valid(
            method_name="fillOrder",
            parameter_name="takerAssetFillAmount",
            argument_value=taker_asset_fill_amount,
        )
        # safeguard against fractional inputs
        taker_asset_fill_amount = int(taker_asset_fill_amount)
        self.validator.assert_valid(
            method_name="fillOrder",
            parameter_name="signature",
            argument_value=signature,
        )
        return (order, taker_asset_fill_amount, signature)

    def call(
        self,
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsFillResults:
        """Execute underlying contract method via eth_call.

        Fills the input order.

        :param order: Order struct containing order specifications.
        :param signature: Proof that order has been created by maker.
        :param takerAssetFillAmount: Desired amount of takerAsset to sell.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            order,
            taker_asset_fill_amount,
            signature,
        ) = self.validate_and_normalize_inputs(
            order, taker_asset_fill_amount, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            order, taker_asset_fill_amount, signature
        ).call(tx_params.as_dict())
        return LibFillResultsFillResults(
            makerAssetFilledAmount=returned[0],
            takerAssetFilledAmount=returned[1],
            makerFeePaid=returned[2],
            takerFeePaid=returned[3],
            protocolFeePaid=returned[4],
        )

    def send_transaction(
        self,
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Fills the input order.

        :param order: Order struct containing order specifications.
        :param signature: Proof that order has been created by maker.
        :param takerAssetFillAmount: Desired amount of takerAsset to sell.
        :param tx_params: transaction parameters
        """
        (
            order,
            taker_asset_fill_amount,
            signature,
        ) = self.validate_and_normalize_inputs(
            order, taker_asset_fill_amount, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_asset_fill_amount, signature
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            order,
            taker_asset_fill_amount,
            signature,
        ) = self.validate_and_normalize_inputs(
            order, taker_asset_fill_amount, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_asset_fill_amount, signature
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        order: LibOrderOrder,
        taker_asset_fill_amount: int,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            order,
            taker_asset_fill_amount,
            signature,
        ) = self.validate_and_normalize_inputs(
            order, taker_asset_fill_amount, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_asset_fill_amount, signature
        ).estimateGas(tx_params.as_dict())


class FilledMethod(ContractMethod):
    """Various interfaces to the filled method."""

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

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str]):
        """Validate the inputs to the filled method."""
        self.validator.assert_valid(
            method_name="filled",
            parameter_name="index_0",
            argument_value=index_0,
        )
        return index_0

    def call(
        self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class GetAssetProxyMethod(ContractMethod):
    """Various interfaces to the getAssetProxy method."""

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

    def validate_and_normalize_inputs(self, asset_proxy_id: Union[bytes, str]):
        """Validate the inputs to the getAssetProxy method."""
        self.validator.assert_valid(
            method_name="getAssetProxy",
            parameter_name="assetProxyId",
            argument_value=asset_proxy_id,
        )
        return asset_proxy_id

    def call(
        self,
        asset_proxy_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        Gets an asset proxy.

        :param assetProxyId: Id of the asset proxy.
        :param tx_params: transaction parameters
        :returns: The asset proxy registered to assetProxyId. Returns 0x0 if no
            proxy is registered.
        """
        (asset_proxy_id) = self.validate_and_normalize_inputs(asset_proxy_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_proxy_id).call(
            tx_params.as_dict()
        )
        return str(returned)

    def estimate_gas(
        self,
        asset_proxy_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (asset_proxy_id) = self.validate_and_normalize_inputs(asset_proxy_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_proxy_id).estimateGas(
            tx_params.as_dict()
        )


class GetOrderInfoMethod(ContractMethod):
    """Various interfaces to the getOrderInfo method."""

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

    def validate_and_normalize_inputs(self, order: LibOrderOrder):
        """Validate the inputs to the getOrderInfo method."""
        self.validator.assert_valid(
            method_name="getOrderInfo",
            parameter_name="order",
            argument_value=order,
        )
        return order

    def call(
        self, order: LibOrderOrder, tx_params: Optional[TxParams] = None
    ) -> LibOrderOrderInfo:
        """Execute underlying contract method via eth_call.

        Gets information about an order: status, hash, and amount filled.

        :param order: Order to gather information on.
        :param tx_params: transaction parameters
        :returns: OrderInfo Information about the order and its state. See
            LibOrder.OrderInfo for a complete description.
        """
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(order).call(tx_params.as_dict())
        return LibOrderOrderInfo(
            orderStatus=returned[0],
            orderHash=returned[1],
            orderTakerAssetFilledAmount=returned[2],
        )

    def estimate_gas(
        self, order: LibOrderOrder, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (order) = self.validate_and_normalize_inputs(order)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order).estimateGas(tx_params.as_dict())


class IsValidHashSignatureMethod(ContractMethod):
    """Various interfaces to the isValidHashSignature method."""

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
        _hash: Union[bytes, str],
        signer_address: str,
        signature: Union[bytes, str],
    ):
        """Validate the inputs to the isValidHashSignature method."""
        self.validator.assert_valid(
            method_name="isValidHashSignature",
            parameter_name="hash",
            argument_value=_hash,
        )
        self.validator.assert_valid(
            method_name="isValidHashSignature",
            parameter_name="signerAddress",
            argument_value=signer_address,
        )
        signer_address = self.validate_and_checksum_address(signer_address)
        self.validator.assert_valid(
            method_name="isValidHashSignature",
            parameter_name="signature",
            argument_value=signature,
        )
        return (_hash, signer_address, signature)

    def call(
        self,
        _hash: Union[bytes, str],
        signer_address: str,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        Verifies that a hash has been signed by the given signer.

        :param hash: Any 32-byte hash.
        :param signature: Proof that the hash has been signed by signer.
        :param signerAddress: Address that should have signed the given hash.
        :param tx_params: transaction parameters
        :returns: isValid `true` if the signature is valid for the given hash
            and signer.
        """
        (
            _hash,
            signer_address,
            signature,
        ) = self.validate_and_normalize_inputs(
            _hash, signer_address, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            _hash, signer_address, signature
        ).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self,
        _hash: Union[bytes, str],
        signer_address: str,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            _hash,
            signer_address,
            signature,
        ) = self.validate_and_normalize_inputs(
            _hash, signer_address, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _hash, signer_address, signature
        ).estimateGas(tx_params.as_dict())


class IsValidOrderSignatureMethod(ContractMethod):
    """Various interfaces to the isValidOrderSignature method."""

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
        self, order: LibOrderOrder, signature: Union[bytes, str]
    ):
        """Validate the inputs to the isValidOrderSignature method."""
        self.validator.assert_valid(
            method_name="isValidOrderSignature",
            parameter_name="order",
            argument_value=order,
        )
        self.validator.assert_valid(
            method_name="isValidOrderSignature",
            parameter_name="signature",
            argument_value=signature,
        )
        return (order, signature)

    def call(
        self,
        order: LibOrderOrder,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        Verifies that a signature for an order is valid.

        :param order: The order.
        :param signature: Proof that the order has been signed by signer.
        :param tx_params: transaction parameters
        :returns: isValid `true` if the signature is valid for the given order
            and signer.
        """
        (order, signature) = self.validate_and_normalize_inputs(
            order, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(order, signature).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def estimate_gas(
        self,
        order: LibOrderOrder,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (order, signature) = self.validate_and_normalize_inputs(
            order, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order, signature).estimateGas(
            tx_params.as_dict()
        )


class IsValidTransactionSignatureMethod(ContractMethod):
    """Various interfaces to the isValidTransactionSignature method."""

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
        transaction: LibZeroExTransactionZeroExTransaction,
        signature: Union[bytes, str],
    ):
        """Validate the inputs to the isValidTransactionSignature method."""
        self.validator.assert_valid(
            method_name="isValidTransactionSignature",
            parameter_name="transaction",
            argument_value=transaction,
        )
        self.validator.assert_valid(
            method_name="isValidTransactionSignature",
            parameter_name="signature",
            argument_value=signature,
        )
        return (transaction, signature)

    def call(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        Verifies that a signature for a transaction is valid.

        :param signature: Proof that the order has been signed by signer.
        :param transaction: The transaction.
        :param tx_params: transaction parameters
        :returns: isValid `true` if the signature is valid for the given
            transaction and signer.
        """
        (transaction, signature) = self.validate_and_normalize_inputs(
            transaction, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(transaction, signature).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def estimate_gas(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction, signature) = self.validate_and_normalize_inputs(
            transaction, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction, signature).estimateGas(
            tx_params.as_dict()
        )


class MarketBuyOrdersFillOrKillMethod(ContractMethod):
    """Various interfaces to the marketBuyOrdersFillOrKill method."""

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
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the marketBuyOrdersFillOrKill method."""
        self.validator.assert_valid(
            method_name="marketBuyOrdersFillOrKill",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="marketBuyOrdersFillOrKill",
            parameter_name="makerAssetFillAmount",
            argument_value=maker_asset_fill_amount,
        )
        # safeguard against fractional inputs
        maker_asset_fill_amount = int(maker_asset_fill_amount)
        self.validator.assert_valid(
            method_name="marketBuyOrdersFillOrKill",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (orders, maker_asset_fill_amount, signatures)

    def call(
        self,
        orders: List[LibOrderOrder],
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsFillResults:
        """Execute underlying contract method via eth_call.

        Calls marketBuyOrdersNoThrow then reverts if < makerAssetFillAmount has
        been bought. NOTE: This function does not enforce that the makerAsset
        is the same for each order.

        :param makerAssetFillAmount: Minimum amount of makerAsset to buy.
        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been signed by makers.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            maker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, maker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, maker_asset_fill_amount, signatures
        ).call(tx_params.as_dict())
        return LibFillResultsFillResults(
            makerAssetFilledAmount=returned[0],
            takerAssetFilledAmount=returned[1],
            makerFeePaid=returned[2],
            takerFeePaid=returned[3],
            protocolFeePaid=returned[4],
        )

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Calls marketBuyOrdersNoThrow then reverts if < makerAssetFillAmount has
        been bought. NOTE: This function does not enforce that the makerAsset
        is the same for each order.

        :param makerAssetFillAmount: Minimum amount of makerAsset to buy.
        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been signed by makers.
        :param tx_params: transaction parameters
        """
        (
            orders,
            maker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, maker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, maker_asset_fill_amount, signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            maker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, maker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, maker_asset_fill_amount, signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            maker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, maker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, maker_asset_fill_amount, signatures
        ).estimateGas(tx_params.as_dict())


class MarketBuyOrdersNoThrowMethod(ContractMethod):
    """Various interfaces to the marketBuyOrdersNoThrow method."""

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
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the marketBuyOrdersNoThrow method."""
        self.validator.assert_valid(
            method_name="marketBuyOrdersNoThrow",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="marketBuyOrdersNoThrow",
            parameter_name="makerAssetFillAmount",
            argument_value=maker_asset_fill_amount,
        )
        # safeguard against fractional inputs
        maker_asset_fill_amount = int(maker_asset_fill_amount)
        self.validator.assert_valid(
            method_name="marketBuyOrdersNoThrow",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (orders, maker_asset_fill_amount, signatures)

    def call(
        self,
        orders: List[LibOrderOrder],
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsFillResults:
        """Execute underlying contract method via eth_call.

        Executes multiple calls of fillOrder until total amount of makerAsset
        is bought by taker. If any fill reverts, the error is caught and
        ignored. NOTE: This function does not enforce that the makerAsset is
        the same for each order.

        :param makerAssetFillAmount: Desired amount of makerAsset to buy.
        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been signed by makers.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            maker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, maker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, maker_asset_fill_amount, signatures
        ).call(tx_params.as_dict())
        return LibFillResultsFillResults(
            makerAssetFilledAmount=returned[0],
            takerAssetFilledAmount=returned[1],
            makerFeePaid=returned[2],
            takerFeePaid=returned[3],
            protocolFeePaid=returned[4],
        )

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes multiple calls of fillOrder until total amount of makerAsset
        is bought by taker. If any fill reverts, the error is caught and
        ignored. NOTE: This function does not enforce that the makerAsset is
        the same for each order.

        :param makerAssetFillAmount: Desired amount of makerAsset to buy.
        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been signed by makers.
        :param tx_params: transaction parameters
        """
        (
            orders,
            maker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, maker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, maker_asset_fill_amount, signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            maker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, maker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, maker_asset_fill_amount, signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        maker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            maker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, maker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, maker_asset_fill_amount, signatures
        ).estimateGas(tx_params.as_dict())


class MarketSellOrdersFillOrKillMethod(ContractMethod):
    """Various interfaces to the marketSellOrdersFillOrKill method."""

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
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the marketSellOrdersFillOrKill method."""
        self.validator.assert_valid(
            method_name="marketSellOrdersFillOrKill",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="marketSellOrdersFillOrKill",
            parameter_name="takerAssetFillAmount",
            argument_value=taker_asset_fill_amount,
        )
        # safeguard against fractional inputs
        taker_asset_fill_amount = int(taker_asset_fill_amount)
        self.validator.assert_valid(
            method_name="marketSellOrdersFillOrKill",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (orders, taker_asset_fill_amount, signatures)

    def call(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsFillResults:
        """Execute underlying contract method via eth_call.

        Calls marketSellOrdersNoThrow then reverts if < takerAssetFillAmount
        has been sold. NOTE: This function does not enforce that the takerAsset
        is the same for each order.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been signed by makers.
        :param takerAssetFillAmount: Minimum amount of takerAsset to sell.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            taker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, taker_asset_fill_amount, signatures
        ).call(tx_params.as_dict())
        return LibFillResultsFillResults(
            makerAssetFilledAmount=returned[0],
            takerAssetFilledAmount=returned[1],
            makerFeePaid=returned[2],
            takerFeePaid=returned[3],
            protocolFeePaid=returned[4],
        )

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Calls marketSellOrdersNoThrow then reverts if < takerAssetFillAmount
        has been sold. NOTE: This function does not enforce that the takerAsset
        is the same for each order.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been signed by makers.
        :param takerAssetFillAmount: Minimum amount of takerAsset to sell.
        :param tx_params: transaction parameters
        """
        (
            orders,
            taker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amount, signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            taker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amount, signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            taker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amount, signatures
        ).estimateGas(tx_params.as_dict())


class MarketSellOrdersNoThrowMethod(ContractMethod):
    """Various interfaces to the marketSellOrdersNoThrow method."""

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
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the marketSellOrdersNoThrow method."""
        self.validator.assert_valid(
            method_name="marketSellOrdersNoThrow",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="marketSellOrdersNoThrow",
            parameter_name="takerAssetFillAmount",
            argument_value=taker_asset_fill_amount,
        )
        # safeguard against fractional inputs
        taker_asset_fill_amount = int(taker_asset_fill_amount)
        self.validator.assert_valid(
            method_name="marketSellOrdersNoThrow",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (orders, taker_asset_fill_amount, signatures)

    def call(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsFillResults:
        """Execute underlying contract method via eth_call.

        Executes multiple calls of fillOrder until total amount of takerAsset
        is sold by taker. If any fill reverts, the error is caught and ignored.
        NOTE: This function does not enforce that the takerAsset is the same
        for each order.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been signed by makers.
        :param takerAssetFillAmount: Desired amount of takerAsset to sell.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            taker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, taker_asset_fill_amount, signatures
        ).call(tx_params.as_dict())
        return LibFillResultsFillResults(
            makerAssetFilledAmount=returned[0],
            takerAssetFilledAmount=returned[1],
            makerFeePaid=returned[2],
            takerFeePaid=returned[3],
            protocolFeePaid=returned[4],
        )

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes multiple calls of fillOrder until total amount of takerAsset
        is sold by taker. If any fill reverts, the error is caught and ignored.
        NOTE: This function does not enforce that the takerAsset is the same
        for each order.

        :param orders: Array of order specifications.
        :param signatures: Proofs that orders have been signed by makers.
        :param takerAssetFillAmount: Desired amount of takerAsset to sell.
        :param tx_params: transaction parameters
        """
        (
            orders,
            taker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amount, signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            taker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amount, signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        taker_asset_fill_amount: int,
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            taker_asset_fill_amount,
            signatures,
        ) = self.validate_and_normalize_inputs(
            orders, taker_asset_fill_amount, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_asset_fill_amount, signatures
        ).estimateGas(tx_params.as_dict())


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
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
    ):
        """Validate the inputs to the matchOrders method."""
        self.validator.assert_valid(
            method_name="matchOrders",
            parameter_name="leftOrder",
            argument_value=left_order,
        )
        self.validator.assert_valid(
            method_name="matchOrders",
            parameter_name="rightOrder",
            argument_value=right_order,
        )
        self.validator.assert_valid(
            method_name="matchOrders",
            parameter_name="leftSignature",
            argument_value=left_signature,
        )
        self.validator.assert_valid(
            method_name="matchOrders",
            parameter_name="rightSignature",
            argument_value=right_signature,
        )
        return (left_order, right_order, left_signature, right_signature)

    def call(
        self,
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsMatchedFillResults:
        """Execute underlying contract method via eth_call.

        Match two complementary orders that have a profitable spread. Each
        order is filled at their respective price point. However, the
        calculations are carried out as though the orders are both being filled
        at the right order's price point. The profit made by the left order
        goes to the taker (who matched the two orders).

        :param leftOrder: First order to match.
        :param leftSignature: Proof that order was created by the left maker.
        :param rightOrder: Second order to match.
        :param rightSignature: Proof that order was created by the right maker.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            left_order,
            right_order,
            left_signature,
            right_signature,
        ) = self.validate_and_normalize_inputs(
            left_order, right_order, left_signature, right_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            left_order, right_order, left_signature, right_signature
        ).call(tx_params.as_dict())
        return LibFillResultsMatchedFillResults(
            left=returned[0],
            right=returned[1],
            profitInLeftMakerAsset=returned[2],
            profitInRightMakerAsset=returned[3],
        )

    def send_transaction(
        self,
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Match two complementary orders that have a profitable spread. Each
        order is filled at their respective price point. However, the
        calculations are carried out as though the orders are both being filled
        at the right order's price point. The profit made by the left order
        goes to the taker (who matched the two orders).

        :param leftOrder: First order to match.
        :param leftSignature: Proof that order was created by the left maker.
        :param rightOrder: Second order to match.
        :param rightSignature: Proof that order was created by the right maker.
        :param tx_params: transaction parameters
        """
        (
            left_order,
            right_order,
            left_signature,
            right_signature,
        ) = self.validate_and_normalize_inputs(
            left_order, right_order, left_signature, right_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_order, right_order, left_signature, right_signature
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            left_order,
            right_order,
            left_signature,
            right_signature,
        ) = self.validate_and_normalize_inputs(
            left_order, right_order, left_signature, right_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_order, right_order, left_signature, right_signature
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            left_order,
            right_order,
            left_signature,
            right_signature,
        ) = self.validate_and_normalize_inputs(
            left_order, right_order, left_signature, right_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_order, right_order, left_signature, right_signature
        ).estimateGas(tx_params.as_dict())


class MatchOrdersWithMaximalFillMethod(ContractMethod):
    """Various interfaces to the matchOrdersWithMaximalFill method."""

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
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
    ):
        """Validate the inputs to the matchOrdersWithMaximalFill method."""
        self.validator.assert_valid(
            method_name="matchOrdersWithMaximalFill",
            parameter_name="leftOrder",
            argument_value=left_order,
        )
        self.validator.assert_valid(
            method_name="matchOrdersWithMaximalFill",
            parameter_name="rightOrder",
            argument_value=right_order,
        )
        self.validator.assert_valid(
            method_name="matchOrdersWithMaximalFill",
            parameter_name="leftSignature",
            argument_value=left_signature,
        )
        self.validator.assert_valid(
            method_name="matchOrdersWithMaximalFill",
            parameter_name="rightSignature",
            argument_value=right_signature,
        )
        return (left_order, right_order, left_signature, right_signature)

    def call(
        self,
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> LibFillResultsMatchedFillResults:
        """Execute underlying contract method via eth_call.

        Match two complementary orders that have a profitable spread. Each
        order is maximally filled at their respective price point, and the
        matcher receives a profit denominated in either the left maker asset,
        right maker asset, or a combination of both.

        :param leftOrder: First order to match.
        :param leftSignature: Proof that order was created by the left maker.
        :param rightOrder: Second order to match.
        :param rightSignature: Proof that order was created by the right maker.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            left_order,
            right_order,
            left_signature,
            right_signature,
        ) = self.validate_and_normalize_inputs(
            left_order, right_order, left_signature, right_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            left_order, right_order, left_signature, right_signature
        ).call(tx_params.as_dict())
        return LibFillResultsMatchedFillResults(
            left=returned[0],
            right=returned[1],
            profitInLeftMakerAsset=returned[2],
            profitInRightMakerAsset=returned[3],
        )

    def send_transaction(
        self,
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Match two complementary orders that have a profitable spread. Each
        order is maximally filled at their respective price point, and the
        matcher receives a profit denominated in either the left maker asset,
        right maker asset, or a combination of both.

        :param leftOrder: First order to match.
        :param leftSignature: Proof that order was created by the left maker.
        :param rightOrder: Second order to match.
        :param rightSignature: Proof that order was created by the right maker.
        :param tx_params: transaction parameters
        """
        (
            left_order,
            right_order,
            left_signature,
            right_signature,
        ) = self.validate_and_normalize_inputs(
            left_order, right_order, left_signature, right_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_order, right_order, left_signature, right_signature
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            left_order,
            right_order,
            left_signature,
            right_signature,
        ) = self.validate_and_normalize_inputs(
            left_order, right_order, left_signature, right_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_order, right_order, left_signature, right_signature
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        left_order: LibOrderOrder,
        right_order: LibOrderOrder,
        left_signature: Union[bytes, str],
        right_signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            left_order,
            right_order,
            left_signature,
            right_signature,
        ) = self.validate_and_normalize_inputs(
            left_order, right_order, left_signature, right_signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            left_order, right_order, left_signature, right_signature
        ).estimateGas(tx_params.as_dict())


class OrderEpochMethod(ContractMethod):
    """Various interfaces to the orderEpoch method."""

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

    def validate_and_normalize_inputs(self, index_0: str, index_1: str):
        """Validate the inputs to the orderEpoch method."""
        self.validator.assert_valid(
            method_name="orderEpoch",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="orderEpoch",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)

    def call(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


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


class PreSignMethod(ContractMethod):
    """Various interfaces to the preSign method."""

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

    def validate_and_normalize_inputs(self, _hash: Union[bytes, str]):
        """Validate the inputs to the preSign method."""
        self.validator.assert_valid(
            method_name="preSign", parameter_name="hash", argument_value=_hash,
        )
        return _hash

    def call(
        self, _hash: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Approves a hash on-chain. After presigning a hash, the preSign
        signature type will become valid for that hash and signer.

        :param hash: Any 32-byte hash.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_hash) = self.validate_and_normalize_inputs(_hash)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_hash).call(tx_params.as_dict())

    def send_transaction(
        self, _hash: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Approves a hash on-chain. After presigning a hash, the preSign
        signature type will become valid for that hash and signer.

        :param hash: Any 32-byte hash.
        :param tx_params: transaction parameters
        """
        (_hash) = self.validate_and_normalize_inputs(_hash)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_hash).transact(tx_params.as_dict())

    def build_transaction(
        self, _hash: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_hash) = self.validate_and_normalize_inputs(_hash)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_hash).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _hash: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_hash) = self.validate_and_normalize_inputs(_hash)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_hash).estimateGas(tx_params.as_dict())


class PreSignedMethod(ContractMethod):
    """Various interfaces to the preSigned method."""

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
        self, index_0: Union[bytes, str], index_1: str
    ):
        """Validate the inputs to the preSigned method."""
        self.validator.assert_valid(
            method_name="preSigned",
            parameter_name="index_0",
            argument_value=index_0,
        )
        self.validator.assert_valid(
            method_name="preSigned",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)

    def call(
        self,
        index_0: Union[bytes, str],
        index_1: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def estimate_gas(
        self,
        index_0: Union[bytes, str],
        index_1: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class ProtocolFeeCollectorMethod(ContractMethod):
    """Various interfaces to the protocolFeeCollector method."""

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


class ProtocolFeeMultiplierMethod(ContractMethod):
    """Various interfaces to the protocolFeeMultiplier method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class RegisterAssetProxyMethod(ContractMethod):
    """Various interfaces to the registerAssetProxy method."""

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

    def validate_and_normalize_inputs(self, asset_proxy: str):
        """Validate the inputs to the registerAssetProxy method."""
        self.validator.assert_valid(
            method_name="registerAssetProxy",
            parameter_name="assetProxy",
            argument_value=asset_proxy,
        )
        asset_proxy = self.validate_and_checksum_address(asset_proxy)
        return asset_proxy

    def call(
        self, asset_proxy: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Registers an asset proxy to its asset proxy id. Once an asset proxy is
        registered, it cannot be unregistered.

        :param assetProxy: Address of new asset proxy to register.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (asset_proxy) = self.validate_and_normalize_inputs(asset_proxy)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(asset_proxy).call(tx_params.as_dict())

    def send_transaction(
        self, asset_proxy: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Registers an asset proxy to its asset proxy id. Once an asset proxy is
        registered, it cannot be unregistered.

        :param assetProxy: Address of new asset proxy to register.
        :param tx_params: transaction parameters
        """
        (asset_proxy) = self.validate_and_normalize_inputs(asset_proxy)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_proxy).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, asset_proxy: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_proxy) = self.validate_and_normalize_inputs(asset_proxy)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_proxy).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, asset_proxy: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (asset_proxy) = self.validate_and_normalize_inputs(asset_proxy)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_proxy).estimateGas(
            tx_params.as_dict()
        )


class SetProtocolFeeCollectorAddressMethod(ContractMethod):
    """Various interfaces to the setProtocolFeeCollectorAddress method."""

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
        self, updated_protocol_fee_collector: str
    ):
        """Validate the inputs to the setProtocolFeeCollectorAddress method."""
        self.validator.assert_valid(
            method_name="setProtocolFeeCollectorAddress",
            parameter_name="updatedProtocolFeeCollector",
            argument_value=updated_protocol_fee_collector,
        )
        updated_protocol_fee_collector = self.validate_and_checksum_address(
            updated_protocol_fee_collector
        )
        return updated_protocol_fee_collector

    def call(
        self,
        updated_protocol_fee_collector: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Allows the owner to update the protocolFeeCollector address.

        :param updatedProtocolFeeCollector: The updated protocolFeeCollector
            contract address.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (updated_protocol_fee_collector) = self.validate_and_normalize_inputs(
            updated_protocol_fee_collector
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(updated_protocol_fee_collector).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        updated_protocol_fee_collector: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows the owner to update the protocolFeeCollector address.

        :param updatedProtocolFeeCollector: The updated protocolFeeCollector
            contract address.
        :param tx_params: transaction parameters
        """
        (updated_protocol_fee_collector) = self.validate_and_normalize_inputs(
            updated_protocol_fee_collector
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            updated_protocol_fee_collector
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        updated_protocol_fee_collector: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (updated_protocol_fee_collector) = self.validate_and_normalize_inputs(
            updated_protocol_fee_collector
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            updated_protocol_fee_collector
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        updated_protocol_fee_collector: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (updated_protocol_fee_collector) = self.validate_and_normalize_inputs(
            updated_protocol_fee_collector
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            updated_protocol_fee_collector
        ).estimateGas(tx_params.as_dict())


class SetProtocolFeeMultiplierMethod(ContractMethod):
    """Various interfaces to the setProtocolFeeMultiplier method."""

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
        self, updated_protocol_fee_multiplier: int
    ):
        """Validate the inputs to the setProtocolFeeMultiplier method."""
        self.validator.assert_valid(
            method_name="setProtocolFeeMultiplier",
            parameter_name="updatedProtocolFeeMultiplier",
            argument_value=updated_protocol_fee_multiplier,
        )
        # safeguard against fractional inputs
        updated_protocol_fee_multiplier = int(updated_protocol_fee_multiplier)
        return updated_protocol_fee_multiplier

    def call(
        self,
        updated_protocol_fee_multiplier: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Allows the owner to update the protocol fee multiplier.

        :param updatedProtocolFeeMultiplier: The updated protocol fee
            multiplier.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (updated_protocol_fee_multiplier) = self.validate_and_normalize_inputs(
            updated_protocol_fee_multiplier
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(updated_protocol_fee_multiplier).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        updated_protocol_fee_multiplier: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows the owner to update the protocol fee multiplier.

        :param updatedProtocolFeeMultiplier: The updated protocol fee
            multiplier.
        :param tx_params: transaction parameters
        """
        (updated_protocol_fee_multiplier) = self.validate_and_normalize_inputs(
            updated_protocol_fee_multiplier
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            updated_protocol_fee_multiplier
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        updated_protocol_fee_multiplier: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (updated_protocol_fee_multiplier) = self.validate_and_normalize_inputs(
            updated_protocol_fee_multiplier
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            updated_protocol_fee_multiplier
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        updated_protocol_fee_multiplier: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (updated_protocol_fee_multiplier) = self.validate_and_normalize_inputs(
            updated_protocol_fee_multiplier
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            updated_protocol_fee_multiplier
        ).estimateGas(tx_params.as_dict())


class SetSignatureValidatorApprovalMethod(ContractMethod):
    """Various interfaces to the setSignatureValidatorApproval method."""

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
        self, validator_address: str, approval: bool
    ):
        """Validate the inputs to the setSignatureValidatorApproval method."""
        self.validator.assert_valid(
            method_name="setSignatureValidatorApproval",
            parameter_name="validatorAddress",
            argument_value=validator_address,
        )
        validator_address = self.validate_and_checksum_address(
            validator_address
        )
        self.validator.assert_valid(
            method_name="setSignatureValidatorApproval",
            parameter_name="approval",
            argument_value=approval,
        )
        return (validator_address, approval)

    def call(
        self,
        validator_address: str,
        approval: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Approves/unnapproves a Validator contract to verify signatures on
        signer's behalf using the `Validator` signature type.

        :param approval: Approval or disapproval of  Validator contract.
        :param validatorAddress: Address of Validator contract.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (validator_address, approval) = self.validate_and_normalize_inputs(
            validator_address, approval
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(validator_address, approval).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        validator_address: str,
        approval: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Approves/unnapproves a Validator contract to verify signatures on
        signer's behalf using the `Validator` signature type.

        :param approval: Approval or disapproval of  Validator contract.
        :param validatorAddress: Address of Validator contract.
        :param tx_params: transaction parameters
        """
        (validator_address, approval) = self.validate_and_normalize_inputs(
            validator_address, approval
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(validator_address, approval).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        validator_address: str,
        approval: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (validator_address, approval) = self.validate_and_normalize_inputs(
            validator_address, approval
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            validator_address, approval
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        validator_address: str,
        approval: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (validator_address, approval) = self.validate_and_normalize_inputs(
            validator_address, approval
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            validator_address, approval
        ).estimateGas(tx_params.as_dict())


class SimulateDispatchTransferFromCallsMethod(ContractMethod):
    """Various interfaces to the simulateDispatchTransferFromCalls method."""

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
        asset_data: List[Union[bytes, str]],
        from_addresses: List[str],
        to_addresses: List[str],
        amounts: List[int],
    ):
        """Validate the inputs to the simulateDispatchTransferFromCalls method."""
        self.validator.assert_valid(
            method_name="simulateDispatchTransferFromCalls",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        self.validator.assert_valid(
            method_name="simulateDispatchTransferFromCalls",
            parameter_name="fromAddresses",
            argument_value=from_addresses,
        )
        self.validator.assert_valid(
            method_name="simulateDispatchTransferFromCalls",
            parameter_name="toAddresses",
            argument_value=to_addresses,
        )
        self.validator.assert_valid(
            method_name="simulateDispatchTransferFromCalls",
            parameter_name="amounts",
            argument_value=amounts,
        )
        return (asset_data, from_addresses, to_addresses, amounts)

    def call(
        self,
        asset_data: List[Union[bytes, str]],
        from_addresses: List[str],
        to_addresses: List[str],
        amounts: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        This function may be used to simulate any amount of transfers As they
        would occur through the Exchange contract. Note that this function will
        always revert, even if all transfers are successful. However, it may be
        used with eth_call or with a try/catch pattern in order to simulate the
        results of the transfers.

        :param amounts: Array containing the amounts that correspond to each
            transfer.
        :param assetData: Array of asset details, each encoded per the
            AssetProxy contract specification.
        :param fromAddresses: Array containing the `from` addresses that
            correspond with each transfer.
        :param toAddresses: Array containing the `to` addresses that correspond
            with each transfer.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            asset_data,
            from_addresses,
            to_addresses,
            amounts,
        ) = self.validate_and_normalize_inputs(
            asset_data, from_addresses, to_addresses, amounts
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            asset_data, from_addresses, to_addresses, amounts
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        asset_data: List[Union[bytes, str]],
        from_addresses: List[str],
        to_addresses: List[str],
        amounts: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        This function may be used to simulate any amount of transfers As they
        would occur through the Exchange contract. Note that this function will
        always revert, even if all transfers are successful. However, it may be
        used with eth_call or with a try/catch pattern in order to simulate the
        results of the transfers.

        :param amounts: Array containing the amounts that correspond to each
            transfer.
        :param assetData: Array of asset details, each encoded per the
            AssetProxy contract specification.
        :param fromAddresses: Array containing the `from` addresses that
            correspond with each transfer.
        :param toAddresses: Array containing the `to` addresses that correspond
            with each transfer.
        :param tx_params: transaction parameters
        """
        (
            asset_data,
            from_addresses,
            to_addresses,
            amounts,
        ) = self.validate_and_normalize_inputs(
            asset_data, from_addresses, to_addresses, amounts
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_data, from_addresses, to_addresses, amounts
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        asset_data: List[Union[bytes, str]],
        from_addresses: List[str],
        to_addresses: List[str],
        amounts: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            asset_data,
            from_addresses,
            to_addresses,
            amounts,
        ) = self.validate_and_normalize_inputs(
            asset_data, from_addresses, to_addresses, amounts
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_data, from_addresses, to_addresses, amounts
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        asset_data: List[Union[bytes, str]],
        from_addresses: List[str],
        to_addresses: List[str],
        amounts: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            asset_data,
            from_addresses,
            to_addresses,
            amounts,
        ) = self.validate_and_normalize_inputs(
            asset_data, from_addresses, to_addresses, amounts
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_data, from_addresses, to_addresses, amounts
        ).estimateGas(tx_params.as_dict())


class TransactionsExecutedMethod(ContractMethod):
    """Various interfaces to the transactionsExecuted method."""

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

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str]):
        """Validate the inputs to the transactionsExecuted method."""
        self.validator.assert_valid(
            method_name="transactionsExecuted",
            parameter_name="index_0",
            argument_value=index_0,
        )
        return index_0

    def call(
        self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Exchange:
    """Wrapper class for Exchange Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    eip1271_magic_value: Eip1271MagicValueMethod
    """Constructor-initialized instance of
    :class:`Eip1271MagicValueMethod`.
    """

    eip712_exchange_domain_hash: Eip712ExchangeDomainHashMethod
    """Constructor-initialized instance of
    :class:`Eip712ExchangeDomainHashMethod`.
    """

    allowed_validators: AllowedValidatorsMethod
    """Constructor-initialized instance of
    :class:`AllowedValidatorsMethod`.
    """

    batch_cancel_orders: BatchCancelOrdersMethod
    """Constructor-initialized instance of
    :class:`BatchCancelOrdersMethod`.
    """

    batch_execute_transactions: BatchExecuteTransactionsMethod
    """Constructor-initialized instance of
    :class:`BatchExecuteTransactionsMethod`.
    """

    batch_fill_or_kill_orders: BatchFillOrKillOrdersMethod
    """Constructor-initialized instance of
    :class:`BatchFillOrKillOrdersMethod`.
    """

    batch_fill_orders: BatchFillOrdersMethod
    """Constructor-initialized instance of
    :class:`BatchFillOrdersMethod`.
    """

    batch_fill_orders_no_throw: BatchFillOrdersNoThrowMethod
    """Constructor-initialized instance of
    :class:`BatchFillOrdersNoThrowMethod`.
    """

    batch_match_orders: BatchMatchOrdersMethod
    """Constructor-initialized instance of
    :class:`BatchMatchOrdersMethod`.
    """

    batch_match_orders_with_maximal_fill: BatchMatchOrdersWithMaximalFillMethod
    """Constructor-initialized instance of
    :class:`BatchMatchOrdersWithMaximalFillMethod`.
    """

    cancel_order: CancelOrderMethod
    """Constructor-initialized instance of
    :class:`CancelOrderMethod`.
    """

    cancel_orders_up_to: CancelOrdersUpToMethod
    """Constructor-initialized instance of
    :class:`CancelOrdersUpToMethod`.
    """

    cancelled: CancelledMethod
    """Constructor-initialized instance of
    :class:`CancelledMethod`.
    """

    current_context_address: CurrentContextAddressMethod
    """Constructor-initialized instance of
    :class:`CurrentContextAddressMethod`.
    """

    execute_transaction: ExecuteTransactionMethod
    """Constructor-initialized instance of
    :class:`ExecuteTransactionMethod`.
    """

    fill_or_kill_order: FillOrKillOrderMethod
    """Constructor-initialized instance of
    :class:`FillOrKillOrderMethod`.
    """

    fill_order: FillOrderMethod
    """Constructor-initialized instance of
    :class:`FillOrderMethod`.
    """

    filled: FilledMethod
    """Constructor-initialized instance of
    :class:`FilledMethod`.
    """

    get_asset_proxy: GetAssetProxyMethod
    """Constructor-initialized instance of
    :class:`GetAssetProxyMethod`.
    """

    get_order_info: GetOrderInfoMethod
    """Constructor-initialized instance of
    :class:`GetOrderInfoMethod`.
    """

    is_valid_hash_signature: IsValidHashSignatureMethod
    """Constructor-initialized instance of
    :class:`IsValidHashSignatureMethod`.
    """

    is_valid_order_signature: IsValidOrderSignatureMethod
    """Constructor-initialized instance of
    :class:`IsValidOrderSignatureMethod`.
    """

    is_valid_transaction_signature: IsValidTransactionSignatureMethod
    """Constructor-initialized instance of
    :class:`IsValidTransactionSignatureMethod`.
    """

    market_buy_orders_fill_or_kill: MarketBuyOrdersFillOrKillMethod
    """Constructor-initialized instance of
    :class:`MarketBuyOrdersFillOrKillMethod`.
    """

    market_buy_orders_no_throw: MarketBuyOrdersNoThrowMethod
    """Constructor-initialized instance of
    :class:`MarketBuyOrdersNoThrowMethod`.
    """

    market_sell_orders_fill_or_kill: MarketSellOrdersFillOrKillMethod
    """Constructor-initialized instance of
    :class:`MarketSellOrdersFillOrKillMethod`.
    """

    market_sell_orders_no_throw: MarketSellOrdersNoThrowMethod
    """Constructor-initialized instance of
    :class:`MarketSellOrdersNoThrowMethod`.
    """

    match_orders: MatchOrdersMethod
    """Constructor-initialized instance of
    :class:`MatchOrdersMethod`.
    """

    match_orders_with_maximal_fill: MatchOrdersWithMaximalFillMethod
    """Constructor-initialized instance of
    :class:`MatchOrdersWithMaximalFillMethod`.
    """

    order_epoch: OrderEpochMethod
    """Constructor-initialized instance of
    :class:`OrderEpochMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    pre_sign: PreSignMethod
    """Constructor-initialized instance of
    :class:`PreSignMethod`.
    """

    pre_signed: PreSignedMethod
    """Constructor-initialized instance of
    :class:`PreSignedMethod`.
    """

    protocol_fee_collector: ProtocolFeeCollectorMethod
    """Constructor-initialized instance of
    :class:`ProtocolFeeCollectorMethod`.
    """

    protocol_fee_multiplier: ProtocolFeeMultiplierMethod
    """Constructor-initialized instance of
    :class:`ProtocolFeeMultiplierMethod`.
    """

    register_asset_proxy: RegisterAssetProxyMethod
    """Constructor-initialized instance of
    :class:`RegisterAssetProxyMethod`.
    """

    set_protocol_fee_collector_address: SetProtocolFeeCollectorAddressMethod
    """Constructor-initialized instance of
    :class:`SetProtocolFeeCollectorAddressMethod`.
    """

    set_protocol_fee_multiplier: SetProtocolFeeMultiplierMethod
    """Constructor-initialized instance of
    :class:`SetProtocolFeeMultiplierMethod`.
    """

    set_signature_validator_approval: SetSignatureValidatorApprovalMethod
    """Constructor-initialized instance of
    :class:`SetSignatureValidatorApprovalMethod`.
    """

    simulate_dispatch_transfer_from_calls: SimulateDispatchTransferFromCallsMethod
    """Constructor-initialized instance of
    :class:`SimulateDispatchTransferFromCallsMethod`.
    """

    transactions_executed: TransactionsExecutedMethod
    """Constructor-initialized instance of
    :class:`TransactionsExecutedMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ExchangeValidator = None,
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
            validator = ExchangeValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=Exchange.abi()
        ).functions

        self.eip1271_magic_value = Eip1271MagicValueMethod(
            web3_or_provider, contract_address, functions.EIP1271_MAGIC_VALUE
        )

        self.eip712_exchange_domain_hash = Eip712ExchangeDomainHashMethod(
            web3_or_provider,
            contract_address,
            functions.EIP712_EXCHANGE_DOMAIN_HASH,
        )

        self.allowed_validators = AllowedValidatorsMethod(
            web3_or_provider,
            contract_address,
            functions.allowedValidators,
            validator,
        )

        self.batch_cancel_orders = BatchCancelOrdersMethod(
            web3_or_provider,
            contract_address,
            functions.batchCancelOrders,
            validator,
        )

        self.batch_execute_transactions = BatchExecuteTransactionsMethod(
            web3_or_provider,
            contract_address,
            functions.batchExecuteTransactions,
            validator,
        )

        self.batch_fill_or_kill_orders = BatchFillOrKillOrdersMethod(
            web3_or_provider,
            contract_address,
            functions.batchFillOrKillOrders,
            validator,
        )

        self.batch_fill_orders = BatchFillOrdersMethod(
            web3_or_provider,
            contract_address,
            functions.batchFillOrders,
            validator,
        )

        self.batch_fill_orders_no_throw = BatchFillOrdersNoThrowMethod(
            web3_or_provider,
            contract_address,
            functions.batchFillOrdersNoThrow,
            validator,
        )

        self.batch_match_orders = BatchMatchOrdersMethod(
            web3_or_provider,
            contract_address,
            functions.batchMatchOrders,
            validator,
        )

        self.batch_match_orders_with_maximal_fill = BatchMatchOrdersWithMaximalFillMethod(
            web3_or_provider,
            contract_address,
            functions.batchMatchOrdersWithMaximalFill,
            validator,
        )

        self.cancel_order = CancelOrderMethod(
            web3_or_provider,
            contract_address,
            functions.cancelOrder,
            validator,
        )

        self.cancel_orders_up_to = CancelOrdersUpToMethod(
            web3_or_provider,
            contract_address,
            functions.cancelOrdersUpTo,
            validator,
        )

        self.cancelled = CancelledMethod(
            web3_or_provider, contract_address, functions.cancelled, validator
        )

        self.current_context_address = CurrentContextAddressMethod(
            web3_or_provider, contract_address, functions.currentContextAddress
        )

        self.execute_transaction = ExecuteTransactionMethod(
            web3_or_provider,
            contract_address,
            functions.executeTransaction,
            validator,
        )

        self.fill_or_kill_order = FillOrKillOrderMethod(
            web3_or_provider,
            contract_address,
            functions.fillOrKillOrder,
            validator,
        )

        self.fill_order = FillOrderMethod(
            web3_or_provider, contract_address, functions.fillOrder, validator
        )

        self.filled = FilledMethod(
            web3_or_provider, contract_address, functions.filled, validator
        )

        self.get_asset_proxy = GetAssetProxyMethod(
            web3_or_provider,
            contract_address,
            functions.getAssetProxy,
            validator,
        )

        self.get_order_info = GetOrderInfoMethod(
            web3_or_provider,
            contract_address,
            functions.getOrderInfo,
            validator,
        )

        self.is_valid_hash_signature = IsValidHashSignatureMethod(
            web3_or_provider,
            contract_address,
            functions.isValidHashSignature,
            validator,
        )

        self.is_valid_order_signature = IsValidOrderSignatureMethod(
            web3_or_provider,
            contract_address,
            functions.isValidOrderSignature,
            validator,
        )

        self.is_valid_transaction_signature = IsValidTransactionSignatureMethod(
            web3_or_provider,
            contract_address,
            functions.isValidTransactionSignature,
            validator,
        )

        self.market_buy_orders_fill_or_kill = MarketBuyOrdersFillOrKillMethod(
            web3_or_provider,
            contract_address,
            functions.marketBuyOrdersFillOrKill,
            validator,
        )

        self.market_buy_orders_no_throw = MarketBuyOrdersNoThrowMethod(
            web3_or_provider,
            contract_address,
            functions.marketBuyOrdersNoThrow,
            validator,
        )

        self.market_sell_orders_fill_or_kill = MarketSellOrdersFillOrKillMethod(
            web3_or_provider,
            contract_address,
            functions.marketSellOrdersFillOrKill,
            validator,
        )

        self.market_sell_orders_no_throw = MarketSellOrdersNoThrowMethod(
            web3_or_provider,
            contract_address,
            functions.marketSellOrdersNoThrow,
            validator,
        )

        self.match_orders = MatchOrdersMethod(
            web3_or_provider,
            contract_address,
            functions.matchOrders,
            validator,
        )

        self.match_orders_with_maximal_fill = MatchOrdersWithMaximalFillMethod(
            web3_or_provider,
            contract_address,
            functions.matchOrdersWithMaximalFill,
            validator,
        )

        self.order_epoch = OrderEpochMethod(
            web3_or_provider, contract_address, functions.orderEpoch, validator
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
        )

        self.pre_sign = PreSignMethod(
            web3_or_provider, contract_address, functions.preSign, validator
        )

        self.pre_signed = PreSignedMethod(
            web3_or_provider, contract_address, functions.preSigned, validator
        )

        self.protocol_fee_collector = ProtocolFeeCollectorMethod(
            web3_or_provider, contract_address, functions.protocolFeeCollector
        )

        self.protocol_fee_multiplier = ProtocolFeeMultiplierMethod(
            web3_or_provider, contract_address, functions.protocolFeeMultiplier
        )

        self.register_asset_proxy = RegisterAssetProxyMethod(
            web3_or_provider,
            contract_address,
            functions.registerAssetProxy,
            validator,
        )

        self.set_protocol_fee_collector_address = SetProtocolFeeCollectorAddressMethod(
            web3_or_provider,
            contract_address,
            functions.setProtocolFeeCollectorAddress,
            validator,
        )

        self.set_protocol_fee_multiplier = SetProtocolFeeMultiplierMethod(
            web3_or_provider,
            contract_address,
            functions.setProtocolFeeMultiplier,
            validator,
        )

        self.set_signature_validator_approval = SetSignatureValidatorApprovalMethod(
            web3_or_provider,
            contract_address,
            functions.setSignatureValidatorApproval,
            validator,
        )

        self.simulate_dispatch_transfer_from_calls = SimulateDispatchTransferFromCallsMethod(
            web3_or_provider,
            contract_address,
            functions.simulateDispatchTransferFromCalls,
            validator,
        )

        self.transactions_executed = TransactionsExecutedMethod(
            web3_or_provider,
            contract_address,
            functions.transactionsExecuted,
            validator,
        )

        self.transfer_ownership = TransferOwnershipMethod(
            web3_or_provider,
            contract_address,
            functions.transferOwnership,
            validator,
        )

    def get_asset_proxy_registered_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AssetProxyRegistered event.

        :param tx_hash: hash of transaction emitting AssetProxyRegistered event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Exchange.abi(),
            )
            .events.AssetProxyRegistered()
            .processReceipt(tx_receipt)
        )

    def get_cancel_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Cancel event.

        :param tx_hash: hash of transaction emitting Cancel event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Exchange.abi(),
            )
            .events.Cancel()
            .processReceipt(tx_receipt)
        )

    def get_cancel_up_to_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for CancelUpTo event.

        :param tx_hash: hash of transaction emitting CancelUpTo event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Exchange.abi(),
            )
            .events.CancelUpTo()
            .processReceipt(tx_receipt)
        )

    def get_fill_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Fill event.

        :param tx_hash: hash of transaction emitting Fill event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Exchange.abi(),
            )
            .events.Fill()
            .processReceipt(tx_receipt)
        )

    def get_protocol_fee_collector_address_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ProtocolFeeCollectorAddress event.

        :param tx_hash: hash of transaction emitting
            ProtocolFeeCollectorAddress event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Exchange.abi(),
            )
            .events.ProtocolFeeCollectorAddress()
            .processReceipt(tx_receipt)
        )

    def get_protocol_fee_multiplier_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ProtocolFeeMultiplier event.

        :param tx_hash: hash of transaction emitting ProtocolFeeMultiplier
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Exchange.abi(),
            )
            .events.ProtocolFeeMultiplier()
            .processReceipt(tx_receipt)
        )

    def get_signature_validator_approval_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for SignatureValidatorApproval event.

        :param tx_hash: hash of transaction emitting SignatureValidatorApproval
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Exchange.abi(),
            )
            .events.SignatureValidatorApproval()
            .processReceipt(tx_receipt)
        )

    def get_transaction_execution_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransactionExecution event.

        :param tx_hash: hash of transaction emitting TransactionExecution event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Exchange.abi(),
            )
            .events.TransactionExecution()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"uint256","name":"chainId","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes4","name":"id","type":"bytes4"},{"indexed":false,"internalType":"address","name":"assetProxy","type":"address"}],"name":"AssetProxyRegistered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"makerAddress","type":"address"},{"indexed":true,"internalType":"address","name":"feeRecipientAddress","type":"address"},{"indexed":false,"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"indexed":false,"internalType":"address","name":"senderAddress","type":"address"},{"indexed":true,"internalType":"bytes32","name":"orderHash","type":"bytes32"}],"name":"Cancel","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"makerAddress","type":"address"},{"indexed":true,"internalType":"address","name":"orderSenderAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"orderEpoch","type":"uint256"}],"name":"CancelUpTo","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"makerAddress","type":"address"},{"indexed":true,"internalType":"address","name":"feeRecipientAddress","type":"address"},{"indexed":false,"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"},{"indexed":true,"internalType":"bytes32","name":"orderHash","type":"bytes32"},{"indexed":false,"internalType":"address","name":"takerAddress","type":"address"},{"indexed":false,"internalType":"address","name":"senderAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"name":"Fill","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldProtocolFeeCollector","type":"address"},{"indexed":false,"internalType":"address","name":"updatedProtocolFeeCollector","type":"address"}],"name":"ProtocolFeeCollectorAddress","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldProtocolFeeMultiplier","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"updatedProtocolFeeMultiplier","type":"uint256"}],"name":"ProtocolFeeMultiplier","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"signerAddress","type":"address"},{"indexed":true,"internalType":"address","name":"validatorAddress","type":"address"},{"indexed":false,"internalType":"bool","name":"isApproved","type":"bool"}],"name":"SignatureValidatorApproval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"transactionHash","type":"bytes32"}],"name":"TransactionExecution","type":"event"},{"constant":true,"inputs":[],"name":"EIP1271_MAGIC_VALUE","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"EIP712_EXCHANGE_DOMAIN_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"}],"name":"allowedValidators","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"}],"name":"batchCancelOrders","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct LibZeroExTransaction.ZeroExTransaction[]","name":"transactions","type":"tuple[]"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"batchExecuteTransactions","outputs":[{"internalType":"bytes[]","name":"","type":"bytes[]"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256[]","name":"takerAssetFillAmounts","type":"uint256[]"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"batchFillOrKillOrders","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults[]","name":"fillResults","type":"tuple[]"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256[]","name":"takerAssetFillAmounts","type":"uint256[]"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"batchFillOrders","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults[]","name":"fillResults","type":"tuple[]"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256[]","name":"takerAssetFillAmounts","type":"uint256[]"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"batchFillOrdersNoThrow","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults[]","name":"fillResults","type":"tuple[]"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"leftOrders","type":"tuple[]"},{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"rightOrders","type":"tuple[]"},{"internalType":"bytes[]","name":"leftSignatures","type":"bytes[]"},{"internalType":"bytes[]","name":"rightSignatures","type":"bytes[]"}],"name":"batchMatchOrders","outputs":[{"components":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults[]","name":"left","type":"tuple[]"},{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults[]","name":"right","type":"tuple[]"},{"internalType":"uint256","name":"profitInLeftMakerAsset","type":"uint256"},{"internalType":"uint256","name":"profitInRightMakerAsset","type":"uint256"}],"internalType":"struct LibFillResults.BatchMatchedFillResults","name":"batchMatchedFillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"leftOrders","type":"tuple[]"},{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"rightOrders","type":"tuple[]"},{"internalType":"bytes[]","name":"leftSignatures","type":"bytes[]"},{"internalType":"bytes[]","name":"rightSignatures","type":"bytes[]"}],"name":"batchMatchOrdersWithMaximalFill","outputs":[{"components":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults[]","name":"left","type":"tuple[]"},{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults[]","name":"right","type":"tuple[]"},{"internalType":"uint256","name":"profitInLeftMakerAsset","type":"uint256"},{"internalType":"uint256","name":"profitInRightMakerAsset","type":"uint256"}],"internalType":"struct LibFillResults.BatchMatchedFillResults","name":"batchMatchedFillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"order","type":"tuple"}],"name":"cancelOrder","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"targetOrderEpoch","type":"uint256"}],"name":"cancelOrdersUpTo","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"cancelled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"currentContextAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct LibZeroExTransaction.ZeroExTransaction","name":"transaction","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"executeTransaction","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"order","type":"tuple"},{"internalType":"uint256","name":"takerAssetFillAmount","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"fillOrKillOrder","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"fillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"order","type":"tuple"},{"internalType":"uint256","name":"takerAssetFillAmount","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"fillOrder","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"fillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"filled","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes4","name":"assetProxyId","type":"bytes4"}],"name":"getAssetProxy","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"order","type":"tuple"}],"name":"getOrderInfo","outputs":[{"components":[{"internalType":"uint8","name":"orderStatus","type":"uint8"},{"internalType":"bytes32","name":"orderHash","type":"bytes32"},{"internalType":"uint256","name":"orderTakerAssetFilledAmount","type":"uint256"}],"internalType":"struct LibOrder.OrderInfo","name":"orderInfo","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"hash","type":"bytes32"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"isValidHashSignature","outputs":[{"internalType":"bool","name":"isValid","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"order","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"isValidOrderSignature","outputs":[{"internalType":"bool","name":"isValid","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct LibZeroExTransaction.ZeroExTransaction","name":"transaction","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"isValidTransactionSignature","outputs":[{"internalType":"bool","name":"isValid","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256","name":"makerAssetFillAmount","type":"uint256"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"marketBuyOrdersFillOrKill","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"fillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256","name":"makerAssetFillAmount","type":"uint256"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"marketBuyOrdersNoThrow","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"fillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256","name":"takerAssetFillAmount","type":"uint256"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"marketSellOrdersFillOrKill","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"fillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256","name":"takerAssetFillAmount","type":"uint256"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"marketSellOrdersNoThrow","outputs":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"fillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"leftOrder","type":"tuple"},{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"rightOrder","type":"tuple"},{"internalType":"bytes","name":"leftSignature","type":"bytes"},{"internalType":"bytes","name":"rightSignature","type":"bytes"}],"name":"matchOrders","outputs":[{"components":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"left","type":"tuple"},{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"right","type":"tuple"},{"internalType":"uint256","name":"profitInLeftMakerAsset","type":"uint256"},{"internalType":"uint256","name":"profitInRightMakerAsset","type":"uint256"}],"internalType":"struct LibFillResults.MatchedFillResults","name":"matchedFillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"leftOrder","type":"tuple"},{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"rightOrder","type":"tuple"},{"internalType":"bytes","name":"leftSignature","type":"bytes"},{"internalType":"bytes","name":"rightSignature","type":"bytes"}],"name":"matchOrdersWithMaximalFill","outputs":[{"components":[{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"left","type":"tuple"},{"components":[{"internalType":"uint256","name":"makerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetFilledAmount","type":"uint256"},{"internalType":"uint256","name":"makerFeePaid","type":"uint256"},{"internalType":"uint256","name":"takerFeePaid","type":"uint256"},{"internalType":"uint256","name":"protocolFeePaid","type":"uint256"}],"internalType":"struct LibFillResults.FillResults","name":"right","type":"tuple"},{"internalType":"uint256","name":"profitInLeftMakerAsset","type":"uint256"},{"internalType":"uint256","name":"profitInRightMakerAsset","type":"uint256"}],"internalType":"struct LibFillResults.MatchedFillResults","name":"matchedFillResults","type":"tuple"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"}],"name":"orderEpoch","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"hash","type":"bytes32"}],"name":"preSign","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"},{"internalType":"address","name":"index_1","type":"address"}],"name":"preSigned","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"protocolFeeCollector","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"protocolFeeMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"assetProxy","type":"address"}],"name":"registerAssetProxy","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"updatedProtocolFeeCollector","type":"address"}],"name":"setProtocolFeeCollectorAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"updatedProtocolFeeMultiplier","type":"uint256"}],"name":"setProtocolFeeMultiplier","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"validatorAddress","type":"address"},{"internalType":"bool","name":"approval","type":"bool"}],"name":"setSignatureValidatorApproval","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes[]","name":"assetData","type":"bytes[]"},{"internalType":"address[]","name":"fromAddresses","type":"address[]"},{"internalType":"address[]","name":"toAddresses","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"name":"simulateDispatchTransferFromCalls","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"transactionsExecuted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
