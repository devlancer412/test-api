"""Generated wrapper for DevUtils Solidity contract."""

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
# constructor for DevUtils below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DevUtilsValidator,
    )
except ImportError:

    class DevUtilsValidator(  # type: ignore
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


class DecodeAssetProxyDispatchErrorMethod(ContractMethod):
    """Various interfaces to the decodeAssetProxyDispatchError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeAssetProxyDispatchError method."""
        self.validator.assert_valid(
            method_name="decodeAssetProxyDispatchError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[int, Union[bytes, str], Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded AssetProxyDispatchError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: errorCode The error code.orderHash Hash of the order being
            dispatched.assetData Asset data of the order being dispatched.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeAssetProxyExistsErrorMethod(ContractMethod):
    """Various interfaces to the decodeAssetProxyExistsError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeAssetProxyExistsError method."""
        self.validator.assert_valid(
            method_name="decodeAssetProxyExistsError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[Union[bytes, str], str]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded AssetProxyExistsError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: assetProxyId Id of asset proxy.assetProxyAddress The address
            of the asset proxy.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeAssetProxyIdMethod(ContractMethod):
    """Various interfaces to the decodeAssetProxyId method."""

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
        """Validate the inputs to the decodeAssetProxyId method."""
        self.validator.assert_valid(
            method_name="decodeAssetProxyId",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return asset_data

    def call(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Decode AssetProxy identifier

        :param assetData: AssetProxy-compliant asset data describing an ERC-20,
            ERC-721, ERC1155, or MultiAsset asset.
        :param tx_params: transaction parameters
        :returns: The AssetProxy identifier
        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_data).call(
            tx_params.as_dict()
        )
        return Union[bytes, str](returned)

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


class DecodeAssetProxyTransferErrorMethod(ContractMethod):
    """Various interfaces to the decodeAssetProxyTransferError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeAssetProxyTransferError method."""
        self.validator.assert_valid(
            method_name="decodeAssetProxyTransferError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[Union[bytes, str], Union[bytes, str], Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded AssetProxyTransferError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: orderHash Hash of the order being dispatched.assetData Asset
            data of the order being dispatched.errorData ABI-encoded revert
            data from the asset proxy.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeEip1271SignatureErrorMethod(ContractMethod):
    """Various interfaces to the decodeEIP1271SignatureError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeEIP1271SignatureError method."""
        self.validator.assert_valid(
            method_name="decodeEIP1271SignatureError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[str, Union[bytes, str], Union[bytes, str], Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded SignatureValidatorError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: signerAddress The expected signer of the hash.signature The
            full signature bytes.errorData The revert data thrown by the
            validator contract.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeErc1155AssetDataMethod(ContractMethod):
    """Various interfaces to the decodeERC1155AssetData method."""

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
        """Validate the inputs to the decodeERC1155AssetData method."""
        self.validator.assert_valid(
            method_name="decodeERC1155AssetData",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return asset_data

    def call(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[
        Union[bytes, str], str, List[int], List[int], Union[bytes, str]
    ]:
        """Execute underlying contract method via eth_call.

        Decode ERC-1155 asset data from the format described in the AssetProxy
        contract specification.

        :param assetData: AssetProxy-compliant asset data describing an ERC-
            1155 set of assets.
        :param tx_params: transaction parameters
        :returns: The ERC-1155 AssetProxy identifier, the address of the ERC-
            1155 contract hosting the assets, an array of the identifiers of
            the assets to be traded, an array of asset amounts to be traded,
            and callback data. Each element of the arrays corresponds to the
            same-indexed element of the other array. Return values specified as
            `memory` are returned as pointers to locations within the memory of
            the input parameter `assetData`.
        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
            returned[4],
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


class DecodeErc20AssetDataMethod(ContractMethod):
    """Various interfaces to the decodeERC20AssetData method."""

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
        """Validate the inputs to the decodeERC20AssetData method."""
        self.validator.assert_valid(
            method_name="decodeERC20AssetData",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return asset_data

    def call(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[Union[bytes, str], str]:
        """Execute underlying contract method via eth_call.

        Decode ERC-20 asset data from the format described in the AssetProxy
        contract specification.

        :param assetData: AssetProxy-compliant asset data describing an ERC-20
            asset.
        :param tx_params: transaction parameters
        :returns: The AssetProxy identifier, and the address of the ERC-20
            contract hosting this asset.
        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
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


class DecodeErc721AssetDataMethod(ContractMethod):
    """Various interfaces to the decodeERC721AssetData method."""

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
        """Validate the inputs to the decodeERC721AssetData method."""
        self.validator.assert_valid(
            method_name="decodeERC721AssetData",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return asset_data

    def call(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[Union[bytes, str], str, int]:
        """Execute underlying contract method via eth_call.

        Decode ERC-721 asset data from the format described in the AssetProxy
        contract specification.

        :param assetData: AssetProxy-compliant asset data describing an ERC-721
            asset.
        :param tx_params: transaction parameters
        :returns: The ERC-721 AssetProxy identifier, the address of the ERC-721
            contract hosting this asset, and the identifier of the specific
            asset to be traded.
        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
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


class DecodeExchangeInvalidContextErrorMethod(ContractMethod):
    """Various interfaces to the decodeExchangeInvalidContextError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeExchangeInvalidContextError method."""
        self.validator.assert_valid(
            method_name="decodeExchangeInvalidContextError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[int, Union[bytes, str], str]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded OrderStatusError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: errorCode Error code that corresponds to invalid maker,
            taker, or sender.orderHash The order hash.contextAddress The maker,
            taker, or sender address
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeFillErrorMethod(ContractMethod):
    """Various interfaces to the decodeFillError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeFillError method."""
        self.validator.assert_valid(
            method_name="decodeFillError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[int, Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded FillError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: errorCode The error code.orderHash The order hash.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeIncompleteFillErrorMethod(ContractMethod):
    """Various interfaces to the decodeIncompleteFillError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeIncompleteFillError method."""
        self.validator.assert_valid(
            method_name="decodeIncompleteFillError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int, int]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded IncompleteFillError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: orderHash Hash of the order being filled.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeMultiAssetDataMethod(ContractMethod):
    """Various interfaces to the decodeMultiAssetData method."""

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
        """Validate the inputs to the decodeMultiAssetData method."""
        self.validator.assert_valid(
            method_name="decodeMultiAssetData",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return asset_data

    def call(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[Union[bytes, str], List[int], List[Union[bytes, str]]]:
        """Execute underlying contract method via eth_call.

        Decode multi-asset data from the format described in the AssetProxy
        contract specification.

        :param assetData: AssetProxy-compliant data describing a multi-asset
            basket.
        :param tx_params: transaction parameters
        :returns: The Multi-Asset AssetProxy identifier, an array of the
            amounts of the assets to be traded, and an array of the AssetProxy-
            compliant data describing each asset to be traded. Each element of
            the arrays corresponds to the same-indexed element of the other
            array.
        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
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


class DecodeNegativeSpreadErrorMethod(ContractMethod):
    """Various interfaces to the decodeNegativeSpreadError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeNegativeSpreadError method."""
        self.validator.assert_valid(
            method_name="decodeNegativeSpreadError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[Union[bytes, str], Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded NegativeSpreadError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: leftOrderHash Hash of the left order being
            matched.rightOrderHash Hash of the right order being matched.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeOrderEpochErrorMethod(ContractMethod):
    """Various interfaces to the decodeOrderEpochError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeOrderEpochError method."""
        self.validator.assert_valid(
            method_name="decodeOrderEpochError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[str, str, int]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded OrderEpochError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: makerAddress The order maker.orderSenderAddress The order
            sender.currentEpoch The current epoch for the maker.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeOrderStatusErrorMethod(ContractMethod):
    """Various interfaces to the decodeOrderStatusError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeOrderStatusError method."""
        self.validator.assert_valid(
            method_name="decodeOrderStatusError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[Union[bytes, str], int]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded OrderStatusError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: orderHash The order hash.orderStatus The order status.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeSignatureErrorMethod(ContractMethod):
    """Various interfaces to the decodeSignatureError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeSignatureError method."""
        self.validator.assert_valid(
            method_name="decodeSignatureError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[int, Union[bytes, str], str, Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded SignatureError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: errorCode The error code.signerAddress The expected signer of
            the hash.signature The full signature.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeSignatureValidatorNotApprovedErrorMethod(ContractMethod):
    """Various interfaces to the decodeSignatureValidatorNotApprovedError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeSignatureValidatorNotApprovedError method."""
        self.validator.assert_valid(
            method_name="decodeSignatureValidatorNotApprovedError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[str, str]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded SignatureValidatorNotApprovedError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: signerAddress The expected signer of the
            hash.validatorAddress The expected validator.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeSignatureWalletErrorMethod(ContractMethod):
    """Various interfaces to the decodeSignatureWalletError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeSignatureWalletError method."""
        self.validator.assert_valid(
            method_name="decodeSignatureWalletError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[Union[bytes, str], str, Union[bytes, str], Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded SignatureWalletError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: errorCode The error code.signerAddress The expected signer of
            the hash.signature The full signature bytes.errorData The revert
            data thrown by the validator contract.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeStaticCallAssetDataMethod(ContractMethod):
    """Various interfaces to the decodeStaticCallAssetData method."""

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
        """Validate the inputs to the decodeStaticCallAssetData method."""
        self.validator.assert_valid(
            method_name="decodeStaticCallAssetData",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return asset_data

    def call(
        self,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[Union[bytes, str], str, Union[bytes, str], Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decode StaticCall asset data from the format described in the
        AssetProxy contract specification.

        :param assetData: AssetProxy-compliant asset data describing a
            StaticCall asset
        :param tx_params: transaction parameters
        :returns: The StaticCall AssetProxy identifier, the target address of
            the StaticCAll, the data to be passed to the target address, and
            the expected Keccak-256 hash of the static call return data.
        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
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


class DecodeTransactionErrorMethod(ContractMethod):
    """Various interfaces to the decodeTransactionError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeTransactionError method."""
        self.validator.assert_valid(
            method_name="decodeTransactionError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[int, Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded TransactionError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: errorCode The error code.transactionHash Hash of the
            transaction.
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeTransactionExecutionErrorMethod(ContractMethod):
    """Various interfaces to the decodeTransactionExecutionError method."""

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

    def validate_and_normalize_inputs(self, encoded: Union[bytes, str]):
        """Validate the inputs to the decodeTransactionExecutionError method."""
        self.validator.assert_valid(
            method_name="decodeTransactionExecutionError",
            parameter_name="encoded",
            argument_value=encoded,
        )
        return encoded

    def call(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Tuple[Union[bytes, str], Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Decompose an ABI-encoded TransactionExecutionError.

        :param encoded: ABI-encoded revert error.
        :param tx_params: transaction parameters
        :returns: transactionHash Hash of the transaction.errorData Error
            thrown by exeucteTransaction().
        """
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(encoded).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self, encoded: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (encoded) = self.validate_and_normalize_inputs(encoded)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(encoded).estimateGas(
            tx_params.as_dict()
        )


class DecodeZeroExTransactionDataMethod(ContractMethod):
    """Various interfaces to the decodeZeroExTransactionData method."""

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
        self, transaction_data: Union[bytes, str]
    ):
        """Validate the inputs to the decodeZeroExTransactionData method."""
        self.validator.assert_valid(
            method_name="decodeZeroExTransactionData",
            parameter_name="transactionData",
            argument_value=transaction_data,
        )
        return transaction_data

    def call(
        self,
        transaction_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[str, List[LibOrderOrder], List[int], List[Union[bytes, str]]]:
        """Execute underlying contract method via eth_call.

        Decodes the call data for an Exchange contract method call.

        :param transactionData: ABI-encoded calldata for an Exchange
            contract method call.
        :param tx_params: transaction parameters
        :returns: The name of the function called, and the parameters it was
            given. For single-order fills and cancels, the arrays will have
            just one element.
        """
        (transaction_data) = self.validate_and_normalize_inputs(
            transaction_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(transaction_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
        )

    def estimate_gas(
        self,
        transaction_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction_data) = self.validate_and_normalize_inputs(
            transaction_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_data).estimateGas(
            tx_params.as_dict()
        )


class EncodeErc1155AssetDataMethod(ContractMethod):
    """Various interfaces to the encodeERC1155AssetData method."""

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
        token_address: str,
        token_ids: List[int],
        token_values: List[int],
        callback_data: Union[bytes, str],
    ):
        """Validate the inputs to the encodeERC1155AssetData method."""
        self.validator.assert_valid(
            method_name="encodeERC1155AssetData",
            parameter_name="tokenAddress",
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        self.validator.assert_valid(
            method_name="encodeERC1155AssetData",
            parameter_name="tokenIds",
            argument_value=token_ids,
        )
        self.validator.assert_valid(
            method_name="encodeERC1155AssetData",
            parameter_name="tokenValues",
            argument_value=token_values,
        )
        self.validator.assert_valid(
            method_name="encodeERC1155AssetData",
            parameter_name="callbackData",
            argument_value=callback_data,
        )
        return (token_address, token_ids, token_values, callback_data)

    def call(
        self,
        token_address: str,
        token_ids: List[int],
        token_values: List[int],
        callback_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Encode ERC-1155 asset data into the format described in the AssetProxy
        contract specification.

        :param callbackData: Data to be passed to receiving contracts when a
            transfer is performed.
        :param tokenAddress: The address of the ERC-1155 contract hosting the
            asset(s) to be traded.
        :param tokenIds: The identifiers of the specific assets to be traded.
        :param tokenValues: The amounts of each asset to be traded.
        :param tx_params: transaction parameters
        :returns: AssetProxy-compliant asset data describing the set of assets.
        """
        (
            token_address,
            token_ids,
            token_values,
            callback_data,
        ) = self.validate_and_normalize_inputs(
            token_address, token_ids, token_values, callback_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            token_address, token_ids, token_values, callback_data
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(
        self,
        token_address: str,
        token_ids: List[int],
        token_values: List[int],
        callback_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            token_address,
            token_ids,
            token_values,
            callback_data,
        ) = self.validate_and_normalize_inputs(
            token_address, token_ids, token_values, callback_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_address, token_ids, token_values, callback_data
        ).estimateGas(tx_params.as_dict())


class EncodeErc20AssetDataMethod(ContractMethod):
    """Various interfaces to the encodeERC20AssetData method."""

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

    def validate_and_normalize_inputs(self, token_address: str):
        """Validate the inputs to the encodeERC20AssetData method."""
        self.validator.assert_valid(
            method_name="encodeERC20AssetData",
            parameter_name="tokenAddress",
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        return token_address

    def call(
        self, token_address: str, tx_params: Optional[TxParams] = None
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Encode ERC-20 asset data into the format described in the AssetProxy
        contract specification.

        :param tokenAddress: The address of the ERC-20 contract hosting the
            asset to be traded.
        :param tx_params: transaction parameters
        :returns: AssetProxy-compliant data describing the asset.
        """
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_address).call(
            tx_params.as_dict()
        )
        return Union[bytes, str](returned)

    def estimate_gas(
        self, token_address: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).estimateGas(
            tx_params.as_dict()
        )


class EncodeErc721AssetDataMethod(ContractMethod):
    """Various interfaces to the encodeERC721AssetData method."""

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

    def validate_and_normalize_inputs(self, token_address: str, token_id: int):
        """Validate the inputs to the encodeERC721AssetData method."""
        self.validator.assert_valid(
            method_name="encodeERC721AssetData",
            parameter_name="tokenAddress",
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        self.validator.assert_valid(
            method_name="encodeERC721AssetData",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (token_address, token_id)

    def call(
        self,
        token_address: str,
        token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Encode ERC-721 asset data into the format described in the AssetProxy
        specification.

        :param tokenAddress: The address of the ERC-721 contract hosting the
            asset to be traded.
        :param tokenId: The identifier of the specific asset to be traded.
        :param tx_params: transaction parameters
        :returns: AssetProxy-compliant asset data describing the asset.
        """
        (token_address, token_id) = self.validate_and_normalize_inputs(
            token_address, token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_address, token_id).call(
            tx_params.as_dict()
        )
        return Union[bytes, str](returned)

    def estimate_gas(
        self,
        token_address: str,
        token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_address, token_id) = self.validate_and_normalize_inputs(
            token_address, token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address, token_id).estimateGas(
            tx_params.as_dict()
        )


class EncodeMultiAssetDataMethod(ContractMethod):
    """Various interfaces to the encodeMultiAssetData method."""

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
        self, amounts: List[int], nested_asset_data: List[Union[bytes, str]]
    ):
        """Validate the inputs to the encodeMultiAssetData method."""
        self.validator.assert_valid(
            method_name="encodeMultiAssetData",
            parameter_name="amounts",
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="encodeMultiAssetData",
            parameter_name="nestedAssetData",
            argument_value=nested_asset_data,
        )
        return (amounts, nested_asset_data)

    def call(
        self,
        amounts: List[int],
        nested_asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Encode data for multiple assets, per the AssetProxy contract
        specification.

        :param amounts: The amounts of each asset to be traded.
        :param nestedAssetData: AssetProxy-compliant data describing each asset
            to be traded.
        :param tx_params: transaction parameters
        :returns: AssetProxy-compliant data describing the set of assets.
        """
        (amounts, nested_asset_data) = self.validate_and_normalize_inputs(
            amounts, nested_asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(amounts, nested_asset_data).call(
            tx_params.as_dict()
        )
        return Union[bytes, str](returned)

    def estimate_gas(
        self,
        amounts: List[int],
        nested_asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (amounts, nested_asset_data) = self.validate_and_normalize_inputs(
            amounts, nested_asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amounts, nested_asset_data).estimateGas(
            tx_params.as_dict()
        )


class EncodeStaticCallAssetDataMethod(ContractMethod):
    """Various interfaces to the encodeStaticCallAssetData method."""

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
        static_call_target_address: str,
        static_call_data: Union[bytes, str],
        expected_return_data_hash: Union[bytes, str],
    ):
        """Validate the inputs to the encodeStaticCallAssetData method."""
        self.validator.assert_valid(
            method_name="encodeStaticCallAssetData",
            parameter_name="staticCallTargetAddress",
            argument_value=static_call_target_address,
        )
        static_call_target_address = self.validate_and_checksum_address(
            static_call_target_address
        )
        self.validator.assert_valid(
            method_name="encodeStaticCallAssetData",
            parameter_name="staticCallData",
            argument_value=static_call_data,
        )
        self.validator.assert_valid(
            method_name="encodeStaticCallAssetData",
            parameter_name="expectedReturnDataHash",
            argument_value=expected_return_data_hash,
        )
        return (
            static_call_target_address,
            static_call_data,
            expected_return_data_hash,
        )

    def call(
        self,
        static_call_target_address: str,
        static_call_data: Union[bytes, str],
        expected_return_data_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Encode StaticCall asset data into the format described in the
        AssetProxy contract specification.

        :param expectedReturnDataHash: Expected Keccak-256 hash of the
            StaticCall return data.
        :param staticCallData: Data that will be passed to
            staticCallTargetAddress in the StaticCall.
        :param staticCallTargetAddress: Target address of StaticCall.
        :param tx_params: transaction parameters
        :returns: AssetProxy-compliant asset data describing the set of assets.
        """
        (
            static_call_target_address,
            static_call_data,
            expected_return_data_hash,
        ) = self.validate_and_normalize_inputs(
            static_call_target_address,
            static_call_data,
            expected_return_data_hash,
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            static_call_target_address,
            static_call_data,
            expected_return_data_hash,
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(
        self,
        static_call_target_address: str,
        static_call_data: Union[bytes, str],
        expected_return_data_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            static_call_target_address,
            static_call_data,
            expected_return_data_hash,
        ) = self.validate_and_normalize_inputs(
            static_call_target_address,
            static_call_data,
            expected_return_data_hash,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            static_call_target_address,
            static_call_data,
            expected_return_data_hash,
        ).estimateGas(tx_params.as_dict())


class GetAssetProxyAllowanceMethod(ContractMethod):
    """Various interfaces to the getAssetProxyAllowance method."""

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
        self, owner_address: str, asset_data: Union[bytes, str]
    ):
        """Validate the inputs to the getAssetProxyAllowance method."""
        self.validator.assert_valid(
            method_name="getAssetProxyAllowance",
            parameter_name="ownerAddress",
            argument_value=owner_address,
        )
        owner_address = self.validate_and_checksum_address(owner_address)
        self.validator.assert_valid(
            method_name="getAssetProxyAllowance",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (owner_address, asset_data)

    def call(
        self,
        owner_address: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        Returns the number of asset(s) (described by assetData) that the
        corresponding AssetProxy contract is authorized to spend. When the
        asset data contains multiple assets (eg for Multi-Asset), the return
        value indicates how many complete "baskets" of those assets may be
        spent by all of the corresponding AssetProxy contracts.

        :param assetData: Details of asset, encoded per the AssetProxy contract
            specification.
        :param ownerAddress: Owner of the assets specified by assetData.
        :param tx_params: transaction parameters
        :returns: Number of assets (or asset baskets) that the corresponding
            AssetProxy is authorized to spend.
        """
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner_address, asset_data).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self,
        owner_address: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner_address, asset_data).estimateGas(
            tx_params.as_dict()
        )


class GetBalanceMethod(ContractMethod):
    """Various interfaces to the getBalance method."""

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
        self, owner_address: str, asset_data: Union[bytes, str]
    ):
        """Validate the inputs to the getBalance method."""
        self.validator.assert_valid(
            method_name="getBalance",
            parameter_name="ownerAddress",
            argument_value=owner_address,
        )
        owner_address = self.validate_and_checksum_address(owner_address)
        self.validator.assert_valid(
            method_name="getBalance",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (owner_address, asset_data)

    def call(
        self,
        owner_address: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        Returns the owner's balance of the assets(s) specified in assetData.
        When the asset data contains multiple assets (eg in ERC1155 or Multi-
        Asset), the return value indicates how many complete "baskets" of those
        assets are owned by owner.

        :param assetData: Details of asset, encoded per the AssetProxy contract
            specification.
        :param ownerAddress: Owner of the assets specified by assetData.
        :param tx_params: transaction parameters
        :returns: Number of assets (or asset baskets) held by owner.
        """
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner_address, asset_data).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self,
        owner_address: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner_address, asset_data).estimateGas(
            tx_params.as_dict()
        )


class GetBalanceAndAssetProxyAllowanceMethod(ContractMethod):
    """Various interfaces to the getBalanceAndAssetProxyAllowance method."""

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
        self, owner_address: str, asset_data: Union[bytes, str]
    ):
        """Validate the inputs to the getBalanceAndAssetProxyAllowance method."""
        self.validator.assert_valid(
            method_name="getBalanceAndAssetProxyAllowance",
            parameter_name="ownerAddress",
            argument_value=owner_address,
        )
        owner_address = self.validate_and_checksum_address(owner_address)
        self.validator.assert_valid(
            method_name="getBalanceAndAssetProxyAllowance",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (owner_address, asset_data)

    def call(
        self,
        owner_address: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        Calls getBalance() and getAllowance() for assetData.

        :param assetData: Details of asset, encoded per the AssetProxy contract
            specification.
        :param ownerAddress: Owner of the assets specified by assetData.
        :param tx_params: transaction parameters
        :returns: Number of assets (or asset baskets) held by owner, and number
            of assets (or asset baskets) that the corresponding AssetProxy is
            authorized to spend.
        """
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner_address, asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self,
        owner_address: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner_address, asset_data).estimateGas(
            tx_params.as_dict()
        )


class GetBatchAssetProxyAllowancesMethod(ContractMethod):
    """Various interfaces to the getBatchAssetProxyAllowances method."""

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
        self, owner_address: str, asset_data: List[Union[bytes, str]]
    ):
        """Validate the inputs to the getBatchAssetProxyAllowances method."""
        self.validator.assert_valid(
            method_name="getBatchAssetProxyAllowances",
            parameter_name="ownerAddress",
            argument_value=owner_address,
        )
        owner_address = self.validate_and_checksum_address(owner_address)
        self.validator.assert_valid(
            method_name="getBatchAssetProxyAllowances",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (owner_address, asset_data)

    def call(
        self,
        owner_address: str,
        asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        Calls getAssetProxyAllowance() for each element of assetData.

        :param assetData: Array of asset details, each encoded per the
            AssetProxy contract specification.
        :param ownerAddress: Owner of the assets specified by assetData.
        :param tx_params: transaction parameters
        :returns: An array of asset allowances from getAllowance(), with each
            element corresponding to the same-indexed element in the assetData
            input.
        """
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner_address, asset_data).call(
            tx_params.as_dict()
        )
        return [int(element) for element in returned]

    def estimate_gas(
        self,
        owner_address: str,
        asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner_address, asset_data).estimateGas(
            tx_params.as_dict()
        )


class GetBatchBalancesMethod(ContractMethod):
    """Various interfaces to the getBatchBalances method."""

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
        self, owner_address: str, asset_data: List[Union[bytes, str]]
    ):
        """Validate the inputs to the getBatchBalances method."""
        self.validator.assert_valid(
            method_name="getBatchBalances",
            parameter_name="ownerAddress",
            argument_value=owner_address,
        )
        owner_address = self.validate_and_checksum_address(owner_address)
        self.validator.assert_valid(
            method_name="getBatchBalances",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (owner_address, asset_data)

    def call(
        self,
        owner_address: str,
        asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        Calls getBalance() for each element of assetData.

        :param assetData: Array of asset details, each encoded per the
            AssetProxy contract specification.
        :param ownerAddress: Owner of the assets specified by assetData.
        :param tx_params: transaction parameters
        :returns: Array of asset balances from getBalance(), with each element
            corresponding to the same-indexed element in the assetData input.
        """
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner_address, asset_data).call(
            tx_params.as_dict()
        )
        return [int(element) for element in returned]

    def estimate_gas(
        self,
        owner_address: str,
        asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner_address, asset_data).estimateGas(
            tx_params.as_dict()
        )


class GetBatchBalancesAndAssetProxyAllowancesMethod(ContractMethod):
    """Various interfaces to the getBatchBalancesAndAssetProxyAllowances method."""

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
        self, owner_address: str, asset_data: List[Union[bytes, str]]
    ):
        """Validate the inputs to the getBatchBalancesAndAssetProxyAllowances method."""
        self.validator.assert_valid(
            method_name="getBatchBalancesAndAssetProxyAllowances",
            parameter_name="ownerAddress",
            argument_value=owner_address,
        )
        owner_address = self.validate_and_checksum_address(owner_address)
        self.validator.assert_valid(
            method_name="getBatchBalancesAndAssetProxyAllowances",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (owner_address, asset_data)

    def call(
        self,
        owner_address: str,
        asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[List[int], List[int]]:
        """Execute underlying contract method via eth_call.

        Calls getBatchBalances() and getBatchAllowances() for each element of
        assetData.

        :param assetData: Array of asset details, each encoded per the
            AssetProxy contract specification.
        :param ownerAddress: Owner of the assets specified by assetData.
        :param tx_params: transaction parameters
        :returns: An array of asset balances from getBalance(), and an array of
            asset allowances from getAllowance(), with each element
            corresponding to the same-indexed element in the assetData input.
        """
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner_address, asset_data).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def estimate_gas(
        self,
        owner_address: str,
        asset_data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner_address, asset_data).estimateGas(
            tx_params.as_dict()
        )


class GetEthBalancesMethod(ContractMethod):
    """Various interfaces to the getEthBalances method."""

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
        returned = self._underlying_method(addresses).call(tx_params.as_dict())
        return [int(element) for element in returned]

    def estimate_gas(
        self, addresses: List[str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addresses) = self.validate_and_normalize_inputs(addresses)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addresses).estimateGas(
            tx_params.as_dict()
        )


class GetOrderHashMethod(ContractMethod):
    """Various interfaces to the getOrderHash method."""

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
        self, order: LibOrderOrder, chain_id: int, exchange: str
    ):
        """Validate the inputs to the getOrderHash method."""
        self.validator.assert_valid(
            method_name="getOrderHash",
            parameter_name="order",
            argument_value=order,
        )
        self.validator.assert_valid(
            method_name="getOrderHash",
            parameter_name="chainId",
            argument_value=chain_id,
        )
        # safeguard against fractional inputs
        chain_id = int(chain_id)
        self.validator.assert_valid(
            method_name="getOrderHash",
            parameter_name="exchange",
            argument_value=exchange,
        )
        exchange = self.validate_and_checksum_address(exchange)
        return (order, chain_id, exchange)

    def call(
        self,
        order: LibOrderOrder,
        chain_id: int,
        exchange: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (order, chain_id, exchange) = self.validate_and_normalize_inputs(
            order, chain_id, exchange
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(order, chain_id, exchange).call(
            tx_params.as_dict()
        )
        return Union[bytes, str](returned)

    def estimate_gas(
        self,
        order: LibOrderOrder,
        chain_id: int,
        exchange: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (order, chain_id, exchange) = self.validate_and_normalize_inputs(
            order, chain_id, exchange
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(order, chain_id, exchange).estimateGas(
            tx_params.as_dict()
        )


class GetOrderRelevantStateMethod(ContractMethod):
    """Various interfaces to the getOrderRelevantState method."""

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
        """Validate the inputs to the getOrderRelevantState method."""
        self.validator.assert_valid(
            method_name="getOrderRelevantState",
            parameter_name="order",
            argument_value=order,
        )
        self.validator.assert_valid(
            method_name="getOrderRelevantState",
            parameter_name="signature",
            argument_value=signature,
        )
        return (order, signature)

    def call(
        self,
        order: LibOrderOrder,
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[LibOrderOrderInfo, int, bool]:
        """Execute underlying contract method via eth_call.

        Fetches all order-relevant information needed to validate if the
        supplied order is fillable.

        :param order: The order structure.
        :param signature: Signature provided by maker that proves the order's
            authenticity. `0x01` can always be provided if the signature does
            not need to be validated.
        :param tx_params: transaction parameters
        :returns: The orderInfo (hash, status, and `takerAssetAmount` already
            filled for the given order), fillableTakerAssetAmount (amount of
            the order's `takerAssetAmount` that is fillable given all on-chain
            state), and isValidSignature (validity of the provided signature).
            NOTE: If the `takerAssetData` encodes data for multiple assets,
            `fillableTakerAssetAmount` will represent a "scaled" amount,
            meaning it must be multiplied by all the individual asset amounts
            within the `takerAssetData` to get the final amount of each asset
            that can be filled.
        """
        (order, signature) = self.validate_and_normalize_inputs(
            order, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(order, signature).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
        )

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


class GetOrderRelevantStatesMethod(ContractMethod):
    """Various interfaces to the getOrderRelevantStates method."""

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
        self, orders: List[LibOrderOrder], signatures: List[Union[bytes, str]]
    ):
        """Validate the inputs to the getOrderRelevantStates method."""
        self.validator.assert_valid(
            method_name="getOrderRelevantStates",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="getOrderRelevantStates",
            parameter_name="signatures",
            argument_value=signatures,
        )
        return (orders, signatures)

    def call(
        self,
        orders: List[LibOrderOrder],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[List[LibOrderOrderInfo], List[int], List[bool]]:
        """Execute underlying contract method via eth_call.

        Fetches all order-relevant information needed to validate if the
        supplied orders are fillable.

        :param orders: Array of order structures.
        :param signatures: Array of signatures provided by makers that prove
            the authenticity of the orders. `0x01` can always be provided if a
            signature does not need to be validated.
        :param tx_params: transaction parameters
        :returns: The ordersInfo (array of the hash, status, and
            `takerAssetAmount` already filled for each order),
            fillableTakerAssetAmounts (array of amounts for each order's
            `takerAssetAmount` that is fillable given all on-chain state), and
            isValidSignature (array containing the validity of each provided
            signature). NOTE: If the `takerAssetData` encodes data for multiple
            assets, each element of `fillableTakerAssetAmounts` will represent
            a "scaled" amount, meaning it must be multiplied by all the
            individual asset amounts within the `takerAssetData` to get the
            final amount of each asset that can be filled.
        """
        (orders, signatures) = self.validate_and_normalize_inputs(
            orders, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(orders, signatures).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        signatures: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (orders, signatures) = self.validate_and_normalize_inputs(
            orders, signatures
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(orders, signatures).estimateGas(
            tx_params.as_dict()
        )


class GetSimulatedOrderTransferResultsMethod(ContractMethod):
    """Various interfaces to the getSimulatedOrderTransferResults method."""

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
        taker_address: str,
        taker_asset_fill_amount: int,
    ):
        """Validate the inputs to the getSimulatedOrderTransferResults method."""
        self.validator.assert_valid(
            method_name="getSimulatedOrderTransferResults",
            parameter_name="order",
            argument_value=order,
        )
        self.validator.assert_valid(
            method_name="getSimulatedOrderTransferResults",
            parameter_name="takerAddress",
            argument_value=taker_address,
        )
        taker_address = self.validate_and_checksum_address(taker_address)
        self.validator.assert_valid(
            method_name="getSimulatedOrderTransferResults",
            parameter_name="takerAssetFillAmount",
            argument_value=taker_asset_fill_amount,
        )
        # safeguard against fractional inputs
        taker_asset_fill_amount = int(taker_asset_fill_amount)
        return (order, taker_address, taker_asset_fill_amount)

    def call(
        self,
        order: LibOrderOrder,
        taker_address: str,
        taker_asset_fill_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        Simulates all of the transfers within an order and returns the index of
        the first failed transfer.

        :param order: The order to simulate transfers for.
        :param takerAddress: The address of the taker that will fill the order.
        :param takerAssetFillAmount: The amount of takerAsset that the taker
            wished to fill.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            order,
            taker_address,
            taker_asset_fill_amount,
        ) = self.validate_and_normalize_inputs(
            order, taker_address, taker_asset_fill_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            order, taker_address, taker_asset_fill_amount
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        order: LibOrderOrder,
        taker_address: str,
        taker_asset_fill_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Simulates all of the transfers within an order and returns the index of
        the first failed transfer.

        :param order: The order to simulate transfers for.
        :param takerAddress: The address of the taker that will fill the order.
        :param takerAssetFillAmount: The amount of takerAsset that the taker
            wished to fill.
        :param tx_params: transaction parameters
        """
        (
            order,
            taker_address,
            taker_asset_fill_amount,
        ) = self.validate_and_normalize_inputs(
            order, taker_address, taker_asset_fill_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_address, taker_asset_fill_amount
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        order: LibOrderOrder,
        taker_address: str,
        taker_asset_fill_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            order,
            taker_address,
            taker_asset_fill_amount,
        ) = self.validate_and_normalize_inputs(
            order, taker_address, taker_asset_fill_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_address, taker_asset_fill_amount
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        order: LibOrderOrder,
        taker_address: str,
        taker_asset_fill_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            order,
            taker_address,
            taker_asset_fill_amount,
        ) = self.validate_and_normalize_inputs(
            order, taker_address, taker_asset_fill_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            order, taker_address, taker_asset_fill_amount
        ).estimateGas(tx_params.as_dict())


class GetSimulatedOrdersTransferResultsMethod(ContractMethod):
    """Various interfaces to the getSimulatedOrdersTransferResults method."""

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
        taker_addresses: List[str],
        taker_asset_fill_amounts: List[int],
    ):
        """Validate the inputs to the getSimulatedOrdersTransferResults method."""
        self.validator.assert_valid(
            method_name="getSimulatedOrdersTransferResults",
            parameter_name="orders",
            argument_value=orders,
        )
        self.validator.assert_valid(
            method_name="getSimulatedOrdersTransferResults",
            parameter_name="takerAddresses",
            argument_value=taker_addresses,
        )
        self.validator.assert_valid(
            method_name="getSimulatedOrdersTransferResults",
            parameter_name="takerAssetFillAmounts",
            argument_value=taker_asset_fill_amounts,
        )
        return (orders, taker_addresses, taker_asset_fill_amounts)

    def call(
        self,
        orders: List[LibOrderOrder],
        taker_addresses: List[str],
        taker_asset_fill_amounts: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        Simulates all of the transfers for each given order and returns the
        indices of each first failed transfer.

        :param orders: Array of orders to individually simulate transfers for.
        :param takerAddresses: Array of addresses of takers that will fill each
            order.
        :param takerAssetFillAmounts: Array of amounts of takerAsset that will
            be filled for each order.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            orders,
            taker_addresses,
            taker_asset_fill_amounts,
        ) = self.validate_and_normalize_inputs(
            orders, taker_addresses, taker_asset_fill_amounts
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            orders, taker_addresses, taker_asset_fill_amounts
        ).call(tx_params.as_dict())
        return [int(element) for element in returned]

    def send_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_addresses: List[str],
        taker_asset_fill_amounts: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Simulates all of the transfers for each given order and returns the
        indices of each first failed transfer.

        :param orders: Array of orders to individually simulate transfers for.
        :param takerAddresses: Array of addresses of takers that will fill each
            order.
        :param takerAssetFillAmounts: Array of amounts of takerAsset that will
            be filled for each order.
        :param tx_params: transaction parameters
        """
        (
            orders,
            taker_addresses,
            taker_asset_fill_amounts,
        ) = self.validate_and_normalize_inputs(
            orders, taker_addresses, taker_asset_fill_amounts
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_addresses, taker_asset_fill_amounts
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        orders: List[LibOrderOrder],
        taker_addresses: List[str],
        taker_asset_fill_amounts: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            orders,
            taker_addresses,
            taker_asset_fill_amounts,
        ) = self.validate_and_normalize_inputs(
            orders, taker_addresses, taker_asset_fill_amounts
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_addresses, taker_asset_fill_amounts
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        orders: List[LibOrderOrder],
        taker_addresses: List[str],
        taker_asset_fill_amounts: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            orders,
            taker_addresses,
            taker_asset_fill_amounts,
        ) = self.validate_and_normalize_inputs(
            orders, taker_addresses, taker_asset_fill_amounts
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            orders, taker_addresses, taker_asset_fill_amounts
        ).estimateGas(tx_params.as_dict())


class GetTransactionHashMethod(ContractMethod):
    """Various interfaces to the getTransactionHash method."""

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
        chain_id: int,
        exchange: str,
    ):
        """Validate the inputs to the getTransactionHash method."""
        self.validator.assert_valid(
            method_name="getTransactionHash",
            parameter_name="transaction",
            argument_value=transaction,
        )
        self.validator.assert_valid(
            method_name="getTransactionHash",
            parameter_name="chainId",
            argument_value=chain_id,
        )
        # safeguard against fractional inputs
        chain_id = int(chain_id)
        self.validator.assert_valid(
            method_name="getTransactionHash",
            parameter_name="exchange",
            argument_value=exchange,
        )
        exchange = self.validate_and_checksum_address(exchange)
        return (transaction, chain_id, exchange)

    def call(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        chain_id: int,
        exchange: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (transaction, chain_id, exchange) = self.validate_and_normalize_inputs(
            transaction, chain_id, exchange
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            transaction, chain_id, exchange
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(
        self,
        transaction: LibZeroExTransactionZeroExTransaction,
        chain_id: int,
        exchange: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction, chain_id, exchange) = self.validate_and_normalize_inputs(
            transaction, chain_id, exchange
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            transaction, chain_id, exchange
        ).estimateGas(tx_params.as_dict())


class GetTransferableAssetAmountMethod(ContractMethod):
    """Various interfaces to the getTransferableAssetAmount method."""

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
        self, owner_address: str, asset_data: Union[bytes, str]
    ):
        """Validate the inputs to the getTransferableAssetAmount method."""
        self.validator.assert_valid(
            method_name="getTransferableAssetAmount",
            parameter_name="ownerAddress",
            argument_value=owner_address,
        )
        owner_address = self.validate_and_checksum_address(owner_address)
        self.validator.assert_valid(
            method_name="getTransferableAssetAmount",
            parameter_name="assetData",
            argument_value=asset_data,
        )
        return (owner_address, asset_data)

    def call(
        self,
        owner_address: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        Gets the amount of an asset transferable by the owner.

        :param assetData: Description of tokens, per the AssetProxy contract
            specification.
        :param ownerAddress: Address of the owner of the asset.
        :param tx_params: transaction parameters
        :returns: The amount of the asset tranferable by the owner. NOTE: If
            the `assetData` encodes data for multiple assets, the
            `transferableAssetAmount` will represent the amount of times the
            entire `assetData` can be transferred. To calculate the total
            individual transferable amounts, this scaled `transferableAmount`
            must be multiplied by the individual asset amounts located within
            the `assetData`.
        """
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner_address, asset_data).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self,
        owner_address: str,
        asset_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner_address, asset_data) = self.validate_and_normalize_inputs(
            owner_address, asset_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner_address, asset_data).estimateGas(
            tx_params.as_dict()
        )


class RevertIfInvalidAssetDataMethod(ContractMethod):
    """Various interfaces to the revertIfInvalidAssetData method."""

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
        """Validate the inputs to the revertIfInvalidAssetData method."""
        self.validator.assert_valid(
            method_name="revertIfInvalidAssetData",
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

        :param tx_params: transaction parameters

        """
        (asset_data) = self.validate_and_normalize_inputs(asset_data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(asset_data).call(tx_params.as_dict())

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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DevUtils:
    """Wrapper class for DevUtils Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    eip712_exchange_domain_hash: Eip712ExchangeDomainHashMethod
    """Constructor-initialized instance of
    :class:`Eip712ExchangeDomainHashMethod`.
    """

    decode_asset_proxy_dispatch_error: DecodeAssetProxyDispatchErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeAssetProxyDispatchErrorMethod`.
    """

    decode_asset_proxy_exists_error: DecodeAssetProxyExistsErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeAssetProxyExistsErrorMethod`.
    """

    decode_asset_proxy_id: DecodeAssetProxyIdMethod
    """Constructor-initialized instance of
    :class:`DecodeAssetProxyIdMethod`.
    """

    decode_asset_proxy_transfer_error: DecodeAssetProxyTransferErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeAssetProxyTransferErrorMethod`.
    """

    decode_eip1271_signature_error: DecodeEip1271SignatureErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeEip1271SignatureErrorMethod`.
    """

    decode_erc1155_asset_data: DecodeErc1155AssetDataMethod
    """Constructor-initialized instance of
    :class:`DecodeErc1155AssetDataMethod`.
    """

    decode_erc20_asset_data: DecodeErc20AssetDataMethod
    """Constructor-initialized instance of
    :class:`DecodeErc20AssetDataMethod`.
    """

    decode_erc721_asset_data: DecodeErc721AssetDataMethod
    """Constructor-initialized instance of
    :class:`DecodeErc721AssetDataMethod`.
    """

    decode_exchange_invalid_context_error: DecodeExchangeInvalidContextErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeExchangeInvalidContextErrorMethod`.
    """

    decode_fill_error: DecodeFillErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeFillErrorMethod`.
    """

    decode_incomplete_fill_error: DecodeIncompleteFillErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeIncompleteFillErrorMethod`.
    """

    decode_multi_asset_data: DecodeMultiAssetDataMethod
    """Constructor-initialized instance of
    :class:`DecodeMultiAssetDataMethod`.
    """

    decode_negative_spread_error: DecodeNegativeSpreadErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeNegativeSpreadErrorMethod`.
    """

    decode_order_epoch_error: DecodeOrderEpochErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeOrderEpochErrorMethod`.
    """

    decode_order_status_error: DecodeOrderStatusErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeOrderStatusErrorMethod`.
    """

    decode_signature_error: DecodeSignatureErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeSignatureErrorMethod`.
    """

    decode_signature_validator_not_approved_error: DecodeSignatureValidatorNotApprovedErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeSignatureValidatorNotApprovedErrorMethod`.
    """

    decode_signature_wallet_error: DecodeSignatureWalletErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeSignatureWalletErrorMethod`.
    """

    decode_static_call_asset_data: DecodeStaticCallAssetDataMethod
    """Constructor-initialized instance of
    :class:`DecodeStaticCallAssetDataMethod`.
    """

    decode_transaction_error: DecodeTransactionErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeTransactionErrorMethod`.
    """

    decode_transaction_execution_error: DecodeTransactionExecutionErrorMethod
    """Constructor-initialized instance of
    :class:`DecodeTransactionExecutionErrorMethod`.
    """

    decode_zero_ex_transaction_data: DecodeZeroExTransactionDataMethod
    """Constructor-initialized instance of
    :class:`DecodeZeroExTransactionDataMethod`.
    """

    encode_erc1155_asset_data: EncodeErc1155AssetDataMethod
    """Constructor-initialized instance of
    :class:`EncodeErc1155AssetDataMethod`.
    """

    encode_erc20_asset_data: EncodeErc20AssetDataMethod
    """Constructor-initialized instance of
    :class:`EncodeErc20AssetDataMethod`.
    """

    encode_erc721_asset_data: EncodeErc721AssetDataMethod
    """Constructor-initialized instance of
    :class:`EncodeErc721AssetDataMethod`.
    """

    encode_multi_asset_data: EncodeMultiAssetDataMethod
    """Constructor-initialized instance of
    :class:`EncodeMultiAssetDataMethod`.
    """

    encode_static_call_asset_data: EncodeStaticCallAssetDataMethod
    """Constructor-initialized instance of
    :class:`EncodeStaticCallAssetDataMethod`.
    """

    get_asset_proxy_allowance: GetAssetProxyAllowanceMethod
    """Constructor-initialized instance of
    :class:`GetAssetProxyAllowanceMethod`.
    """

    get_balance: GetBalanceMethod
    """Constructor-initialized instance of
    :class:`GetBalanceMethod`.
    """

    get_balance_and_asset_proxy_allowance: GetBalanceAndAssetProxyAllowanceMethod
    """Constructor-initialized instance of
    :class:`GetBalanceAndAssetProxyAllowanceMethod`.
    """

    get_batch_asset_proxy_allowances: GetBatchAssetProxyAllowancesMethod
    """Constructor-initialized instance of
    :class:`GetBatchAssetProxyAllowancesMethod`.
    """

    get_batch_balances: GetBatchBalancesMethod
    """Constructor-initialized instance of
    :class:`GetBatchBalancesMethod`.
    """

    get_batch_balances_and_asset_proxy_allowances: GetBatchBalancesAndAssetProxyAllowancesMethod
    """Constructor-initialized instance of
    :class:`GetBatchBalancesAndAssetProxyAllowancesMethod`.
    """

    get_eth_balances: GetEthBalancesMethod
    """Constructor-initialized instance of
    :class:`GetEthBalancesMethod`.
    """

    get_order_hash: GetOrderHashMethod
    """Constructor-initialized instance of
    :class:`GetOrderHashMethod`.
    """

    get_order_relevant_state: GetOrderRelevantStateMethod
    """Constructor-initialized instance of
    :class:`GetOrderRelevantStateMethod`.
    """

    get_order_relevant_states: GetOrderRelevantStatesMethod
    """Constructor-initialized instance of
    :class:`GetOrderRelevantStatesMethod`.
    """

    get_simulated_order_transfer_results: GetSimulatedOrderTransferResultsMethod
    """Constructor-initialized instance of
    :class:`GetSimulatedOrderTransferResultsMethod`.
    """

    get_simulated_orders_transfer_results: GetSimulatedOrdersTransferResultsMethod
    """Constructor-initialized instance of
    :class:`GetSimulatedOrdersTransferResultsMethod`.
    """

    get_transaction_hash: GetTransactionHashMethod
    """Constructor-initialized instance of
    :class:`GetTransactionHashMethod`.
    """

    get_transferable_asset_amount: GetTransferableAssetAmountMethod
    """Constructor-initialized instance of
    :class:`GetTransferableAssetAmountMethod`.
    """

    revert_if_invalid_asset_data: RevertIfInvalidAssetDataMethod
    """Constructor-initialized instance of
    :class:`RevertIfInvalidAssetDataMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: DevUtilsValidator = None,
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
            validator = DevUtilsValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=DevUtils.abi()
        ).functions

        self.eip712_exchange_domain_hash = Eip712ExchangeDomainHashMethod(
            web3_or_provider,
            contract_address,
            functions.EIP712_EXCHANGE_DOMAIN_HASH,
        )

        self.decode_asset_proxy_dispatch_error = DecodeAssetProxyDispatchErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeAssetProxyDispatchError,
            validator,
        )

        self.decode_asset_proxy_exists_error = DecodeAssetProxyExistsErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeAssetProxyExistsError,
            validator,
        )

        self.decode_asset_proxy_id = DecodeAssetProxyIdMethod(
            web3_or_provider,
            contract_address,
            functions.decodeAssetProxyId,
            validator,
        )

        self.decode_asset_proxy_transfer_error = DecodeAssetProxyTransferErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeAssetProxyTransferError,
            validator,
        )

        self.decode_eip1271_signature_error = DecodeEip1271SignatureErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeEIP1271SignatureError,
            validator,
        )

        self.decode_erc1155_asset_data = DecodeErc1155AssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.decodeERC1155AssetData,
            validator,
        )

        self.decode_erc20_asset_data = DecodeErc20AssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.decodeERC20AssetData,
            validator,
        )

        self.decode_erc721_asset_data = DecodeErc721AssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.decodeERC721AssetData,
            validator,
        )

        self.decode_exchange_invalid_context_error = DecodeExchangeInvalidContextErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeExchangeInvalidContextError,
            validator,
        )

        self.decode_fill_error = DecodeFillErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeFillError,
            validator,
        )

        self.decode_incomplete_fill_error = DecodeIncompleteFillErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeIncompleteFillError,
            validator,
        )

        self.decode_multi_asset_data = DecodeMultiAssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.decodeMultiAssetData,
            validator,
        )

        self.decode_negative_spread_error = DecodeNegativeSpreadErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeNegativeSpreadError,
            validator,
        )

        self.decode_order_epoch_error = DecodeOrderEpochErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeOrderEpochError,
            validator,
        )

        self.decode_order_status_error = DecodeOrderStatusErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeOrderStatusError,
            validator,
        )

        self.decode_signature_error = DecodeSignatureErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeSignatureError,
            validator,
        )

        self.decode_signature_validator_not_approved_error = DecodeSignatureValidatorNotApprovedErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeSignatureValidatorNotApprovedError,
            validator,
        )

        self.decode_signature_wallet_error = DecodeSignatureWalletErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeSignatureWalletError,
            validator,
        )

        self.decode_static_call_asset_data = DecodeStaticCallAssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.decodeStaticCallAssetData,
            validator,
        )

        self.decode_transaction_error = DecodeTransactionErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeTransactionError,
            validator,
        )

        self.decode_transaction_execution_error = DecodeTransactionExecutionErrorMethod(
            web3_or_provider,
            contract_address,
            functions.decodeTransactionExecutionError,
            validator,
        )

        self.decode_zero_ex_transaction_data = DecodeZeroExTransactionDataMethod(
            web3_or_provider,
            contract_address,
            functions.decodeZeroExTransactionData,
            validator,
        )

        self.encode_erc1155_asset_data = EncodeErc1155AssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.encodeERC1155AssetData,
            validator,
        )

        self.encode_erc20_asset_data = EncodeErc20AssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.encodeERC20AssetData,
            validator,
        )

        self.encode_erc721_asset_data = EncodeErc721AssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.encodeERC721AssetData,
            validator,
        )

        self.encode_multi_asset_data = EncodeMultiAssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.encodeMultiAssetData,
            validator,
        )

        self.encode_static_call_asset_data = EncodeStaticCallAssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.encodeStaticCallAssetData,
            validator,
        )

        self.get_asset_proxy_allowance = GetAssetProxyAllowanceMethod(
            web3_or_provider,
            contract_address,
            functions.getAssetProxyAllowance,
            validator,
        )

        self.get_balance = GetBalanceMethod(
            web3_or_provider, contract_address, functions.getBalance, validator
        )

        self.get_balance_and_asset_proxy_allowance = GetBalanceAndAssetProxyAllowanceMethod(
            web3_or_provider,
            contract_address,
            functions.getBalanceAndAssetProxyAllowance,
            validator,
        )

        self.get_batch_asset_proxy_allowances = GetBatchAssetProxyAllowancesMethod(
            web3_or_provider,
            contract_address,
            functions.getBatchAssetProxyAllowances,
            validator,
        )

        self.get_batch_balances = GetBatchBalancesMethod(
            web3_or_provider,
            contract_address,
            functions.getBatchBalances,
            validator,
        )

        self.get_batch_balances_and_asset_proxy_allowances = GetBatchBalancesAndAssetProxyAllowancesMethod(
            web3_or_provider,
            contract_address,
            functions.getBatchBalancesAndAssetProxyAllowances,
            validator,
        )

        self.get_eth_balances = GetEthBalancesMethod(
            web3_or_provider,
            contract_address,
            functions.getEthBalances,
            validator,
        )

        self.get_order_hash = GetOrderHashMethod(
            web3_or_provider,
            contract_address,
            functions.getOrderHash,
            validator,
        )

        self.get_order_relevant_state = GetOrderRelevantStateMethod(
            web3_or_provider,
            contract_address,
            functions.getOrderRelevantState,
            validator,
        )

        self.get_order_relevant_states = GetOrderRelevantStatesMethod(
            web3_or_provider,
            contract_address,
            functions.getOrderRelevantStates,
            validator,
        )

        self.get_simulated_order_transfer_results = GetSimulatedOrderTransferResultsMethod(
            web3_or_provider,
            contract_address,
            functions.getSimulatedOrderTransferResults,
            validator,
        )

        self.get_simulated_orders_transfer_results = GetSimulatedOrdersTransferResultsMethod(
            web3_or_provider,
            contract_address,
            functions.getSimulatedOrdersTransferResults,
            validator,
        )

        self.get_transaction_hash = GetTransactionHashMethod(
            web3_or_provider,
            contract_address,
            functions.getTransactionHash,
            validator,
        )

        self.get_transferable_asset_amount = GetTransferableAssetAmountMethod(
            web3_or_provider,
            contract_address,
            functions.getTransferableAssetAmount,
            validator,
        )

        self.revert_if_invalid_asset_data = RevertIfInvalidAssetDataMethod(
            web3_or_provider,
            contract_address,
            functions.revertIfInvalidAssetData,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_exchange","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"EIP712_EXCHANGE_DOMAIN_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeAssetProxyDispatchError","outputs":[{"internalType":"enum LibExchangeRichErrors.AssetProxyDispatchErrorCodes","name":"errorCode","type":"uint8"},{"internalType":"bytes32","name":"orderHash","type":"bytes32"},{"internalType":"bytes","name":"assetData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeAssetProxyExistsError","outputs":[{"internalType":"bytes4","name":"assetProxyId","type":"bytes4"},{"internalType":"address","name":"assetProxyAddress","type":"address"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"decodeAssetProxyId","outputs":[{"internalType":"bytes4","name":"assetProxyId","type":"bytes4"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeAssetProxyTransferError","outputs":[{"internalType":"bytes32","name":"orderHash","type":"bytes32"},{"internalType":"bytes","name":"assetData","type":"bytes"},{"internalType":"bytes","name":"errorData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeEIP1271SignatureError","outputs":[{"internalType":"address","name":"verifyingContractAddress","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes","name":"errorData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"decodeERC1155AssetData","outputs":[{"internalType":"bytes4","name":"assetProxyId","type":"bytes4"},{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"tokenValues","type":"uint256[]"},{"internalType":"bytes","name":"callbackData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"decodeERC20AssetData","outputs":[{"internalType":"bytes4","name":"assetProxyId","type":"bytes4"},{"internalType":"address","name":"tokenAddress","type":"address"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"decodeERC721AssetData","outputs":[{"internalType":"bytes4","name":"assetProxyId","type":"bytes4"},{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeExchangeInvalidContextError","outputs":[{"internalType":"enum LibExchangeRichErrors.ExchangeContextErrorCodes","name":"errorCode","type":"uint8"},{"internalType":"bytes32","name":"orderHash","type":"bytes32"},{"internalType":"address","name":"contextAddress","type":"address"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeFillError","outputs":[{"internalType":"enum LibExchangeRichErrors.FillErrorCodes","name":"errorCode","type":"uint8"},{"internalType":"bytes32","name":"orderHash","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeIncompleteFillError","outputs":[{"internalType":"enum LibExchangeRichErrors.IncompleteFillErrorCode","name":"errorCode","type":"uint8"},{"internalType":"uint256","name":"expectedAssetFillAmount","type":"uint256"},{"internalType":"uint256","name":"actualAssetFillAmount","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"decodeMultiAssetData","outputs":[{"internalType":"bytes4","name":"assetProxyId","type":"bytes4"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes[]","name":"nestedAssetData","type":"bytes[]"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeNegativeSpreadError","outputs":[{"internalType":"bytes32","name":"leftOrderHash","type":"bytes32"},{"internalType":"bytes32","name":"rightOrderHash","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeOrderEpochError","outputs":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"orderSenderAddress","type":"address"},{"internalType":"uint256","name":"currentEpoch","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeOrderStatusError","outputs":[{"internalType":"bytes32","name":"orderHash","type":"bytes32"},{"internalType":"enum LibOrder.OrderStatus","name":"orderStatus","type":"uint8"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeSignatureError","outputs":[{"internalType":"enum LibExchangeRichErrors.SignatureErrorCodes","name":"errorCode","type":"uint8"},{"internalType":"bytes32","name":"hash","type":"bytes32"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"signature","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeSignatureValidatorNotApprovedError","outputs":[{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"address","name":"validatorAddress","type":"address"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeSignatureWalletError","outputs":[{"internalType":"bytes32","name":"hash","type":"bytes32"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes","name":"errorData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"decodeStaticCallAssetData","outputs":[{"internalType":"bytes4","name":"assetProxyId","type":"bytes4"},{"internalType":"address","name":"staticCallTargetAddress","type":"address"},{"internalType":"bytes","name":"staticCallData","type":"bytes"},{"internalType":"bytes32","name":"expectedReturnDataHash","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeTransactionError","outputs":[{"internalType":"enum LibExchangeRichErrors.TransactionErrorCodes","name":"errorCode","type":"uint8"},{"internalType":"bytes32","name":"transactionHash","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"encoded","type":"bytes"}],"name":"decodeTransactionExecutionError","outputs":[{"internalType":"bytes32","name":"transactionHash","type":"bytes32"},{"internalType":"bytes","name":"errorData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"transactionData","type":"bytes"}],"name":"decodeZeroExTransactionData","outputs":[{"internalType":"string","name":"functionName","type":"string"},{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"uint256[]","name":"takerAssetFillAmounts","type":"uint256[]"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"},{"internalType":"uint256[]","name":"tokenValues","type":"uint256[]"},{"internalType":"bytes","name":"callbackData","type":"bytes"}],"name":"encodeERC1155AssetData","outputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"}],"name":"encodeERC20AssetData","outputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"encodeERC721AssetData","outputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes[]","name":"nestedAssetData","type":"bytes[]"}],"name":"encodeMultiAssetData","outputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"staticCallTargetAddress","type":"address"},{"internalType":"bytes","name":"staticCallData","type":"bytes"},{"internalType":"bytes32","name":"expectedReturnDataHash","type":"bytes32"}],"name":"encodeStaticCallAssetData","outputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"ownerAddress","type":"address"},{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"getAssetProxyAllowance","outputs":[{"internalType":"uint256","name":"allowance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"ownerAddress","type":"address"},{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"getBalance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"ownerAddress","type":"address"},{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"getBalanceAndAssetProxyAllowance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"allowance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"ownerAddress","type":"address"},{"internalType":"bytes[]","name":"assetData","type":"bytes[]"}],"name":"getBatchAssetProxyAllowances","outputs":[{"internalType":"uint256[]","name":"allowances","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"ownerAddress","type":"address"},{"internalType":"bytes[]","name":"assetData","type":"bytes[]"}],"name":"getBatchBalances","outputs":[{"internalType":"uint256[]","name":"balances","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"ownerAddress","type":"address"},{"internalType":"bytes[]","name":"assetData","type":"bytes[]"}],"name":"getBatchBalancesAndAssetProxyAllowances","outputs":[{"internalType":"uint256[]","name":"balances","type":"uint256[]"},{"internalType":"uint256[]","name":"allowances","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address[]","name":"addresses","type":"address[]"}],"name":"getEthBalances","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"order","type":"tuple"},{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"address","name":"exchange","type":"address"}],"name":"getOrderHash","outputs":[{"internalType":"bytes32","name":"orderHash","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"order","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"getOrderRelevantState","outputs":[{"components":[{"internalType":"uint8","name":"orderStatus","type":"uint8"},{"internalType":"bytes32","name":"orderHash","type":"bytes32"},{"internalType":"uint256","name":"orderTakerAssetFilledAmount","type":"uint256"}],"internalType":"struct LibOrder.OrderInfo","name":"orderInfo","type":"tuple"},{"internalType":"uint256","name":"fillableTakerAssetAmount","type":"uint256"},{"internalType":"bool","name":"isValidSignature","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"bytes[]","name":"signatures","type":"bytes[]"}],"name":"getOrderRelevantStates","outputs":[{"components":[{"internalType":"uint8","name":"orderStatus","type":"uint8"},{"internalType":"bytes32","name":"orderHash","type":"bytes32"},{"internalType":"uint256","name":"orderTakerAssetFilledAmount","type":"uint256"}],"internalType":"struct LibOrder.OrderInfo[]","name":"ordersInfo","type":"tuple[]"},{"internalType":"uint256[]","name":"fillableTakerAssetAmounts","type":"uint256[]"},{"internalType":"bool[]","name":"isValidSignature","type":"bool[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order","name":"order","type":"tuple"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"uint256","name":"takerAssetFillAmount","type":"uint256"}],"name":"getSimulatedOrderTransferResults","outputs":[{"internalType":"enum OrderTransferSimulationUtils.OrderTransferResults","name":"orderTransferResults","type":"uint8"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"takerAddress","type":"address"},{"internalType":"address","name":"feeRecipientAddress","type":"address"},{"internalType":"address","name":"senderAddress","type":"address"},{"internalType":"uint256","name":"makerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"takerAssetAmount","type":"uint256"},{"internalType":"uint256","name":"makerFee","type":"uint256"},{"internalType":"uint256","name":"takerFee","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"bytes","name":"makerAssetData","type":"bytes"},{"internalType":"bytes","name":"takerAssetData","type":"bytes"},{"internalType":"bytes","name":"makerFeeAssetData","type":"bytes"},{"internalType":"bytes","name":"takerFeeAssetData","type":"bytes"}],"internalType":"struct LibOrder.Order[]","name":"orders","type":"tuple[]"},{"internalType":"address[]","name":"takerAddresses","type":"address[]"},{"internalType":"uint256[]","name":"takerAssetFillAmounts","type":"uint256[]"}],"name":"getSimulatedOrdersTransferResults","outputs":[{"internalType":"enum OrderTransferSimulationUtils.OrderTransferResults[]","name":"orderTransferResults","type":"uint8[]"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"components":[{"internalType":"uint256","name":"salt","type":"uint256"},{"internalType":"uint256","name":"expirationTimeSeconds","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"},{"internalType":"address","name":"signerAddress","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct LibZeroExTransaction.ZeroExTransaction","name":"transaction","type":"tuple"},{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"address","name":"exchange","type":"address"}],"name":"getTransactionHash","outputs":[{"internalType":"bytes32","name":"transactionHash","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"ownerAddress","type":"address"},{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"getTransferableAssetAmount","outputs":[{"internalType":"uint256","name":"transferableAssetAmount","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"assetData","type":"bytes"}],"name":"revertIfInvalidAssetData","outputs":[],"payable":false,"stateMutability":"pure","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
