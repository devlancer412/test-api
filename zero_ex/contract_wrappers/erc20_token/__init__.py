"""Generated wrapper for ERC20Token Solidity contract."""

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
# constructor for ERC20Token below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ERC20TokenValidator,
    )
except ImportError:

    class ERC20TokenValidator(  # type: ignore
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

    def validate_and_normalize_inputs(self, _spender: str, _value: int):
        """Validate the inputs to the approve method."""
        self.validator.assert_valid(
            method_name="approve",
            parameter_name="_spender",
            argument_value=_spender,
        )
        _spender = self.validate_and_checksum_address(_spender)
        self.validator.assert_valid(
            method_name="approve",
            parameter_name="_value",
            argument_value=_value,
        )
        # safeguard against fractional inputs
        _value = int(_value)
        return (_spender, _value)

    def call(
        self, _spender: str, _value: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        `msg.sender` approves `_spender` to spend `_value` tokens

        :param _spender: The address of the account able to transfer the tokens
        :param _value: The amount of wei to be approved for transfer
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_spender, _value) = self.validate_and_normalize_inputs(
            _spender, _value
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_spender, _value).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, _spender: str, _value: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        `msg.sender` approves `_spender` to spend `_value` tokens

        :param _spender: The address of the account able to transfer the tokens
        :param _value: The amount of wei to be approved for transfer
        :param tx_params: transaction parameters
        """
        (_spender, _value) = self.validate_and_normalize_inputs(
            _spender, _value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_spender, _value).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _spender: str, _value: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_spender, _value) = self.validate_and_normalize_inputs(
            _spender, _value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_spender, _value).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _spender: str, _value: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_spender, _value) = self.validate_and_normalize_inputs(
            _spender, _value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_spender, _value).estimateGas(
            tx_params.as_dict()
        )


class TotalSupplyMethod(ContractMethod):
    """Various interfaces to the totalSupply method."""

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

        Query total supply of token

        :param tx_params: transaction parameters
        :returns: Total supply of token
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

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

    def validate_and_normalize_inputs(self, _from: str, _to: str, _value: int):
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
            parameter_name="_value",
            argument_value=_value,
        )
        # safeguard against fractional inputs
        _value = int(_value)
        return (_from, _to, _value)

    def call(
        self,
        _from: str,
        _to: str,
        _value: int,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        send `value` token to `to` from `from` on the condition it is approved
        by `from`

        :param _from: The address of the sender
        :param _to: The address of the recipient
        :param _value: The amount of token to be transferred
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, _to, _value) = self.validate_and_normalize_inputs(
            _from, _to, _value
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_from, _to, _value).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        _from: str,
        _to: str,
        _value: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        send `value` token to `to` from `from` on the condition it is approved
        by `from`

        :param _from: The address of the sender
        :param _to: The address of the recipient
        :param _value: The amount of token to be transferred
        :param tx_params: transaction parameters
        """
        (_from, _to, _value) = self.validate_and_normalize_inputs(
            _from, _to, _value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _value).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        _to: str,
        _value: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, _to, _value) = self.validate_and_normalize_inputs(
            _from, _to, _value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _value).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _from: str,
        _to: str,
        _value: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, _to, _value) = self.validate_and_normalize_inputs(
            _from, _to, _value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, _to, _value).estimateGas(
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

        Query the balance of owner

        :param _owner: The address from which the balance will be retrieved
        :param tx_params: transaction parameters
        :returns: Balance of owner
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


class TransferMethod(ContractMethod):
    """Various interfaces to the transfer method."""

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

    def validate_and_normalize_inputs(self, _to: str, _value: int):
        """Validate the inputs to the transfer method."""
        self.validator.assert_valid(
            method_name="transfer", parameter_name="_to", argument_value=_to,
        )
        _to = self.validate_and_checksum_address(_to)
        self.validator.assert_valid(
            method_name="transfer",
            parameter_name="_value",
            argument_value=_value,
        )
        # safeguard against fractional inputs
        _value = int(_value)
        return (_to, _value)

    def call(
        self, _to: str, _value: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        send `value` token to `to` from `msg.sender`

        :param _to: The address of the recipient
        :param _value: The amount of token to be transferred
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_to, _value) = self.validate_and_normalize_inputs(_to, _value)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_to, _value).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, _to: str, _value: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        send `value` token to `to` from `msg.sender`

        :param _to: The address of the recipient
        :param _value: The amount of token to be transferred
        :param tx_params: transaction parameters
        """
        (_to, _value) = self.validate_and_normalize_inputs(_to, _value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_to, _value).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _to: str, _value: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_to, _value) = self.validate_and_normalize_inputs(_to, _value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_to, _value).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _to: str, _value: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_to, _value) = self.validate_and_normalize_inputs(_to, _value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_to, _value).estimateGas(
            tx_params.as_dict()
        )


class AllowanceMethod(ContractMethod):
    """Various interfaces to the allowance method."""

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

    def validate_and_normalize_inputs(self, _owner: str, _spender: str):
        """Validate the inputs to the allowance method."""
        self.validator.assert_valid(
            method_name="allowance",
            parameter_name="_owner",
            argument_value=_owner,
        )
        _owner = self.validate_and_checksum_address(_owner)
        self.validator.assert_valid(
            method_name="allowance",
            parameter_name="_spender",
            argument_value=_spender,
        )
        _spender = self.validate_and_checksum_address(_spender)
        return (_owner, _spender)

    def call(
        self, _owner: str, _spender: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param _owner: The address of the account owning tokens
        :param _spender: The address of the account able to transfer the tokens
        :param tx_params: transaction parameters
        :returns: Amount of remaining tokens allowed to spent
        """
        (_owner, _spender) = self.validate_and_normalize_inputs(
            _owner, _spender
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_owner, _spender).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self, _owner: str, _spender: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_owner, _spender) = self.validate_and_normalize_inputs(
            _owner, _spender
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_owner, _spender).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ERC20Token:
    """Wrapper class for ERC20Token Solidity contract."""

    approve: ApproveMethod
    """Constructor-initialized instance of
    :class:`ApproveMethod`.
    """

    total_supply: TotalSupplyMethod
    """Constructor-initialized instance of
    :class:`TotalSupplyMethod`.
    """

    transfer_from: TransferFromMethod
    """Constructor-initialized instance of
    :class:`TransferFromMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    transfer: TransferMethod
    """Constructor-initialized instance of
    :class:`TransferMethod`.
    """

    allowance: AllowanceMethod
    """Constructor-initialized instance of
    :class:`AllowanceMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ERC20TokenValidator = None,
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
            validator = ERC20TokenValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=ERC20Token.abi()
        ).functions

        self.approve = ApproveMethod(
            web3_or_provider, contract_address, functions.approve, validator
        )

        self.total_supply = TotalSupplyMethod(
            web3_or_provider, contract_address, functions.totalSupply
        )

        self.transfer_from = TransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.transferFrom,
            validator,
        )

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.transfer = TransferMethod(
            web3_or_provider, contract_address, functions.transfer, validator
        )

        self.allowance = AllowanceMethod(
            web3_or_provider, contract_address, functions.allowance, validator
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
                abi=ERC20Token.abi(),
            )
            .events.Transfer()
            .processReceipt(tx_receipt)
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
                abi=ERC20Token.abi(),
            )
            .events.Approval()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":false,"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_owner","type":"address"},{"indexed":true,"internalType":"address","name":"_spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
