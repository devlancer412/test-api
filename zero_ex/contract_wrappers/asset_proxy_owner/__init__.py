"""Generated wrapper for AssetProxyOwner Solidity contract."""

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
# constructor for AssetProxyOwner below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        AssetProxyOwnerValidator,
    )
except ImportError:

    class AssetProxyOwnerValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class MaxOwnerCountMethod(ContractMethod):
    """Various interfaces to the MAX_OWNER_COUNT method."""

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


class AddOwnerMethod(ContractMethod):
    """Various interfaces to the addOwner method."""

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

    def validate_and_normalize_inputs(self, owner: str):
        """Validate the inputs to the addOwner method."""
        self.validator.assert_valid(
            method_name="addOwner",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        return owner

    def call(self, owner: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Allows to add a new owner. Transaction has to be sent by wallet.

        :param owner: Address of new owner.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(owner).call(tx_params.as_dict())

    def send_transaction(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows to add a new owner. Transaction has to be sent by wallet.

        :param owner: Address of new owner.
        :param tx_params: transaction parameters
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).transact(tx_params.as_dict())

    def build_transaction(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).estimateGas(tx_params.as_dict())


class ChangeRequirementMethod(ContractMethod):
    """Various interfaces to the changeRequirement method."""

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

    def validate_and_normalize_inputs(self, _required: int):
        """Validate the inputs to the changeRequirement method."""
        self.validator.assert_valid(
            method_name="changeRequirement",
            parameter_name="_required",
            argument_value=_required,
        )
        # safeguard against fractional inputs
        _required = int(_required)
        return _required

    def call(
        self, _required: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Allows to change the number of required confirmations. Transaction has
        to be sent by wallet.

        :param _required: Number of required confirmations.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_required) = self.validate_and_normalize_inputs(_required)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_required).call(tx_params.as_dict())

    def send_transaction(
        self, _required: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows to change the number of required confirmations. Transaction has
        to be sent by wallet.

        :param _required: Number of required confirmations.
        :param tx_params: transaction parameters
        """
        (_required) = self.validate_and_normalize_inputs(_required)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_required).transact(tx_params.as_dict())

    def build_transaction(
        self, _required: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_required) = self.validate_and_normalize_inputs(_required)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_required).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _required: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_required) = self.validate_and_normalize_inputs(_required)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_required).estimateGas(
            tx_params.as_dict()
        )


class ChangeTimeLockMethod(ContractMethod):
    """Various interfaces to the changeTimeLock method."""

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

    def validate_and_normalize_inputs(self, _seconds_time_locked: int):
        """Validate the inputs to the changeTimeLock method."""
        self.validator.assert_valid(
            method_name="changeTimeLock",
            parameter_name="_secondsTimeLocked",
            argument_value=_seconds_time_locked,
        )
        # safeguard against fractional inputs
        _seconds_time_locked = int(_seconds_time_locked)
        return _seconds_time_locked

    def call(
        self, _seconds_time_locked: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Changes the duration of the time lock for transactions.

        :param _secondsTimeLocked: Duration needed after a transaction is
            confirmed and before it becomes executable, in seconds.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_seconds_time_locked) = self.validate_and_normalize_inputs(
            _seconds_time_locked
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_seconds_time_locked).call(tx_params.as_dict())

    def send_transaction(
        self, _seconds_time_locked: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Changes the duration of the time lock for transactions.

        :param _secondsTimeLocked: Duration needed after a transaction is
            confirmed and before it becomes executable, in seconds.
        :param tx_params: transaction parameters
        """
        (_seconds_time_locked) = self.validate_and_normalize_inputs(
            _seconds_time_locked
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_seconds_time_locked).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _seconds_time_locked: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_seconds_time_locked) = self.validate_and_normalize_inputs(
            _seconds_time_locked
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_seconds_time_locked).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _seconds_time_locked: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_seconds_time_locked) = self.validate_and_normalize_inputs(
            _seconds_time_locked
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_seconds_time_locked).estimateGas(
            tx_params.as_dict()
        )


class ConfirmTransactionMethod(ContractMethod):
    """Various interfaces to the confirmTransaction method."""

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

    def validate_and_normalize_inputs(self, transaction_id: int):
        """Validate the inputs to the confirmTransaction method."""
        self.validator.assert_valid(
            method_name="confirmTransaction",
            parameter_name="transactionId",
            argument_value=transaction_id,
        )
        # safeguard against fractional inputs
        transaction_id = int(transaction_id)
        return transaction_id

    def call(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Allows an owner to confirm a transaction.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(transaction_id).call(tx_params.as_dict())

    def send_transaction(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows an owner to confirm a transaction.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).estimateGas(
            tx_params.as_dict()
        )


class ConfirmationTimesMethod(ContractMethod):
    """Various interfaces to the confirmationTimes method."""

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
        """Validate the inputs to the confirmationTimes method."""
        self.validator.assert_valid(
            method_name="confirmationTimes",
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


class ConfirmationsMethod(ContractMethod):
    """Various interfaces to the confirmations method."""

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

    def validate_and_normalize_inputs(self, index_0: int, index_1: str):
        """Validate the inputs to the confirmations method."""
        self.validator.assert_valid(
            method_name="confirmations",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        self.validator.assert_valid(
            method_name="confirmations",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)

    def call(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
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
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


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

    def validate_and_normalize_inputs(self, transaction_id: int):
        """Validate the inputs to the executeTransaction method."""
        self.validator.assert_valid(
            method_name="executeTransaction",
            parameter_name="transactionId",
            argument_value=transaction_id,
        )
        # safeguard against fractional inputs
        transaction_id = int(transaction_id)
        return transaction_id

    def call(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Allows anyone to execute a confirmed transaction. Transactions *must*
        encode the values with the signature "bytes[] data, address[]
        destinations, uint256[] values" The `destination` and `value` fields of
        the transaction in storage are ignored. All function calls must be
        successful or the entire call will revert.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(transaction_id).call(tx_params.as_dict())

    def send_transaction(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows anyone to execute a confirmed transaction. Transactions *must*
        encode the values with the signature "bytes[] data, address[]
        destinations, uint256[] values" The `destination` and `value` fields of
        the transaction in storage are ignored. All function calls must be
        successful or the entire call will revert.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).estimateGas(
            tx_params.as_dict()
        )


class FunctionCallTimeLocksMethod(ContractMethod):
    """Various interfaces to the functionCallTimeLocks method."""

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
        """Validate the inputs to the functionCallTimeLocks method."""
        self.validator.assert_valid(
            method_name="functionCallTimeLocks",
            parameter_name="index_0",
            argument_value=index_0,
        )
        self.validator.assert_valid(
            method_name="functionCallTimeLocks",
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
    ) -> Tuple[bool, int]:
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
        return (
            returned[0],
            returned[1],
        )

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


class GetConfirmationCountMethod(ContractMethod):
    """Various interfaces to the getConfirmationCount method."""

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

    def validate_and_normalize_inputs(self, transaction_id: int):
        """Validate the inputs to the getConfirmationCount method."""
        self.validator.assert_valid(
            method_name="getConfirmationCount",
            parameter_name="transactionId",
            argument_value=transaction_id,
        )
        # safeguard against fractional inputs
        transaction_id = int(transaction_id)
        return transaction_id

    def call(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        Returns number of confirmations of a transaction.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        :returns: Number of confirmations.
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(transaction_id).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).estimateGas(
            tx_params.as_dict()
        )


class GetConfirmationsMethod(ContractMethod):
    """Various interfaces to the getConfirmations method."""

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

    def validate_and_normalize_inputs(self, transaction_id: int):
        """Validate the inputs to the getConfirmations method."""
        self.validator.assert_valid(
            method_name="getConfirmations",
            parameter_name="transactionId",
            argument_value=transaction_id,
        )
        # safeguard against fractional inputs
        transaction_id = int(transaction_id)
        return transaction_id

    def call(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> List[str]:
        """Execute underlying contract method via eth_call.

        Returns array with owner addresses, which confirmed transaction.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        :returns: Returns array of owner addresses.
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(transaction_id).call(
            tx_params.as_dict()
        )
        return [str(element) for element in returned]

    def estimate_gas(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).estimateGas(
            tx_params.as_dict()
        )


class GetOwnersMethod(ContractMethod):
    """Various interfaces to the getOwners method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> List[str]:
        """Execute underlying contract method via eth_call.

        Returns list of owners.

        :param tx_params: transaction parameters
        :returns: List of owner addresses.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [str(element) for element in returned]

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class GetTransactionCountMethod(ContractMethod):
    """Various interfaces to the getTransactionCount method."""

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

    def validate_and_normalize_inputs(self, pending: bool, executed: bool):
        """Validate the inputs to the getTransactionCount method."""
        self.validator.assert_valid(
            method_name="getTransactionCount",
            parameter_name="pending",
            argument_value=pending,
        )
        self.validator.assert_valid(
            method_name="getTransactionCount",
            parameter_name="executed",
            argument_value=executed,
        )
        return (pending, executed)

    def call(
        self,
        pending: bool,
        executed: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        Returns total number of transactions after filers are applied.

        :param executed: Include executed transactions.
        :param pending: Include pending transactions.
        :param tx_params: transaction parameters
        :returns: Total number of transactions after filters are applied.
        """
        (pending, executed) = self.validate_and_normalize_inputs(
            pending, executed
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(pending, executed).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self,
        pending: bool,
        executed: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (pending, executed) = self.validate_and_normalize_inputs(
            pending, executed
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pending, executed).estimateGas(
            tx_params.as_dict()
        )


class GetTransactionIdsMethod(ContractMethod):
    """Various interfaces to the getTransactionIds method."""

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
        self, _from: int, to: int, pending: bool, executed: bool
    ):
        """Validate the inputs to the getTransactionIds method."""
        self.validator.assert_valid(
            method_name="getTransactionIds",
            parameter_name="from",
            argument_value=_from,
        )
        # safeguard against fractional inputs
        _from = int(_from)
        self.validator.assert_valid(
            method_name="getTransactionIds",
            parameter_name="to",
            argument_value=to,
        )
        # safeguard against fractional inputs
        to = int(to)
        self.validator.assert_valid(
            method_name="getTransactionIds",
            parameter_name="pending",
            argument_value=pending,
        )
        self.validator.assert_valid(
            method_name="getTransactionIds",
            parameter_name="executed",
            argument_value=executed,
        )
        return (_from, to, pending, executed)

    def call(
        self,
        _from: int,
        to: int,
        pending: bool,
        executed: bool,
        tx_params: Optional[TxParams] = None,
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        Returns list of transaction IDs in defined range.

        :param executed: Include executed transactions.
        :param from: Index start position of transaction array.
        :param pending: Include pending transactions.
        :param to: Index end position of transaction array.
        :param tx_params: transaction parameters
        :returns: Returns array of transaction IDs.
        """
        (_from, to, pending, executed) = self.validate_and_normalize_inputs(
            _from, to, pending, executed
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_from, to, pending, executed).call(
            tx_params.as_dict()
        )
        return [int(element) for element in returned]

    def estimate_gas(
        self,
        _from: int,
        to: int,
        pending: bool,
        executed: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, pending, executed) = self.validate_and_normalize_inputs(
            _from, to, pending, executed
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, pending, executed
        ).estimateGas(tx_params.as_dict())


class IsConfirmedMethod(ContractMethod):
    """Various interfaces to the isConfirmed method."""

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

    def validate_and_normalize_inputs(self, transaction_id: int):
        """Validate the inputs to the isConfirmed method."""
        self.validator.assert_valid(
            method_name="isConfirmed",
            parameter_name="transactionId",
            argument_value=transaction_id,
        )
        # safeguard against fractional inputs
        transaction_id = int(transaction_id)
        return transaction_id

    def call(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        Returns the confirmation status of a transaction.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        :returns: Confirmation status.
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(transaction_id).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def estimate_gas(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).estimateGas(
            tx_params.as_dict()
        )


class IsOwnerMethod(ContractMethod):
    """Various interfaces to the isOwner method."""

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

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the isOwner method."""
        self.validator.assert_valid(
            method_name="isOwner",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return bool(returned)

    def estimate_gas(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class OwnersMethod(ContractMethod):
    """Various interfaces to the owners method."""

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
        """Validate the inputs to the owners method."""
        self.validator.assert_valid(
            method_name="owners",
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


class RegisterFunctionCallMethod(ContractMethod):
    """Various interfaces to the registerFunctionCall method."""

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
        has_custom_time_lock: bool,
        function_selector: Union[bytes, str],
        destination: str,
        new_seconds_time_locked: int,
    ):
        """Validate the inputs to the registerFunctionCall method."""
        self.validator.assert_valid(
            method_name="registerFunctionCall",
            parameter_name="hasCustomTimeLock",
            argument_value=has_custom_time_lock,
        )
        self.validator.assert_valid(
            method_name="registerFunctionCall",
            parameter_name="functionSelector",
            argument_value=function_selector,
        )
        self.validator.assert_valid(
            method_name="registerFunctionCall",
            parameter_name="destination",
            argument_value=destination,
        )
        destination = self.validate_and_checksum_address(destination)
        self.validator.assert_valid(
            method_name="registerFunctionCall",
            parameter_name="newSecondsTimeLocked",
            argument_value=new_seconds_time_locked,
        )
        return (
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        )

    def call(
        self,
        has_custom_time_lock: bool,
        function_selector: Union[bytes, str],
        destination: str,
        new_seconds_time_locked: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Registers a custom timelock to a specific function selector /
        destination combo

        :param destination: Address of destination where function will be
            called.
        :param functionSelector: 4 byte selector of registered function.
        :param hasCustomTimeLock: True if timelock is custom.
        :param newSecondsTimeLocked: Duration in seconds needed after a
            transaction is confirmed to become executable.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        ) = self.validate_and_normalize_inputs(
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        has_custom_time_lock: bool,
        function_selector: Union[bytes, str],
        destination: str,
        new_seconds_time_locked: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Registers a custom timelock to a specific function selector /
        destination combo

        :param destination: Address of destination where function will be
            called.
        :param functionSelector: 4 byte selector of registered function.
        :param hasCustomTimeLock: True if timelock is custom.
        :param newSecondsTimeLocked: Duration in seconds needed after a
            transaction is confirmed to become executable.
        :param tx_params: transaction parameters
        """
        (
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        ) = self.validate_and_normalize_inputs(
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        has_custom_time_lock: bool,
        function_selector: Union[bytes, str],
        destination: str,
        new_seconds_time_locked: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        ) = self.validate_and_normalize_inputs(
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        has_custom_time_lock: bool,
        function_selector: Union[bytes, str],
        destination: str,
        new_seconds_time_locked: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        ) = self.validate_and_normalize_inputs(
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            has_custom_time_lock,
            function_selector,
            destination,
            new_seconds_time_locked,
        ).estimateGas(tx_params.as_dict())


class RemoveOwnerMethod(ContractMethod):
    """Various interfaces to the removeOwner method."""

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

    def validate_and_normalize_inputs(self, owner: str):
        """Validate the inputs to the removeOwner method."""
        self.validator.assert_valid(
            method_name="removeOwner",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        return owner

    def call(self, owner: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Allows to remove an owner. Transaction has to be sent by wallet.

        :param owner: Address of owner.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(owner).call(tx_params.as_dict())

    def send_transaction(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows to remove an owner. Transaction has to be sent by wallet.

        :param owner: Address of owner.
        :param tx_params: transaction parameters
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).transact(tx_params.as_dict())

    def build_transaction(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).estimateGas(tx_params.as_dict())


class ReplaceOwnerMethod(ContractMethod):
    """Various interfaces to the replaceOwner method."""

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

    def validate_and_normalize_inputs(self, owner: str, new_owner: str):
        """Validate the inputs to the replaceOwner method."""
        self.validator.assert_valid(
            method_name="replaceOwner",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name="replaceOwner",
            parameter_name="newOwner",
            argument_value=new_owner,
        )
        new_owner = self.validate_and_checksum_address(new_owner)
        return (owner, new_owner)

    def call(
        self, owner: str, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Allows to replace an owner with a new owner. Transaction has to be sent
        by wallet.

        :param newOwner: Address of new owner.
        :param owner: Address of owner to be replaced.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner, new_owner) = self.validate_and_normalize_inputs(
            owner, new_owner
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(owner, new_owner).call(tx_params.as_dict())

    def send_transaction(
        self, owner: str, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows to replace an owner with a new owner. Transaction has to be sent
        by wallet.

        :param newOwner: Address of new owner.
        :param owner: Address of owner to be replaced.
        :param tx_params: transaction parameters
        """
        (owner, new_owner) = self.validate_and_normalize_inputs(
            owner, new_owner
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, new_owner).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, owner: str, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, new_owner) = self.validate_and_normalize_inputs(
            owner, new_owner
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, new_owner).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, owner: str, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner, new_owner) = self.validate_and_normalize_inputs(
            owner, new_owner
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, new_owner).estimateGas(
            tx_params.as_dict()
        )


class RequiredMethod(ContractMethod):
    """Various interfaces to the required method."""

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


class RevokeConfirmationMethod(ContractMethod):
    """Various interfaces to the revokeConfirmation method."""

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

    def validate_and_normalize_inputs(self, transaction_id: int):
        """Validate the inputs to the revokeConfirmation method."""
        self.validator.assert_valid(
            method_name="revokeConfirmation",
            parameter_name="transactionId",
            argument_value=transaction_id,
        )
        # safeguard against fractional inputs
        transaction_id = int(transaction_id)
        return transaction_id

    def call(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Allows an owner to revoke a confirmation for a transaction.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(transaction_id).call(tx_params.as_dict())

    def send_transaction(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows an owner to revoke a confirmation for a transaction.

        :param transactionId: Transaction ID.
        :param tx_params: transaction parameters
        """
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, transaction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (transaction_id) = self.validate_and_normalize_inputs(transaction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_id).estimateGas(
            tx_params.as_dict()
        )


class SecondsTimeLockedMethod(ContractMethod):
    """Various interfaces to the secondsTimeLocked method."""

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


class SubmitTransactionMethod(ContractMethod):
    """Various interfaces to the submitTransaction method."""

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
        self, destination: str, value: int, data: Union[bytes, str]
    ):
        """Validate the inputs to the submitTransaction method."""
        self.validator.assert_valid(
            method_name="submitTransaction",
            parameter_name="destination",
            argument_value=destination,
        )
        destination = self.validate_and_checksum_address(destination)
        self.validator.assert_valid(
            method_name="submitTransaction",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        self.validator.assert_valid(
            method_name="submitTransaction",
            parameter_name="data",
            argument_value=data,
        )
        return (destination, value, data)

    def call(
        self,
        destination: str,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        Allows an owner to submit and confirm a transaction.

        :param data: Transaction data payload.
        :param destination: Transaction target address.
        :param value: Transaction ether value.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (destination, value, data) = self.validate_and_normalize_inputs(
            destination, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(destination, value, data).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        destination: str,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows an owner to submit and confirm a transaction.

        :param data: Transaction data payload.
        :param destination: Transaction target address.
        :param value: Transaction ether value.
        :param tx_params: transaction parameters
        """
        (destination, value, data) = self.validate_and_normalize_inputs(
            destination, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(destination, value, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        destination: str,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (destination, value, data) = self.validate_and_normalize_inputs(
            destination, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            destination, value, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        destination: str,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (destination, value, data) = self.validate_and_normalize_inputs(
            destination, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(destination, value, data).estimateGas(
            tx_params.as_dict()
        )


class TransactionCountMethod(ContractMethod):
    """Various interfaces to the transactionCount method."""

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


class TransactionsMethod(ContractMethod):
    """Various interfaces to the transactions method."""

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
        """Validate the inputs to the transactions method."""
        self.validator.assert_valid(
            method_name="transactions",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[str, int, Union[bytes, str], bool]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class AssetProxyOwner:
    """Wrapper class for AssetProxyOwner Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    max_owner_count: MaxOwnerCountMethod
    """Constructor-initialized instance of
    :class:`MaxOwnerCountMethod`.
    """

    add_owner: AddOwnerMethod
    """Constructor-initialized instance of
    :class:`AddOwnerMethod`.
    """

    change_requirement: ChangeRequirementMethod
    """Constructor-initialized instance of
    :class:`ChangeRequirementMethod`.
    """

    change_time_lock: ChangeTimeLockMethod
    """Constructor-initialized instance of
    :class:`ChangeTimeLockMethod`.
    """

    confirm_transaction: ConfirmTransactionMethod
    """Constructor-initialized instance of
    :class:`ConfirmTransactionMethod`.
    """

    confirmation_times: ConfirmationTimesMethod
    """Constructor-initialized instance of
    :class:`ConfirmationTimesMethod`.
    """

    confirmations: ConfirmationsMethod
    """Constructor-initialized instance of
    :class:`ConfirmationsMethod`.
    """

    execute_transaction: ExecuteTransactionMethod
    """Constructor-initialized instance of
    :class:`ExecuteTransactionMethod`.
    """

    function_call_time_locks: FunctionCallTimeLocksMethod
    """Constructor-initialized instance of
    :class:`FunctionCallTimeLocksMethod`.
    """

    get_confirmation_count: GetConfirmationCountMethod
    """Constructor-initialized instance of
    :class:`GetConfirmationCountMethod`.
    """

    get_confirmations: GetConfirmationsMethod
    """Constructor-initialized instance of
    :class:`GetConfirmationsMethod`.
    """

    get_owners: GetOwnersMethod
    """Constructor-initialized instance of
    :class:`GetOwnersMethod`.
    """

    get_transaction_count: GetTransactionCountMethod
    """Constructor-initialized instance of
    :class:`GetTransactionCountMethod`.
    """

    get_transaction_ids: GetTransactionIdsMethod
    """Constructor-initialized instance of
    :class:`GetTransactionIdsMethod`.
    """

    is_confirmed: IsConfirmedMethod
    """Constructor-initialized instance of
    :class:`IsConfirmedMethod`.
    """

    is_owner: IsOwnerMethod
    """Constructor-initialized instance of
    :class:`IsOwnerMethod`.
    """

    owners: OwnersMethod
    """Constructor-initialized instance of
    :class:`OwnersMethod`.
    """

    register_function_call: RegisterFunctionCallMethod
    """Constructor-initialized instance of
    :class:`RegisterFunctionCallMethod`.
    """

    remove_owner: RemoveOwnerMethod
    """Constructor-initialized instance of
    :class:`RemoveOwnerMethod`.
    """

    replace_owner: ReplaceOwnerMethod
    """Constructor-initialized instance of
    :class:`ReplaceOwnerMethod`.
    """

    required: RequiredMethod
    """Constructor-initialized instance of
    :class:`RequiredMethod`.
    """

    revoke_confirmation: RevokeConfirmationMethod
    """Constructor-initialized instance of
    :class:`RevokeConfirmationMethod`.
    """

    seconds_time_locked: SecondsTimeLockedMethod
    """Constructor-initialized instance of
    :class:`SecondsTimeLockedMethod`.
    """

    submit_transaction: SubmitTransactionMethod
    """Constructor-initialized instance of
    :class:`SubmitTransactionMethod`.
    """

    transaction_count: TransactionCountMethod
    """Constructor-initialized instance of
    :class:`TransactionCountMethod`.
    """

    transactions: TransactionsMethod
    """Constructor-initialized instance of
    :class:`TransactionsMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: AssetProxyOwnerValidator = None,
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
            validator = AssetProxyOwnerValidator(
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
            abi=AssetProxyOwner.abi(),
        ).functions

        self.max_owner_count = MaxOwnerCountMethod(
            web3_or_provider, contract_address, functions.MAX_OWNER_COUNT
        )

        self.add_owner = AddOwnerMethod(
            web3_or_provider, contract_address, functions.addOwner, validator
        )

        self.change_requirement = ChangeRequirementMethod(
            web3_or_provider,
            contract_address,
            functions.changeRequirement,
            validator,
        )

        self.change_time_lock = ChangeTimeLockMethod(
            web3_or_provider,
            contract_address,
            functions.changeTimeLock,
            validator,
        )

        self.confirm_transaction = ConfirmTransactionMethod(
            web3_or_provider,
            contract_address,
            functions.confirmTransaction,
            validator,
        )

        self.confirmation_times = ConfirmationTimesMethod(
            web3_or_provider,
            contract_address,
            functions.confirmationTimes,
            validator,
        )

        self.confirmations = ConfirmationsMethod(
            web3_or_provider,
            contract_address,
            functions.confirmations,
            validator,
        )

        self.execute_transaction = ExecuteTransactionMethod(
            web3_or_provider,
            contract_address,
            functions.executeTransaction,
            validator,
        )

        self.function_call_time_locks = FunctionCallTimeLocksMethod(
            web3_or_provider,
            contract_address,
            functions.functionCallTimeLocks,
            validator,
        )

        self.get_confirmation_count = GetConfirmationCountMethod(
            web3_or_provider,
            contract_address,
            functions.getConfirmationCount,
            validator,
        )

        self.get_confirmations = GetConfirmationsMethod(
            web3_or_provider,
            contract_address,
            functions.getConfirmations,
            validator,
        )

        self.get_owners = GetOwnersMethod(
            web3_or_provider, contract_address, functions.getOwners
        )

        self.get_transaction_count = GetTransactionCountMethod(
            web3_or_provider,
            contract_address,
            functions.getTransactionCount,
            validator,
        )

        self.get_transaction_ids = GetTransactionIdsMethod(
            web3_or_provider,
            contract_address,
            functions.getTransactionIds,
            validator,
        )

        self.is_confirmed = IsConfirmedMethod(
            web3_or_provider,
            contract_address,
            functions.isConfirmed,
            validator,
        )

        self.is_owner = IsOwnerMethod(
            web3_or_provider, contract_address, functions.isOwner, validator
        )

        self.owners = OwnersMethod(
            web3_or_provider, contract_address, functions.owners, validator
        )

        self.register_function_call = RegisterFunctionCallMethod(
            web3_or_provider,
            contract_address,
            functions.registerFunctionCall,
            validator,
        )

        self.remove_owner = RemoveOwnerMethod(
            web3_or_provider,
            contract_address,
            functions.removeOwner,
            validator,
        )

        self.replace_owner = ReplaceOwnerMethod(
            web3_or_provider,
            contract_address,
            functions.replaceOwner,
            validator,
        )

        self.required = RequiredMethod(
            web3_or_provider, contract_address, functions.required
        )

        self.revoke_confirmation = RevokeConfirmationMethod(
            web3_or_provider,
            contract_address,
            functions.revokeConfirmation,
            validator,
        )

        self.seconds_time_locked = SecondsTimeLockedMethod(
            web3_or_provider, contract_address, functions.secondsTimeLocked
        )

        self.submit_transaction = SubmitTransactionMethod(
            web3_or_provider,
            contract_address,
            functions.submitTransaction,
            validator,
        )

        self.transaction_count = TransactionCountMethod(
            web3_or_provider, contract_address, functions.transactionCount
        )

        self.transactions = TransactionsMethod(
            web3_or_provider,
            contract_address,
            functions.transactions,
            validator,
        )

    def get_confirmation_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Confirmation event.

        :param tx_hash: hash of transaction emitting Confirmation event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.Confirmation()
            .processReceipt(tx_receipt)
        )

    def get_confirmation_time_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ConfirmationTimeSet event.

        :param tx_hash: hash of transaction emitting ConfirmationTimeSet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.ConfirmationTimeSet()
            .processReceipt(tx_receipt)
        )

    def get_deposit_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Deposit event.

        :param tx_hash: hash of transaction emitting Deposit event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.Deposit()
            .processReceipt(tx_receipt)
        )

    def get_execution_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Execution event.

        :param tx_hash: hash of transaction emitting Execution event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.Execution()
            .processReceipt(tx_receipt)
        )

    def get_execution_failure_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ExecutionFailure event.

        :param tx_hash: hash of transaction emitting ExecutionFailure event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.ExecutionFailure()
            .processReceipt(tx_receipt)
        )

    def get_function_call_time_lock_registration_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for FunctionCallTimeLockRegistration event.

        :param tx_hash: hash of transaction emitting
            FunctionCallTimeLockRegistration event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.FunctionCallTimeLockRegistration()
            .processReceipt(tx_receipt)
        )

    def get_owner_addition_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnerAddition event.

        :param tx_hash: hash of transaction emitting OwnerAddition event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.OwnerAddition()
            .processReceipt(tx_receipt)
        )

    def get_owner_removal_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnerRemoval event.

        :param tx_hash: hash of transaction emitting OwnerRemoval event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.OwnerRemoval()
            .processReceipt(tx_receipt)
        )

    def get_requirement_change_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RequirementChange event.

        :param tx_hash: hash of transaction emitting RequirementChange event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.RequirementChange()
            .processReceipt(tx_receipt)
        )

    def get_revocation_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Revocation event.

        :param tx_hash: hash of transaction emitting Revocation event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.Revocation()
            .processReceipt(tx_receipt)
        )

    def get_submission_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Submission event.

        :param tx_hash: hash of transaction emitting Submission event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.Submission()
            .processReceipt(tx_receipt)
        )

    def get_time_lock_change_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TimeLockChange event.

        :param tx_hash: hash of transaction emitting TimeLockChange event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AssetProxyOwner.abi(),
            )
            .events.TimeLockChange()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"bytes4[]","name":"_functionSelectors","type":"bytes4[]"},{"internalType":"address[]","name":"_destinations","type":"address[]"},{"internalType":"uint128[]","name":"_functionCallTimeLockSeconds","type":"uint128[]"},{"internalType":"address[]","name":"_owners","type":"address[]"},{"internalType":"uint256","name":"_required","type":"uint256"},{"internalType":"uint256","name":"_defaultSecondsTimeLocked","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"Confirmation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"transactionId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"confirmationTime","type":"uint256"}],"name":"ConfirmationTimeSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"Execution","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"ExecutionFailure","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"indexed":false,"internalType":"address","name":"destination","type":"address"},{"indexed":false,"internalType":"bool","name":"hasCustomTimeLock","type":"bool"},{"indexed":false,"internalType":"uint128","name":"newSecondsTimeLocked","type":"uint128"}],"name":"FunctionCallTimeLockRegistration","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"}],"name":"OwnerAddition","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"}],"name":"OwnerRemoval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"required","type":"uint256"}],"name":"RequirementChange","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"Revocation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"Submission","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"secondsTimeLocked","type":"uint256"}],"name":"TimeLockChange","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":true,"inputs":[],"name":"MAX_OWNER_COUNT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"addOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_required","type":"uint256"}],"name":"changeRequirement","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_secondsTimeLocked","type":"uint256"}],"name":"changeTimeLock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"confirmTransaction","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"confirmationTimes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"},{"internalType":"address","name":"index_1","type":"address"}],"name":"confirmations","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"executeTransaction","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes4","name":"index_0","type":"bytes4"},{"internalType":"address","name":"index_1","type":"address"}],"name":"functionCallTimeLocks","outputs":[{"internalType":"bool","name":"hasCustomTimeLock","type":"bool"},{"internalType":"uint128","name":"secondsTimeLocked","type":"uint128"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"getConfirmationCount","outputs":[{"internalType":"uint256","name":"count","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"getConfirmations","outputs":[{"internalType":"address[]","name":"_confirmations","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getOwners","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bool","name":"pending","type":"bool"},{"internalType":"bool","name":"executed","type":"bool"}],"name":"getTransactionCount","outputs":[{"internalType":"uint256","name":"count","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"from","type":"uint256"},{"internalType":"uint256","name":"to","type":"uint256"},{"internalType":"bool","name":"pending","type":"bool"},{"internalType":"bool","name":"executed","type":"bool"}],"name":"getTransactionIds","outputs":[{"internalType":"uint256[]","name":"_transactionIds","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"isConfirmed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"owners","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bool","name":"hasCustomTimeLock","type":"bool"},{"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"internalType":"address","name":"destination","type":"address"},{"internalType":"uint128","name":"newSecondsTimeLocked","type":"uint128"}],"name":"registerFunctionCall","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"removeOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"newOwner","type":"address"}],"name":"replaceOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"required","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"transactionId","type":"uint256"}],"name":"revokeConfirmation","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"secondsTimeLocked","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"destination","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"submitTransaction","outputs":[{"internalType":"uint256","name":"transactionId","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"transactionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"transactions","outputs":[{"internalType":"address","name":"destination","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"},{"internalType":"bool","name":"executed","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
