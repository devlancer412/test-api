"""Generated wrapper for DummyERC721Token Solidity contract."""

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
# constructor for DummyERC721Token below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DummyERC721TokenValidator,
    )
except ImportError:

    class DummyERC721TokenValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ApproveMethod(ContractMethod):
    """Various interfaces to the approve method."""

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

    def validate_and_normalize_inputs(self, _approved: str, _token_id: int):
        """Validate the inputs to the approve method."""
        self.validator.assert_valid(
            method_name="approve",
            parameter_name="_approved",
            argument_value=_approved,
        )
        _approved = self.validate_and_checksum_address(_approved)
        self.validator.assert_valid(
            method_name="approve",
            parameter_name="_tokenId",
            argument_value=_token_id,
        )
        # safeguard against fractional inputs
        _token_id = int(_token_id)
        return (_approved, _token_id)

    def call(
        self,
        _approved: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        The zero address indicates there is no approved address. Throws unless
        `msg.sender` is the current NFT owner, or an authorized operator of the
        current owner.

        :param _approved: The new approved NFT controller
        :param _tokenId: The NFT to approve
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_approved, _token_id) = self.validate_and_normalize_inputs(
            _approved, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_approved, _token_id).call(tx_params.as_dict())

    def send_transaction(
        self,
        _approved: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        The zero address indicates there is no approved address. Throws unless
        `msg.sender` is the current NFT owner, or an authorized operator of the
        current owner.

        :param _approved: The new approved NFT controller
        :param _tokenId: The NFT to approve
        :param tx_params: transaction parameters
        """
        (_approved, _token_id) = self.validate_and_normalize_inputs(
            _approved, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_approved, _token_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _approved: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_approved, _token_id) = self.validate_and_normalize_inputs(
            _approved, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_approved, _token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _approved: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_approved, _token_id) = self.validate_and_normalize_inputs(
            _approved, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_approved, _token_id).estimateGas(
            tx_params.as_dict()
        )


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

    def validate_and_normalize_inputs(self, _owner: str):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name="balanceOf",
            parameter_name="_owner",
            argument_value=_owner,
        )
        _owner = self.validate_and_checksum_address(_owner)
        return _owner

    def call(self, _owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        NFTs assigned to the zero address are considered invalid, and this
        function throws for queries about the zero address.

        :param _owner: An address for whom to query the balance
        :param tx_params: transaction parameters
        :returns: The number of NFTs owned by `_owner`, possibly zero
        """
        (_owner) = self.validate_and_normalize_inputs(_owner)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_owner).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, _owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_owner) = self.validate_and_normalize_inputs(_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_owner).estimateGas(tx_params.as_dict())


class BurnMethod(ContractMethod):
    """Various interfaces to the burn method."""

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

    def validate_and_normalize_inputs(self, _owner: str, _token_id: int):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name="burn", parameter_name="_owner", argument_value=_owner,
        )
        _owner = self.validate_and_checksum_address(_owner)
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="_tokenId",
            argument_value=_token_id,
        )
        # safeguard against fractional inputs
        _token_id = int(_token_id)
        return (_owner, _token_id)

    def call(
        self, _owner: str, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Function to burn a token Reverts if the given token ID doesn't exist or
        not called by contract owner

        :param _owner: Owner of token with given token ID
        :param _tokenId: ID of the token to be burned by the msg.sender
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_owner, _token_id) = self.validate_and_normalize_inputs(
            _owner, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_owner, _token_id).call(tx_params.as_dict())

    def send_transaction(
        self, _owner: str, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Function to burn a token Reverts if the given token ID doesn't exist or
        not called by contract owner

        :param _owner: Owner of token with given token ID
        :param _tokenId: ID of the token to be burned by the msg.sender
        :param tx_params: transaction parameters
        """
        (_owner, _token_id) = self.validate_and_normalize_inputs(
            _owner, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_owner, _token_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _owner: str, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_owner, _token_id) = self.validate_and_normalize_inputs(
            _owner, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_owner, _token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _owner: str, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_owner, _token_id) = self.validate_and_normalize_inputs(
            _owner, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_owner, _token_id).estimateGas(
            tx_params.as_dict()
        )


class GetApprovedMethod(ContractMethod):
    """Various interfaces to the getApproved method."""

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

    def validate_and_normalize_inputs(self, _token_id: int):
        """Validate the inputs to the getApproved method."""
        self.validator.assert_valid(
            method_name="getApproved",
            parameter_name="_tokenId",
            argument_value=_token_id,
        )
        # safeguard against fractional inputs
        _token_id = int(_token_id)
        return _token_id

    def call(
        self, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        Throws if `_tokenId` is not a valid NFT.

        :param _tokenId: The NFT to find the approved address for
        :param tx_params: transaction parameters
        :returns: The approved address for this NFT, or the zero address if
            there is none
        """
        (_token_id) = self.validate_and_normalize_inputs(_token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_token_id).call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(
        self, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_token_id) = self.validate_and_normalize_inputs(_token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_token_id).estimateGas(
            tx_params.as_dict()
        )


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

    def validate_and_normalize_inputs(self, _owner: str, _operator: str):
        """Validate the inputs to the isApprovedForAll method."""
        self.validator.assert_valid(
            method_name="isApprovedForAll",
            parameter_name="_owner",
            argument_value=_owner,
        )
        _owner = self.validate_and_checksum_address(_owner)
        self.validator.assert_valid(
            method_name="isApprovedForAll",
            parameter_name="_operator",
            argument_value=_operator,
        )
        _operator = self.validate_and_checksum_address(_operator)
        return (_owner, _operator)

    def call(
        self, _owner: str, _operator: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param _operator: The address that acts on behalf of the owner
        :param _owner: The address that owns the NFTs
        :param tx_params: transaction parameters
        :returns: True if `_operator` is an approved operator for `_owner`,
            false otherwise
        """
        (_owner, _operator) = self.validate_and_normalize_inputs(
            _owner, _operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_owner, _operator).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def estimate_gas(
        self, _owner: str, _operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_owner, _operator) = self.validate_and_normalize_inputs(
            _owner, _operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_owner, _operator).estimateGas(
            tx_params.as_dict()
        )


class MintMethod(ContractMethod):
    """Various interfaces to the mint method."""

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

    def validate_and_normalize_inputs(self, _to: str, _token_id: int):
        """Validate the inputs to the mint method."""
        self.validator.assert_valid(
            method_name="mint", parameter_name="_to", argument_value=_to,
        )
        _to = self.validate_and_checksum_address(_to)
        self.validator.assert_valid(
            method_name="mint",
            parameter_name="_tokenId",
            argument_value=_token_id,
        )
        # safeguard against fractional inputs
        _token_id = int(_token_id)
        return (_to, _token_id)

    def call(
        self, _to: str, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Function to mint a new token Reverts if the given token ID already
        exists

        :param _to: Address of the beneficiary that will own the minted token
        :param _tokenId: ID of the token to be minted by the msg.sender
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_to, _token_id) = self.validate_and_normalize_inputs(_to, _token_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_to, _token_id).call(tx_params.as_dict())

    def send_transaction(
        self, _to: str, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Function to mint a new token Reverts if the given token ID already
        exists

        :param _to: Address of the beneficiary that will own the minted token
        :param _tokenId: ID of the token to be minted by the msg.sender
        :param tx_params: transaction parameters
        """
        (_to, _token_id) = self.validate_and_normalize_inputs(_to, _token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_to, _token_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _to: str, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_to, _token_id) = self.validate_and_normalize_inputs(_to, _token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_to, _token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _to: str, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_to, _token_id) = self.validate_and_normalize_inputs(_to, _token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_to, _token_id).estimateGas(
            tx_params.as_dict()
        )


class NameMethod(ContractMethod):
    """Various interfaces to the name method."""

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

    def validate_and_normalize_inputs(self, _token_id: int):
        """Validate the inputs to the ownerOf method."""
        self.validator.assert_valid(
            method_name="ownerOf",
            parameter_name="_tokenId",
            argument_value=_token_id,
        )
        # safeguard against fractional inputs
        _token_id = int(_token_id)
        return _token_id

    def call(
        self, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        NFTs assigned to zero address are considered invalid, and queries about
        them do throw.

        :param _tokenId: The identifier for an NFT
        :param tx_params: transaction parameters
        :returns: The address of the owner of the NFT
        """
        (_token_id) = self.validate_and_normalize_inputs(_token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_token_id).call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(
        self, _token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_token_id) = self.validate_and_normalize_inputs(_token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_token_id).estimateGas(
            tx_params.as_dict()
        )


class SafeTransferFrom1Method(ContractMethod):
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
        self, _from: str, _to: str, _token_id: int
    ):
        """Validate the inputs to the safeTransferFrom method."""
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="_from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="_to",
            argument_value=_to,
        )
        _to = self.validate_and_checksum_address(_to)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="_tokenId",
            argument_value=_token_id,
        )
        # safeguard against fractional inputs
        _token_id = int(_token_id)
        return (_from, _to, _token_id)

    def call(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        This works identically to the other function with an extra data
        parameter, except this function just sets data to "".

        :param _from: The current owner of the NFT
        :param _to: The new owner
        :param _tokenId: The NFT to transfer
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, _to, _token_id) = self.validate_and_normalize_inputs(
            _from, _to, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, _to, _token_id).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        This works identically to the other function with an extra data
        parameter, except this function just sets data to "".

        :param _from: The current owner of the NFT
        :param _to: The new owner
        :param _tokenId: The NFT to transfer
        :param tx_params: transaction parameters
        """
        (_from, _to, _token_id) = self.validate_and_normalize_inputs(
            _from, _to, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _token_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, _to, _token_id) = self.validate_and_normalize_inputs(
            _from, _to, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, _to, _token_id) = self.validate_and_normalize_inputs(
            _from, _to, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _token_id).estimateGas(
            tx_params.as_dict()
        )


class SafeTransferFrom2Method(ContractMethod):
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
        self, _from: str, _to: str, _token_id: int, _data: Union[bytes, str]
    ):
        """Validate the inputs to the safeTransferFrom method."""
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="_from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="_to",
            argument_value=_to,
        )
        _to = self.validate_and_checksum_address(_to)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="_tokenId",
            argument_value=_token_id,
        )
        # safeguard against fractional inputs
        _token_id = int(_token_id)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="_data",
            argument_value=_data,
        )
        return (_from, _to, _token_id, _data)

    def call(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        _data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Throws unless `msg.sender` is the current owner, an authorized
        operator, or the approved address for this NFT. Throws if `_from` is
        not the current owner. Throws if `_to` is the zero address. Throws if
        `_tokenId` is not a valid NFT. When transfer is complete, this function
        checks if `_to` is a smart contract (code size > 0). If so, it calls
        `onERC721Received` on `_to` and throws if the return value is not
        `bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))`.

        :param _data: Additional data with no specified format, sent in call to
            `_to`
        :param _from: The current owner of the NFT
        :param _to: The new owner
        :param _tokenId: The NFT to transfer
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, _to, _token_id, _data) = self.validate_and_normalize_inputs(
            _from, _to, _token_id, _data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, _to, _token_id, _data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        _data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Throws unless `msg.sender` is the current owner, an authorized
        operator, or the approved address for this NFT. Throws if `_from` is
        not the current owner. Throws if `_to` is the zero address. Throws if
        `_tokenId` is not a valid NFT. When transfer is complete, this function
        checks if `_to` is a smart contract (code size > 0). If so, it calls
        `onERC721Received` on `_to` and throws if the return value is not
        `bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))`.

        :param _data: Additional data with no specified format, sent in call to
            `_to`
        :param _from: The current owner of the NFT
        :param _to: The new owner
        :param _tokenId: The NFT to transfer
        :param tx_params: transaction parameters
        """
        (_from, _to, _token_id, _data) = self.validate_and_normalize_inputs(
            _from, _to, _token_id, _data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _token_id, _data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        _data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, _to, _token_id, _data) = self.validate_and_normalize_inputs(
            _from, _to, _token_id, _data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, _to, _token_id, _data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        _data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, _to, _token_id, _data) = self.validate_and_normalize_inputs(
            _from, _to, _token_id, _data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, _to, _token_id, _data
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

    def validate_and_normalize_inputs(self, _operator: str, _approved: bool):
        """Validate the inputs to the setApprovalForAll method."""
        self.validator.assert_valid(
            method_name="setApprovalForAll",
            parameter_name="_operator",
            argument_value=_operator,
        )
        _operator = self.validate_and_checksum_address(_operator)
        self.validator.assert_valid(
            method_name="setApprovalForAll",
            parameter_name="_approved",
            argument_value=_approved,
        )
        return (_operator, _approved)

    def call(
        self,
        _operator: str,
        _approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Emits the ApprovalForAll event. The contract MUST allow multiple
        operators per owner.

        :param _approved: True if the operator is approved, false to revoke
            approval
        :param _operator: Address to add to the set of authorized operators
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_operator, _approved) = self.validate_and_normalize_inputs(
            _operator, _approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_operator, _approved).call(tx_params.as_dict())

    def send_transaction(
        self,
        _operator: str,
        _approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Emits the ApprovalForAll event. The contract MUST allow multiple
        operators per owner.

        :param _approved: True if the operator is approved, false to revoke
            approval
        :param _operator: Address to add to the set of authorized operators
        :param tx_params: transaction parameters
        """
        (_operator, _approved) = self.validate_and_normalize_inputs(
            _operator, _approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_operator, _approved).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _operator: str,
        _approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_operator, _approved) = self.validate_and_normalize_inputs(
            _operator, _approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_operator, _approved).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _operator: str,
        _approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_operator, _approved) = self.validate_and_normalize_inputs(
            _operator, _approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_operator, _approved).estimateGas(
            tx_params.as_dict()
        )


class SymbolMethod(ContractMethod):
    """Various interfaces to the symbol method."""

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
        self, _from: str, _to: str, _token_id: int
    ):
        """Validate the inputs to the transferFrom method."""
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="_from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="_to",
            argument_value=_to,
        )
        _to = self.validate_and_checksum_address(_to)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="_tokenId",
            argument_value=_token_id,
        )
        # safeguard against fractional inputs
        _token_id = int(_token_id)
        return (_from, _to, _token_id)

    def call(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Throws unless `msg.sender` is the current owner, an authorized
        operator, or the approved address for this NFT. Throws if `_from` is
        not the current owner. Throws if `_to` is the zero address. Throws if
        `_tokenId` is not a valid NFT.

        :param _from: The current owner of the NFT
        :param _to: The new owner
        :param _tokenId: The NFT to transfer
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, _to, _token_id) = self.validate_and_normalize_inputs(
            _from, _to, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, _to, _token_id).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Throws unless `msg.sender` is the current owner, an authorized
        operator, or the approved address for this NFT. Throws if `_from` is
        not the current owner. Throws if `_to` is the zero address. Throws if
        `_tokenId` is not a valid NFT.

        :param _from: The current owner of the NFT
        :param _to: The new owner
        :param _tokenId: The NFT to transfer
        :param tx_params: transaction parameters
        """
        (_from, _to, _token_id) = self.validate_and_normalize_inputs(
            _from, _to, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _token_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, _to, _token_id) = self.validate_and_normalize_inputs(
            _from, _to, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _from: str,
        _to: str,
        _token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, _to, _token_id) = self.validate_and_normalize_inputs(
            _from, _to, _token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _token_id).estimateGas(
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
class DummyERC721Token:
    """Wrapper class for DummyERC721Token Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    approve: ApproveMethod
    """Constructor-initialized instance of
    :class:`ApproveMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    burn: BurnMethod
    """Constructor-initialized instance of
    :class:`BurnMethod`.
    """

    get_approved: GetApprovedMethod
    """Constructor-initialized instance of
    :class:`GetApprovedMethod`.
    """

    is_approved_for_all: IsApprovedForAllMethod
    """Constructor-initialized instance of
    :class:`IsApprovedForAllMethod`.
    """

    mint: MintMethod
    """Constructor-initialized instance of
    :class:`MintMethod`.
    """

    name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    owner_of: OwnerOfMethod
    """Constructor-initialized instance of
    :class:`OwnerOfMethod`.
    """

    safe_transfer_from1: SafeTransferFrom1Method
    """Constructor-initialized instance of
    :class:`SafeTransferFrom1Method`.
    """

    safe_transfer_from2: SafeTransferFrom2Method
    """Constructor-initialized instance of
    :class:`SafeTransferFrom2Method`.
    """

    set_approval_for_all: SetApprovalForAllMethod
    """Constructor-initialized instance of
    :class:`SetApprovalForAllMethod`.
    """

    symbol: SymbolMethod
    """Constructor-initialized instance of
    :class:`SymbolMethod`.
    """

    transfer_from: TransferFromMethod
    """Constructor-initialized instance of
    :class:`TransferFromMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: DummyERC721TokenValidator = None,
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
            validator = DummyERC721TokenValidator(
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
            abi=DummyERC721Token.abi(),
        ).functions

        self.approve = ApproveMethod(
            web3_or_provider, contract_address, functions.approve, validator
        )

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.burn = BurnMethod(
            web3_or_provider, contract_address, functions.burn, validator
        )

        self.get_approved = GetApprovedMethod(
            web3_or_provider,
            contract_address,
            functions.getApproved,
            validator,
        )

        self.is_approved_for_all = IsApprovedForAllMethod(
            web3_or_provider,
            contract_address,
            functions.isApprovedForAll,
            validator,
        )

        self.mint = MintMethod(
            web3_or_provider, contract_address, functions.mint, validator
        )

        self.name = NameMethod(
            web3_or_provider, contract_address, functions.name
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
        )

        self.owner_of = OwnerOfMethod(
            web3_or_provider, contract_address, functions.ownerOf, validator
        )

        self.safe_transfer_from1 = SafeTransferFrom1Method(
            web3_or_provider,
            contract_address,
            functions.safeTransferFrom,
            validator,
        )

        self.safe_transfer_from2 = SafeTransferFrom2Method(
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

        self.symbol = SymbolMethod(
            web3_or_provider, contract_address, functions.symbol
        )

        self.transfer_from = TransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.transferFrom,
            validator,
        )

        self.transfer_ownership = TransferOwnershipMethod(
            web3_or_provider,
            contract_address,
            functions.transferOwnership,
            validator,
        )

    def get_approval_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Approval event.

        :param tx_hash: hash of transaction emitting Approval event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DummyERC721Token.abi(),
            )
            .events.Approval()
            .processReceipt(tx_receipt)
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
                abi=DummyERC721Token.abi(),
            )
            .events.ApprovalForAll()
            .processReceipt(tx_receipt)
        )

    def get_transfer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Transfer event.

        :param tx_hash: hash of transaction emitting Transfer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DummyERC721Token.abi(),
            )
            .events.Transfer()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_owner","type":"address"},{"indexed":true,"internalType":"address","name":"_approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_owner","type":"address"},{"indexed":true,"internalType":"address","name":"_operator","type":"address"},{"indexed":false,"internalType":"bool","name":"_approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"},{"indexed":true,"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":false,"inputs":[{"internalType":"address","name":"_approved","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"bool","name":"_approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
