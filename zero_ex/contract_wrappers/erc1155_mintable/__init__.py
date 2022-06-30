"""Generated wrapper for ERC1155Mintable Solidity contract."""

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
# constructor for ERC1155Mintable below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ERC1155MintableValidator,
    )
except ImportError:

    class ERC1155MintableValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class Erc1155BatchReceivedMethod(ContractMethod):
    """Various interfaces to the ERC1155_BATCH_RECEIVED method."""

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


class Erc1155ReceivedMethod(ContractMethod):
    """Various interfaces to the ERC1155_RECEIVED method."""

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


class BalanceOfMethod(ContractMethod):
    """Various interfaces to the balanceOf method."""

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

    def validate_and_normalize_inputs(self, owner: str, _id: int):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name="balanceOf",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name="balanceOf", parameter_name="id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (owner, _id)

    def call(
        self, owner: str, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param id: ID of the Token
        :param owner: The address of the token holder
        :param tx_params: transaction parameters
        :returns: The _owner's balance of the Token type requested
        """
        (owner, _id) = self.validate_and_normalize_inputs(owner, _id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, _id).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self, owner: str, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner, _id) = self.validate_and_normalize_inputs(owner, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, _id).estimateGas(
            tx_params.as_dict()
        )


class BalanceOfBatchMethod(ContractMethod):
    """Various interfaces to the balanceOfBatch method."""

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

    def validate_and_normalize_inputs(self, owners: List[str], ids: List[int]):
        """Validate the inputs to the balanceOfBatch method."""
        self.validator.assert_valid(
            method_name="balanceOfBatch",
            parameter_name="owners",
            argument_value=owners,
        )
        self.validator.assert_valid(
            method_name="balanceOfBatch",
            parameter_name="ids",
            argument_value=ids,
        )
        return (owners, ids)

    def call(
        self,
        owners: List[str],
        ids: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        :param ids: ID of the Tokens
        :param owners: The addresses of the token holders
        :param tx_params: transaction parameters
        :returns: The _owner's balance of the Token types requested
        """
        (owners, ids) = self.validate_and_normalize_inputs(owners, ids)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owners, ids).call(
            tx_params.as_dict()
        )
        return [int(element) for element in returned]

    def estimate_gas(
        self,
        owners: List[str],
        ids: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (owners, ids) = self.validate_and_normalize_inputs(owners, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owners, ids).estimateGas(
            tx_params.as_dict()
        )


class CreateMethod(ContractMethod):
    """Various interfaces to the create method."""

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

    def validate_and_normalize_inputs(self, uri: str, is_nf: bool):
        """Validate the inputs to the create method."""
        self.validator.assert_valid(
            method_name="create", parameter_name="uri", argument_value=uri,
        )
        self.validator.assert_valid(
            method_name="create", parameter_name="isNF", argument_value=is_nf,
        )
        return (uri, is_nf)

    def call(
        self, uri: str, is_nf: bool, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        creates a new token

        :param isNF: is non-fungible token
        :param uri: URI of token
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri, is_nf) = self.validate_and_normalize_inputs(uri, is_nf)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(uri, is_nf).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, uri: str, is_nf: bool, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        creates a new token

        :param isNF: is non-fungible token
        :param uri: URI of token
        :param tx_params: transaction parameters
        """
        (uri, is_nf) = self.validate_and_normalize_inputs(uri, is_nf)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, uri: str, is_nf: bool, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri, is_nf) = self.validate_and_normalize_inputs(uri, is_nf)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, uri: str, is_nf: bool, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (uri, is_nf) = self.validate_and_normalize_inputs(uri, is_nf)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri, is_nf).estimateGas(
            tx_params.as_dict()
        )


class CreateWithTypeMethod(ContractMethod):
    """Various interfaces to the createWithType method."""

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

    def validate_and_normalize_inputs(self, _type: int, uri: str):
        """Validate the inputs to the createWithType method."""
        self.validator.assert_valid(
            method_name="createWithType",
            parameter_name="type_",
            argument_value=_type,
        )
        # safeguard against fractional inputs
        _type = int(_type)
        self.validator.assert_valid(
            method_name="createWithType",
            parameter_name="uri",
            argument_value=uri,
        )
        return (_type, uri)

    def call(
        self, _type: int, uri: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        creates a new token

        :param type_: of token
        :param uri: URI of token
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_type, uri) = self.validate_and_normalize_inputs(_type, uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_type, uri).call(tx_params.as_dict())

    def send_transaction(
        self, _type: int, uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        creates a new token

        :param type_: of token
        :param uri: URI of token
        :param tx_params: transaction parameters
        """
        (_type, uri) = self.validate_and_normalize_inputs(_type, uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, uri).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _type: int, uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_type, uri) = self.validate_and_normalize_inputs(_type, uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _type: int, uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_type, uri) = self.validate_and_normalize_inputs(_type, uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, uri).estimateGas(
            tx_params.as_dict()
        )


class CreatorsMethod(ContractMethod):
    """Various interfaces to the creators method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the creators method."""
        self.validator.assert_valid(
            method_name="creators",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class GetNonFungibleBaseTypeMethod(ContractMethod):
    """Various interfaces to the getNonFungibleBaseType method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the getNonFungibleBaseType method."""
        self.validator.assert_valid(
            method_name="getNonFungibleBaseType",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        Returns base type of non-fungible token

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class GetNonFungibleIndexMethod(ContractMethod):
    """Various interfaces to the getNonFungibleIndex method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the getNonFungibleIndex method."""
        self.validator.assert_valid(
            method_name="getNonFungibleIndex",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        Returns index of non-fungible token

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class IsApprovedForAllMethod(ContractMethod):
    """Various interfaces to the isApprovedForAll method."""

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

    def validate_and_normalize_inputs(self, owner: str, operator: str):
        """Validate the inputs to the isApprovedForAll method."""
        self.validator.assert_valid(
            method_name="isApprovedForAll",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name="isApprovedForAll",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (owner, operator)

    def call(
        self, owner: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param operator: Address of authorized operator
        :param owner: The owner of the Tokens
        :param tx_params: transaction parameters
        :returns: True if the operator is approved, false if not
        """
        (owner, operator) = self.validate_and_normalize_inputs(owner, operator)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, operator).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def estimate_gas(
        self, owner: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner, operator) = self.validate_and_normalize_inputs(owner, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, operator).estimateGas(
            tx_params.as_dict()
        )


class IsFungibleMethod(ContractMethod):
    """Various interfaces to the isFungible method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isFungible method."""
        self.validator.assert_valid(
            method_name="isFungible", parameter_name="id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        Returns true if token is fungible

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class IsNonFungibleMethod(ContractMethod):
    """Various interfaces to the isNonFungible method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungible method."""
        self.validator.assert_valid(
            method_name="isNonFungible",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        Returns true if token is non-fungible

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class IsNonFungibleBaseTypeMethod(ContractMethod):
    """Various interfaces to the isNonFungibleBaseType method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungibleBaseType method."""
        self.validator.assert_valid(
            method_name="isNonFungibleBaseType",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        Returns true if input is base-type of a non-fungible token

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class IsNonFungibleItemMethod(ContractMethod):
    """Various interfaces to the isNonFungibleItem method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the isNonFungibleItem method."""
        self.validator.assert_valid(
            method_name="isNonFungibleItem",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        Returns true if input is a non-fungible token

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class MaxIndexMethod(ContractMethod):
    """Various interfaces to the maxIndex method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the maxIndex method."""
        self.validator.assert_valid(
            method_name="maxIndex",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class MintFungibleMethod(ContractMethod):
    """Various interfaces to the mintFungible method."""

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
        self, _id: int, to: List[str], quantities: List[int]
    ):
        """Validate the inputs to the mintFungible method."""
        self.validator.assert_valid(
            method_name="mintFungible",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name="mintFungible", parameter_name="to", argument_value=to,
        )
        self.validator.assert_valid(
            method_name="mintFungible",
            parameter_name="quantities",
            argument_value=quantities,
        )
        return (_id, to, quantities)

    def call(
        self,
        _id: int,
        to: List[str],
        quantities: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        mints fungible tokens

        :param id: token type
        :param quantities: amounts of minted tokens
        :param to: beneficiaries of minted tokens
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id, to, quantities) = self.validate_and_normalize_inputs(
            _id, to, quantities
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_id, to, quantities).call(tx_params.as_dict())

    def send_transaction(
        self,
        _id: int,
        to: List[str],
        quantities: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        mints fungible tokens

        :param id: token type
        :param quantities: amounts of minted tokens
        :param to: beneficiaries of minted tokens
        :param tx_params: transaction parameters
        """
        (_id, to, quantities) = self.validate_and_normalize_inputs(
            _id, to, quantities
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id, to, quantities).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _id: int,
        to: List[str],
        quantities: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id, to, quantities) = self.validate_and_normalize_inputs(
            _id, to, quantities
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id, to, quantities).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _id: int,
        to: List[str],
        quantities: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id, to, quantities) = self.validate_and_normalize_inputs(
            _id, to, quantities
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id, to, quantities).estimateGas(
            tx_params.as_dict()
        )


class MintNonFungibleMethod(ContractMethod):
    """Various interfaces to the mintNonFungible method."""

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

    def validate_and_normalize_inputs(self, _type: int, to: List[str]):
        """Validate the inputs to the mintNonFungible method."""
        self.validator.assert_valid(
            method_name="mintNonFungible",
            parameter_name="type_",
            argument_value=_type,
        )
        # safeguard against fractional inputs
        _type = int(_type)
        self.validator.assert_valid(
            method_name="mintNonFungible",
            parameter_name="to",
            argument_value=to,
        )
        return (_type, to)

    def call(
        self, _type: int, to: List[str], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        mints a non-fungible token

        :param to: beneficiaries of minted tokens
        :param type_: token type
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_type, to) = self.validate_and_normalize_inputs(_type, to)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_type, to).call(tx_params.as_dict())

    def send_transaction(
        self, _type: int, to: List[str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        mints a non-fungible token

        :param to: beneficiaries of minted tokens
        :param type_: token type
        :param tx_params: transaction parameters
        """
        (_type, to) = self.validate_and_normalize_inputs(_type, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, to).transact(tx_params.as_dict())

    def build_transaction(
        self, _type: int, to: List[str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_type, to) = self.validate_and_normalize_inputs(_type, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, to).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _type: int, to: List[str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_type, to) = self.validate_and_normalize_inputs(_type, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, to).estimateGas(
            tx_params.as_dict()
        )


class OwnerOfMethod(ContractMethod):
    """Various interfaces to the ownerOf method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the ownerOf method."""
        self.validator.assert_valid(
            method_name="ownerOf", parameter_name="id", argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        returns owner of a non-fungible token

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class SafeBatchTransferFromMethod(ContractMethod):
    """Various interfaces to the safeBatchTransferFrom method."""

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
        _from: str,
        to: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
    ):
        """Validate the inputs to the safeBatchTransferFrom method."""
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="ids",
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="values",
            argument_value=values,
        )
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="data",
            argument_value=data,
        )
        return (_from, to, ids, values, data)

    def call(
        self,
        _from: str,
        to: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        MUST emit TransferBatch event on success. Caller must be approved to
        manage the _from account's tokens (see isApprovedForAll). MUST throw if
        `_to` is the zero address. MUST throw if length of `_ids` is not the
        same as length of `_values`. MUST throw if any of the balance of sender
        for token `_ids` is lower than the respective `_values` sent. MUST
        throw on any other error. When transfer is complete, this function MUST
        check if `_to` is a smart contract (code size > 0). If so, it MUST call
        `onERC1155BatchReceived` on `_to` and revert if the return value is not
        `bytes4(keccak256("onERC1155BatchReceived(address,address,uint256[],ui-
        nt256[],bytes)"))`.

        :param data: Additional data with no specified format, sent in call to
            `_to`
        :param from: Source addresses
        :param ids: IDs of each token type
        :param to: Target addresses
        :param values: Transfer amounts per token type
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, ids, values, data) = self.validate_and_normalize_inputs(
            _from, to, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, ids, values, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        to: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        MUST emit TransferBatch event on success. Caller must be approved to
        manage the _from account's tokens (see isApprovedForAll). MUST throw if
        `_to` is the zero address. MUST throw if length of `_ids` is not the
        same as length of `_values`. MUST throw if any of the balance of sender
        for token `_ids` is lower than the respective `_values` sent. MUST
        throw on any other error. When transfer is complete, this function MUST
        check if `_to` is a smart contract (code size > 0). If so, it MUST call
        `onERC1155BatchReceived` on `_to` and revert if the return value is not
        `bytes4(keccak256("onERC1155BatchReceived(address,address,uint256[],ui-
        nt256[],bytes)"))`.

        :param data: Additional data with no specified format, sent in call to
            `_to`
        :param from: Source addresses
        :param ids: IDs of each token type
        :param to: Target addresses
        :param values: Transfer amounts per token type
        :param tx_params: transaction parameters
        """
        (_from, to, ids, values, data) = self.validate_and_normalize_inputs(
            _from, to, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, ids, values, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        to: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, ids, values, data) = self.validate_and_normalize_inputs(
            _from, to, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, ids, values, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        _from: str,
        to: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, ids, values, data) = self.validate_and_normalize_inputs(
            _from, to, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, ids, values, data
        ).estimateGas(tx_params.as_dict())


class SafeTransferFromMethod(ContractMethod):
    """Various interfaces to the safeTransferFrom method."""

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
        _from: str,
        to: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
    ):
        """Validate the inputs to the safeTransferFrom method."""
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="data",
            argument_value=data,
        )
        return (_from, to, _id, value, data)

    def call(
        self,
        _from: str,
        to: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        MUST emit TransferSingle event on success. Caller must be approved to
        manage the _from account's tokens (see isApprovedForAll). MUST throw if
        `_to` is the zero address. MUST throw if balance of sender for token
        `_id` is lower than the `_value` sent. MUST throw on any other error.
        When transfer is complete, this function MUST check if `_to` is a smart
        contract (code size > 0). If so, it MUST call `onERC1155Received` on
        `_to` and revert if the return value is not `bytes4(keccak256("onERC11-
        55Received(address,address,uint256,uint256,bytes)"))`.

        :param data: Additional data with no specified format, sent in call to
            `_to`
        :param from: Source address
        :param id: ID of the token type
        :param to: Target address
        :param value: Transfer amount
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, _id, value, data) = self.validate_and_normalize_inputs(
            _from, to, _id, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, _id, value, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        to: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        MUST emit TransferSingle event on success. Caller must be approved to
        manage the _from account's tokens (see isApprovedForAll). MUST throw if
        `_to` is the zero address. MUST throw if balance of sender for token
        `_id` is lower than the `_value` sent. MUST throw on any other error.
        When transfer is complete, this function MUST check if `_to` is a smart
        contract (code size > 0). If so, it MUST call `onERC1155Received` on
        `_to` and revert if the return value is not `bytes4(keccak256("onERC11-
        55Received(address,address,uint256,uint256,bytes)"))`.

        :param data: Additional data with no specified format, sent in call to
            `_to`
        :param from: Source address
        :param id: ID of the token type
        :param to: Target address
        :param value: Transfer amount
        :param tx_params: transaction parameters
        """
        (_from, to, _id, value, data) = self.validate_and_normalize_inputs(
            _from, to, _id, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, _id, value, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        to: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, _id, value, data) = self.validate_and_normalize_inputs(
            _from, to, _id, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, _id, value, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        _from: str,
        to: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, _id, value, data) = self.validate_and_normalize_inputs(
            _from, to, _id, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, _id, value, data
        ).estimateGas(tx_params.as_dict())


class SetApprovalForAllMethod(ContractMethod):
    """Various interfaces to the setApprovalForAll method."""

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

    def validate_and_normalize_inputs(self, operator: str, approved: bool):
        """Validate the inputs to the setApprovalForAll method."""
        self.validator.assert_valid(
            method_name="setApprovalForAll",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="setApprovalForAll",
            parameter_name="approved",
            argument_value=approved,
        )
        return (operator, approved)

    def call(
        self,
        operator: str,
        approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        MUST emit the ApprovalForAll event on success.

        :param approved: True if the operator is approved, false to revoke
            approval
        :param operator: Address to add to the set of authorized operators
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator, approved) = self.validate_and_normalize_inputs(
            operator, approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator, approved).call(tx_params.as_dict())

    def send_transaction(
        self,
        operator: str,
        approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        MUST emit the ApprovalForAll event on success.

        :param approved: True if the operator is approved, false to revoke
            approval
        :param operator: Address to add to the set of authorized operators
        :param tx_params: transaction parameters
        """
        (operator, approved) = self.validate_and_normalize_inputs(
            operator, approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        operator: str,
        approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator, approved) = self.validate_and_normalize_inputs(
            operator, approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        operator: str,
        approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator, approved) = self.validate_and_normalize_inputs(
            operator, approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ERC1155Mintable:
    """Wrapper class for ERC1155Mintable Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    erc1155_batch_received: Erc1155BatchReceivedMethod
    """Constructor-initialized instance of
    :class:`Erc1155BatchReceivedMethod`.
    """

    erc1155_received: Erc1155ReceivedMethod
    """Constructor-initialized instance of
    :class:`Erc1155ReceivedMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    balance_of_batch: BalanceOfBatchMethod
    """Constructor-initialized instance of
    :class:`BalanceOfBatchMethod`.
    """

    create: CreateMethod
    """Constructor-initialized instance of
    :class:`CreateMethod`.
    """

    create_with_type: CreateWithTypeMethod
    """Constructor-initialized instance of
    :class:`CreateWithTypeMethod`.
    """

    creators: CreatorsMethod
    """Constructor-initialized instance of
    :class:`CreatorsMethod`.
    """

    get_non_fungible_base_type: GetNonFungibleBaseTypeMethod
    """Constructor-initialized instance of
    :class:`GetNonFungibleBaseTypeMethod`.
    """

    get_non_fungible_index: GetNonFungibleIndexMethod
    """Constructor-initialized instance of
    :class:`GetNonFungibleIndexMethod`.
    """

    is_approved_for_all: IsApprovedForAllMethod
    """Constructor-initialized instance of
    :class:`IsApprovedForAllMethod`.
    """

    is_fungible: IsFungibleMethod
    """Constructor-initialized instance of
    :class:`IsFungibleMethod`.
    """

    is_non_fungible: IsNonFungibleMethod
    """Constructor-initialized instance of
    :class:`IsNonFungibleMethod`.
    """

    is_non_fungible_base_type: IsNonFungibleBaseTypeMethod
    """Constructor-initialized instance of
    :class:`IsNonFungibleBaseTypeMethod`.
    """

    is_non_fungible_item: IsNonFungibleItemMethod
    """Constructor-initialized instance of
    :class:`IsNonFungibleItemMethod`.
    """

    max_index: MaxIndexMethod
    """Constructor-initialized instance of
    :class:`MaxIndexMethod`.
    """

    mint_fungible: MintFungibleMethod
    """Constructor-initialized instance of
    :class:`MintFungibleMethod`.
    """

    mint_non_fungible: MintNonFungibleMethod
    """Constructor-initialized instance of
    :class:`MintNonFungibleMethod`.
    """

    owner_of: OwnerOfMethod
    """Constructor-initialized instance of
    :class:`OwnerOfMethod`.
    """

    safe_batch_transfer_from: SafeBatchTransferFromMethod
    """Constructor-initialized instance of
    :class:`SafeBatchTransferFromMethod`.
    """

    safe_transfer_from: SafeTransferFromMethod
    """Constructor-initialized instance of
    :class:`SafeTransferFromMethod`.
    """

    set_approval_for_all: SetApprovalForAllMethod
    """Constructor-initialized instance of
    :class:`SetApprovalForAllMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ERC1155MintableValidator = None,
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
            validator = ERC1155MintableValidator(
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
            abi=ERC1155Mintable.abi(),
        ).functions

        self.erc1155_batch_received = Erc1155BatchReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.ERC1155_BATCH_RECEIVED,
        )

        self.erc1155_received = Erc1155ReceivedMethod(
            web3_or_provider, contract_address, functions.ERC1155_RECEIVED
        )

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.balance_of_batch = BalanceOfBatchMethod(
            web3_or_provider,
            contract_address,
            functions.balanceOfBatch,
            validator,
        )

        self.create = CreateMethod(
            web3_or_provider, contract_address, functions.create, validator
        )

        self.create_with_type = CreateWithTypeMethod(
            web3_or_provider,
            contract_address,
            functions.createWithType,
            validator,
        )

        self.creators = CreatorsMethod(
            web3_or_provider, contract_address, functions.creators, validator
        )

        self.get_non_fungible_base_type = GetNonFungibleBaseTypeMethod(
            web3_or_provider,
            contract_address,
            functions.getNonFungibleBaseType,
            validator,
        )

        self.get_non_fungible_index = GetNonFungibleIndexMethod(
            web3_or_provider,
            contract_address,
            functions.getNonFungibleIndex,
            validator,
        )

        self.is_approved_for_all = IsApprovedForAllMethod(
            web3_or_provider,
            contract_address,
            functions.isApprovedForAll,
            validator,
        )

        self.is_fungible = IsFungibleMethod(
            web3_or_provider, contract_address, functions.isFungible, validator
        )

        self.is_non_fungible = IsNonFungibleMethod(
            web3_or_provider,
            contract_address,
            functions.isNonFungible,
            validator,
        )

        self.is_non_fungible_base_type = IsNonFungibleBaseTypeMethod(
            web3_or_provider,
            contract_address,
            functions.isNonFungibleBaseType,
            validator,
        )

        self.is_non_fungible_item = IsNonFungibleItemMethod(
            web3_or_provider,
            contract_address,
            functions.isNonFungibleItem,
            validator,
        )

        self.max_index = MaxIndexMethod(
            web3_or_provider, contract_address, functions.maxIndex, validator
        )

        self.mint_fungible = MintFungibleMethod(
            web3_or_provider,
            contract_address,
            functions.mintFungible,
            validator,
        )

        self.mint_non_fungible = MintNonFungibleMethod(
            web3_or_provider,
            contract_address,
            functions.mintNonFungible,
            validator,
        )

        self.owner_of = OwnerOfMethod(
            web3_or_provider, contract_address, functions.ownerOf, validator
        )

        self.safe_batch_transfer_from = SafeBatchTransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.safeBatchTransferFrom,
            validator,
        )

        self.safe_transfer_from = SafeTransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.safeTransferFrom,
            validator,
        )

        self.set_approval_for_all = SetApprovalForAllMethod(
            web3_or_provider,
            contract_address,
            functions.setApprovalForAll,
            validator,
        )

    def get_approval_for_all_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ApprovalForAll event.

        :param tx_hash: hash of transaction emitting ApprovalForAll event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ERC1155Mintable.abi(),
            )
            .events.ApprovalForAll()
            .processReceipt(tx_receipt)
        )

    def get_transfer_batch_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransferBatch event.

        :param tx_hash: hash of transaction emitting TransferBatch event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ERC1155Mintable.abi(),
            )
            .events.TransferBatch()
            .processReceipt(tx_receipt)
        )

    def get_transfer_single_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransferSingle event.

        :param tx_hash: hash of transaction emitting TransferSingle event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ERC1155Mintable.abi(),
            )
            .events.TransferSingle()
            .processReceipt(tx_receipt)
        )

    def get_uri_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for URI event.

        :param tx_hash: hash of transaction emitting URI event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ERC1155Mintable.abi(),
            )
            .events.URI()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"constant":true,"inputs":[],"name":"ERC1155_BATCH_RECEIVED","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"ERC1155_RECEIVED","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address[]","name":"owners","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"balances_","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"uri","type":"string"},{"internalType":"bool","name":"isNF","type":"bool"}],"name":"create","outputs":[{"internalType":"uint256","name":"type_","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"type_","type":"uint256"},{"internalType":"string","name":"uri","type":"string"}],"name":"createWithType","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"creators","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getNonFungibleBaseType","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getNonFungibleIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isFungible","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungible","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungibleBaseType","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isNonFungibleItem","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"maxIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address[]","name":"to","type":"address[]"},{"internalType":"uint256[]","name":"quantities","type":"uint256[]"}],"name":"mintFungible","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"type_","type":"uint256"},{"internalType":"address[]","name":"to","type":"address[]"}],"name":"mintNonFungible","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
