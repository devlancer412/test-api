"""Generated wrapper for Coordinator Solidity contract."""

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
# constructor for Coordinator below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        CoordinatorValidator,
    )
except ImportError:

    class CoordinatorValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


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


class LibCoordinatorApprovalCoordinatorApproval(TypedDict):
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

    txOrigin: str

    transactionHash: Union[bytes, str]

    transactionSignature: Union[bytes, str]


class Eip712CoordinatorApprovalSchemaHashMethod(ContractMethod):
    """Various interfaces to the EIP712_COORDINATOR_APPROVAL_SCHEMA_HASH method."""

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


class Eip712CoordinatorDomainHashMethod(ContractMethod):
    """Various interfaces to the EIP712_COORDINATOR_DOMAIN_HASH method."""

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


class Eip712CoordinatorDomainNameMethod(ContractMethod):
    """Various interfaces to the EIP712_COORDINATOR_DOMAIN_NAME method."""

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


class Eip712CoordinatorDomainVersionMethod(ContractMethod):
    """Various interfaces to the EIP712_COORDINATOR_DOMAIN_VERSION method."""

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


class AssertValidCoordinatorApprovalsMethod(ContractMethod):
    """Various interfaces to the assertValidCoordinatorApprovals method."""

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
        tx_origin: str,
        transaction_signature: Union[bytes, str],
        approval_signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the assertValidCoordinatorApprovals method."""
        self.validator.assert_valid(
            method_name="assertValidCoordinatorApprovals",
            parameter_name="transaction",
            argument_value=transaction,
        )
        self.validator.assert_valid(
            method_name="assertValidCoordinatorApprovals",
            parameter_name="txOrigin",
            argument_value=tx_origin,
        )
        tx_origin = self.validate_and_checksum_address(tx_origin)
        self.validator.assert_valid(
            method_name="assertValidCoordinatorApprovals",
            parameter_name="transactionSignature",
            argument_value=transaction_signature,
        )
        self.validator.assert_valid(
            method_name="assertValidCoordinatorApprovals",
            parameter_name="approvalSignatures",
            argument_value=approval_signatures,
        )
        return (
            transaction,
            tx_origin,
            transaction_signature,
            approval_signatures,
        )

    def call(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        tx_origin: str,
        transaction_signature: Union[bytes, str],
        approval_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Validates that the 0x transaction has been approved by all of the
        feeRecipients that correspond to each order in the transaction's
        Exchange calldata.

        :param approvalSignatures: Array of signatures that correspond to the
            feeRecipients of each        order in the transaction's Exchange
            calldata.
        :param transaction: 0x transaction containing salt, signerAddress, and
            data.
        :param transactionSignature: Proof that the transaction has been signed
            by the signer.
        :param txOrigin: Required signer of Ethereum transaction calling this
            function.
        :param tx_params: transaction parameters

        """
        (
            transaction,
            tx_origin,
            transaction_signature,
            approval_signatures,
        ) = self.validate_and_normalize_inputs(
            transaction, tx_origin, transaction_signature, approval_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            transaction, tx_origin, transaction_signature, approval_signatures
        ).call(tx_params.as_dict())

    def estimate_gas(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        tx_origin: str,
        transaction_signature: Union[bytes, str],
        approval_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            transaction,
            tx_origin,
            transaction_signature,
            approval_signatures,
        ) = self.validate_and_normalize_inputs(
            transaction, tx_origin, transaction_signature, approval_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            transaction, tx_origin, transaction_signature, approval_signatures
        ).estimateGas(tx_params.as_dict())


class DecodeOrdersFromFillDataMethod(ContractMethod):
    """Various interfaces to the decodeOrdersFromFillData method."""

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

    def validate_and_normalize_inputs(self, data: Union[bytes, str]):
        """Validate the inputs to the decodeOrdersFromFillData method."""
        self.validator.assert_valid(
            method_name="decodeOrdersFromFillData",
            parameter_name="data",
            argument_value=data,
        )
        return data

    def call(
        self, data: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> List[LibOrderOrder]:
        """Execute underlying contract method via eth_call.

        Decodes the orders from Exchange calldata representing any fill method.

        :param data: Exchange calldata representing a fill method.
        :param tx_params: transaction parameters
        :returns: orders The orders from the Exchange calldata.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return [
            LibOrderOrder(
                makerAddress=element[0],
                takerAddress=element[1],
                feeRecipientAddress=element[2],
                senderAddress=element[3],
                makerAssetAmount=element[4],
                takerAssetAmount=element[5],
                makerFee=element[6],
                takerFee=element[7],
                expirationTimeSeconds=element[8],
                salt=element[9],
                makerAssetData=element[10],
                takerAssetData=element[11],
                makerFeeAssetData=element[12],
                takerFeeAssetData=element[13],
            )
            for element in returned
        ]

    def estimate_gas(
        self, data: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())


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
        tx_origin: str,
        transaction_signature: Union[bytes, str],
        approval_signatures: List[Union[bytes, str]],
    ):
        """Validate the inputs to the executeTransaction method."""
        self.validator.assert_valid(
            method_name="executeTransaction",
            parameter_name="transaction",
            argument_value=transaction,
        )
        self.validator.assert_valid(
            method_name="executeTransaction",
            parameter_name="txOrigin",
            argument_value=tx_origin,
        )
        tx_origin = self.validate_and_checksum_address(tx_origin)
        self.validator.assert_valid(
            method_name="executeTransaction",
            parameter_name="transactionSignature",
            argument_value=transaction_signature,
        )
        self.validator.assert_valid(
            method_name="executeTransaction",
            parameter_name="approvalSignatures",
            argument_value=approval_signatures,
        )
        return (
            transaction,
            tx_origin,
            transaction_signature,
            approval_signatures,
        )

    def call(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        tx_origin: str,
        transaction_signature: Union[bytes, str],
        approval_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Executes a 0x transaction that has been signed by the feeRecipients
        that correspond to each order in the transaction's Exchange calldata.

        :param approvalSignatures: Array of signatures that correspond to the
            feeRecipients of each        order in the transaction's Exchange
            calldata.
        :param transaction: 0x transaction containing salt, signerAddress, and
            data.
        :param transactionSignature: Proof that the transaction has been signed
            by the signer.
        :param txOrigin: Required signer of Ethereum transaction calling this
            function.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            transaction,
            tx_origin,
            transaction_signature,
            approval_signatures,
        ) = self.validate_and_normalize_inputs(
            transaction, tx_origin, transaction_signature, approval_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            transaction, tx_origin, transaction_signature, approval_signatures
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        tx_origin: str,
        transaction_signature: Union[bytes, str],
        approval_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Executes a 0x transaction that has been signed by the feeRecipients
        that correspond to each order in the transaction's Exchange calldata.

        :param approvalSignatures: Array of signatures that correspond to the
            feeRecipients of each        order in the transaction's Exchange
            calldata.
        :param transaction: 0x transaction containing salt, signerAddress, and
            data.
        :param transactionSignature: Proof that the transaction has been signed
            by the signer.
        :param txOrigin: Required signer of Ethereum transaction calling this
            function.
        :param tx_params: transaction parameters
        """
        (
            transaction,
            tx_origin,
            transaction_signature,
            approval_signatures,
        ) = self.validate_and_normalize_inputs(
            transaction, tx_origin, transaction_signature, approval_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            transaction, tx_origin, transaction_signature, approval_signatures
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        tx_origin: str,
        transaction_signature: Union[bytes, str],
        approval_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            transaction,
            tx_origin,
            transaction_signature,
            approval_signatures,
        ) = self.validate_and_normalize_inputs(
            transaction, tx_origin, transaction_signature, approval_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            transaction, tx_origin, transaction_signature, approval_signatures
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        tx_origin: str,
        transaction_signature: Union[bytes, str],
        approval_signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            transaction,
            tx_origin,
            transaction_signature,
            approval_signatures,
        ) = self.validate_and_normalize_inputs(
            transaction, tx_origin, transaction_signature, approval_signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            transaction, tx_origin, transaction_signature, approval_signatures
        ).estimateGas(tx_params.as_dict())


class GetCoordinatorApprovalHashMethod(ContractMethod):
    """Various interfaces to the getCoordinatorApprovalHash method."""

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
        self, approval: LibCoordinatorApprovalCoordinatorApproval
    ):
        """Validate the inputs to the getCoordinatorApprovalHash method."""
        self.validator.assert_valid(
            method_name="getCoordinatorApprovalHash",
            parameter_name="approval",
            argument_value=approval,
        )
        return approval

    def call(
        self,
        approval: LibCoordinatorApprovalCoordinatorApproval,
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Calculates the EIP712 hash of the Coordinator approval mesasage using
        the domain separator of this contract.

        :param approval: Coordinator approval message containing the
            transaction hash, and transaction        signature.
        :param tx_params: transaction parameters
        :returns: approvalHash EIP712 hash of the Coordinator approval message
            with the domain separator of this contract.
        """
        (approval) = self.validate_and_normalize_inputs(approval)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(approval).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(
        self,
        approval: LibCoordinatorApprovalCoordinatorApproval,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (approval) = self.validate_and_normalize_inputs(approval)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(approval).estimateGas(
            tx_params.as_dict()
        )


class GetSignerAddressMethod(ContractMethod):
    """Various interfaces to the getSignerAddress method."""

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
        self, _hash: Union[bytes, str], signature: Union[bytes, str]
    ):
        """Validate the inputs to the getSignerAddress method."""
        self.validator.assert_valid(
            method_name="getSignerAddress",
            parameter_name="hash",
            argument_value=_hash,
        )
        self.validator.assert_valid(
            method_name="getSignerAddress",
            parameter_name="signature",
            argument_value=signature,
        )
        return (_hash, signature)

    def call(
        self,
        _hash: Union[bytes, str],
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        Recovers the address of a signer given a hash and signature.

        :param hash: Any 32 byte hash.
        :param signature: Proof that the hash has been signed by signer.
        :param tx_params: transaction parameters
        :returns: signerAddress Address of the signer.
        """
        (_hash, signature) = self.validate_and_normalize_inputs(
            _hash, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_hash, signature).call(
            tx_params.as_dict()
        )
        return str(returned)

    def estimate_gas(
        self,
        _hash: Union[bytes, str],
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_hash, signature) = self.validate_and_normalize_inputs(
            _hash, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_hash, signature).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Coordinator:
    """Wrapper class for Coordinator Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    eip712_coordinator_approval_schema_hash: Eip712CoordinatorApprovalSchemaHashMethod
    """Constructor-initialized instance of
    :class:`Eip712CoordinatorApprovalSchemaHashMethod`.
    """

    eip712_coordinator_domain_hash: Eip712CoordinatorDomainHashMethod
    """Constructor-initialized instance of
    :class:`Eip712CoordinatorDomainHashMethod`.
    """

    eip712_coordinator_domain_name: Eip712CoordinatorDomainNameMethod
    """Constructor-initialized instance of
    :class:`Eip712CoordinatorDomainNameMethod`.
    """

    eip712_coordinator_domain_version: Eip712CoordinatorDomainVersionMethod
    """Constructor-initialized instance of
    :class:`Eip712CoordinatorDomainVersionMethod`.
    """

    eip712_exchange_domain_hash: Eip712ExchangeDomainHashMethod
    """Constructor-initialized instance of
    :class:`Eip712ExchangeDomainHashMethod`.
    """

    assert_valid_coordinator_approvals: AssertValidCoordinatorApprovalsMethod
    """Constructor-initialized instance of
    :class:`AssertValidCoordinatorApprovalsMethod`.
    """

    decode_orders_from_fill_data: DecodeOrdersFromFillDataMethod
    """Constructor-initialized instance of
    :class:`DecodeOrdersFromFillDataMethod`.
    """

    execute_transaction: ExecuteTransactionMethod
    """Constructor-initialized instance of
    :class:`ExecuteTransactionMethod`.
    """

    get_coordinator_approval_hash: GetCoordinatorApprovalHashMethod
    """Constructor-initialized instance of
    :class:`GetCoordinatorApprovalHashMethod`.
    """

    get_signer_address: GetSignerAddressMethod
    """Constructor-initialized instance of
    :class:`GetSignerAddressMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: CoordinatorValidator = None,
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
            validator = CoordinatorValidator(
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
            abi=Coordinator.abi(),
        ).functions

        self.eip712_coordinator_approval_schema_hash = Eip712CoordinatorApprovalSchemaHashMethod(
            web3_or_provider,
            contract_address,
            functions.EIP712_COORDINATOR_APPROVAL_SCHEMA_HASH,
        )

        self.eip712_coordinator_domain_hash = Eip712CoordinatorDomainHashMethod(
            web3_or_provider,
            contract_address,
            functions.EIP712_COORDINATOR_DOMAIN_HASH,
        )

        self.eip712_coordinator_domain_name = Eip712CoordinatorDomainNameMethod(
            web3_or_provider,
            contract_address,
            functions.EIP712_COORDINATOR_DOMAIN_NAME,
        )

        self.eip712_coordinator_domain_version = Eip712CoordinatorDomainVersionMethod(
            web3_or_provider,
            contract_address,
            functions.EIP712_COORDINATOR_DOMAIN_VERSION,
        )

        self.eip712_exchange_domain_hash = Eip712ExchangeDomainHashMethod(
            web3_or_provider,
            contract_address,
            functions.EIP712_EXCHANGE_DOMAIN_HASH,
        )

        self.assert_valid_coordinator_approvals = AssertValidCoordinatorApprovalsMethod(
            web3_or_provider,
            contract_address,
            functions.assertValidCoordinatorApprovals,
            validator,
        )

        self.decode_orders_from_fill_data = DecodeOrdersFromFillDataMethod(
            web3_or_provider,
            contract_address,
            functions.decodeOrdersFromFillData,
            validator,
        )

        self.execute_transaction = ExecuteTransactionMethod(
            web3_or_provider,
            contract_address,
            functions.executeTransaction,
            validator,
        )

        self.get_coordinator_approval_hash = GetCoordinatorApprovalHashMethod(
            web3_or_provider,
            contract_address,
            functions.getCoordinatorApprovalHash,
            validator,
        )

        self.get_signer_address = GetSignerAddressMethod(
            web3_or_provider,
            contract_address,
            functions.getSignerAddress,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"exchange","type":"address"},{"internalType":"uint256","name":"chainId","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":true,"inputs":[],"name":"EIP712_COORDINATOR_APPROVAL_SCHEMA_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"EIP712_COORDINATOR_DOMAIN_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"EIP712_COORDINATOR_DOMAIN_NAME","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"EIP712_COORDINATOR_DOMAIN_VERSION","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"EIP712_EXCHANGE_DOMAIN_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct LibZeroExTransaction.ZeroExTransaction","name":"transaction","type":"tuple"},{"internalType":"address","name":"txOrigin","type":"address"},{"internalType":"bytes","name":"transactionSignature","type":"bytes"},{"internalType":"bytes[]","name":"approvalSignatures","type":"bytes[]"}],"name":"assertValidCoordinatorApprovals","outputs":[],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"data","type":"bytes"}],"name":"decodeOrdersFromFillData","outputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct LibZeroExTransaction.ZeroExTransaction","name":"transaction","type":"tuple"},{"internalType":"address","name":"txOrigin","type":"address"},{"internalType":"bytes","name":"transactionSignature","type":"bytes"},{"internalType":"bytes[]","name":"approvalSignatures","type":"bytes[]"}],"name":"executeTransaction","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"address","name":"txOrigin","type":"address"},{"internalType":"bytes32","name":"transactionHash","type":"bytes32"},{"internalType":"bytes","name":"transactionSignature","type":"bytes"}],"internalType":"struct LibCoordinatorApproval.CoordinatorApproval","name":"approval","type":"tuple"}],"name":"getCoordinatorApprovalHash","outputs":[{"internalType":"bytes32","name":"approvalHash","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"hash","type":"bytes32"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"getSignerAddress","outputs":[{"internalType":"address","name":"signerAddress","type":"address"}],"payable":false,"stateMutability":"pure","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
