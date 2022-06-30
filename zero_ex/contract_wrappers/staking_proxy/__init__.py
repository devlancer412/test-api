"""Generated wrapper for StakingProxy Solidity contract."""

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
# constructor for StakingProxy below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        StakingProxyValidator,
    )
except ImportError:

    class StakingProxyValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class AddAuthorizedAddressMethod(ContractMethod):
    """Various interfaces to the addAuthorizedAddress method."""

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

    def validate_and_normalize_inputs(self, target: str):
        """Validate the inputs to the addAuthorizedAddress method."""
        self.validator.assert_valid(
            method_name="addAuthorizedAddress",
            parameter_name="target",
            argument_value=target,
        )
        target = self.validate_and_checksum_address(target)
        return target

    def call(self, target: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Authorizes an address.

        :param target: Address to authorize.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (target) = self.validate_and_normalize_inputs(target)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(target).call(tx_params.as_dict())

    def send_transaction(
        self, target: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Authorizes an address.

        :param target: Address to authorize.
        :param tx_params: transaction parameters
        """
        (target) = self.validate_and_normalize_inputs(target)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target).transact(tx_params.as_dict())

    def build_transaction(
        self, target: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (target) = self.validate_and_normalize_inputs(target)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, target: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (target) = self.validate_and_normalize_inputs(target)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target).estimateGas(tx_params.as_dict())


class AggregatedStatsByEpochMethod(ContractMethod):
    """Various interfaces to the aggregatedStatsByEpoch method."""

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
        """Validate the inputs to the aggregatedStatsByEpoch method."""
        self.validator.assert_valid(
            method_name="aggregatedStatsByEpoch",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int, int, int, int]:
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
            returned[4],
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


class AssertValidStorageParamsMethod(ContractMethod):
    """Various interfaces to the assertValidStorageParams method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Asserts that an epoch is between 5 and 30 days long.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class AttachStakingContractMethod(ContractMethod):
    """Various interfaces to the attachStakingContract method."""

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

    def validate_and_normalize_inputs(self, _staking_contract: str):
        """Validate the inputs to the attachStakingContract method."""
        self.validator.assert_valid(
            method_name="attachStakingContract",
            parameter_name="_stakingContract",
            argument_value=_staking_contract,
        )
        _staking_contract = self.validate_and_checksum_address(
            _staking_contract
        )
        return _staking_contract

    def call(
        self, _staking_contract: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Attach a staking contract; future calls will be delegated to the
        staking contract. Note that this is callable only by an authorized
        address.

        :param _stakingContract: Address of staking contract.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_staking_contract) = self.validate_and_normalize_inputs(
            _staking_contract
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_staking_contract).call(tx_params.as_dict())

    def send_transaction(
        self, _staking_contract: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Attach a staking contract; future calls will be delegated to the
        staking contract. Note that this is callable only by an authorized
        address.

        :param _stakingContract: Address of staking contract.
        :param tx_params: transaction parameters
        """
        (_staking_contract) = self.validate_and_normalize_inputs(
            _staking_contract
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_staking_contract).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _staking_contract: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_staking_contract) = self.validate_and_normalize_inputs(
            _staking_contract
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_staking_contract).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _staking_contract: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_staking_contract) = self.validate_and_normalize_inputs(
            _staking_contract
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_staking_contract).estimateGas(
            tx_params.as_dict()
        )


class AuthoritiesMethod(ContractMethod):
    """Various interfaces to the authorities method."""

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
        """Validate the inputs to the authorities method."""
        self.validator.assert_valid(
            method_name="authorities",
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


class AuthorizedMethod(ContractMethod):
    """Various interfaces to the authorized method."""

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
        """Validate the inputs to the authorized method."""
        self.validator.assert_valid(
            method_name="authorized",
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


class BatchExecuteMethod(ContractMethod):
    """Various interfaces to the batchExecute method."""

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

    def validate_and_normalize_inputs(self, data: List[Union[bytes, str]]):
        """Validate the inputs to the batchExecute method."""
        self.validator.assert_valid(
            method_name="batchExecute",
            parameter_name="data",
            argument_value=data,
        )
        return data

    def call(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        Batch executes a series of calls to the staking contract.

        :param data: An array of data that encodes a sequence of functions to
                      call in the staking contracts.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Batch executes a series of calls to the staking contract.

        :param data: An array of data that encodes a sequence of functions to
                      call in the staking contracts.
        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())


class CobbDouglasAlphaDenominatorMethod(ContractMethod):
    """Various interfaces to the cobbDouglasAlphaDenominator method."""

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


class CobbDouglasAlphaNumeratorMethod(ContractMethod):
    """Various interfaces to the cobbDouglasAlphaNumerator method."""

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


class CurrentEpochMethod(ContractMethod):
    """Various interfaces to the currentEpoch method."""

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


class CurrentEpochStartTimeInSecondsMethod(ContractMethod):
    """Various interfaces to the currentEpochStartTimeInSeconds method."""

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


class DetachStakingContractMethod(ContractMethod):
    """Various interfaces to the detachStakingContract method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Detach the current staking contract. Note that this is callable only by
        an authorized address.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Detach the current staking contract. Note that this is callable only by
        an authorized address.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class EpochDurationInSecondsMethod(ContractMethod):
    """Various interfaces to the epochDurationInSeconds method."""

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


class GetAuthorizedAddressesMethod(ContractMethod):
    """Various interfaces to the getAuthorizedAddresses method."""

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

        Gets all authorized addresses.

        :param tx_params: transaction parameters
        :returns: Array of authorized addresses.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [str(element) for element in returned]

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class LastPoolIdMethod(ContractMethod):
    """Various interfaces to the lastPoolId method."""

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


class MinimumPoolStakeMethod(ContractMethod):
    """Various interfaces to the minimumPoolStake method."""

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


class PoolIdByMakerMethod(ContractMethod):
    """Various interfaces to the poolIdByMaker method."""

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
        """Validate the inputs to the poolIdByMaker method."""
        self.validator.assert_valid(
            method_name="poolIdByMaker",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class PoolStatsByEpochMethod(ContractMethod):
    """Various interfaces to the poolStatsByEpoch method."""

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
        self, index_0: Union[bytes, str], index_1: int
    ):
        """Validate the inputs to the poolStatsByEpoch method."""
        self.validator.assert_valid(
            method_name="poolStatsByEpoch",
            parameter_name="index_0",
            argument_value=index_0,
        )
        self.validator.assert_valid(
            method_name="poolStatsByEpoch",
            parameter_name="index_1",
            argument_value=index_1,
        )
        # safeguard against fractional inputs
        index_1 = int(index_1)
        return (index_0, index_1)

    def call(
        self,
        index_0: Union[bytes, str],
        index_1: int,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[int, int, int]:
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
            returned[2],
        )

    def estimate_gas(
        self,
        index_0: Union[bytes, str],
        index_1: int,
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


class RemoveAuthorizedAddressMethod(ContractMethod):
    """Various interfaces to the removeAuthorizedAddress method."""

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

    def validate_and_normalize_inputs(self, target: str):
        """Validate the inputs to the removeAuthorizedAddress method."""
        self.validator.assert_valid(
            method_name="removeAuthorizedAddress",
            parameter_name="target",
            argument_value=target,
        )
        target = self.validate_and_checksum_address(target)
        return target

    def call(self, target: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Removes authorizion of an address.

        :param target: Address to remove authorization from.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (target) = self.validate_and_normalize_inputs(target)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(target).call(tx_params.as_dict())

    def send_transaction(
        self, target: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Removes authorizion of an address.

        :param target: Address to remove authorization from.
        :param tx_params: transaction parameters
        """
        (target) = self.validate_and_normalize_inputs(target)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target).transact(tx_params.as_dict())

    def build_transaction(
        self, target: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (target) = self.validate_and_normalize_inputs(target)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, target: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (target) = self.validate_and_normalize_inputs(target)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target).estimateGas(tx_params.as_dict())


class RemoveAuthorizedAddressAtIndexMethod(ContractMethod):
    """Various interfaces to the removeAuthorizedAddressAtIndex method."""

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

    def validate_and_normalize_inputs(self, target: str, index: int):
        """Validate the inputs to the removeAuthorizedAddressAtIndex method."""
        self.validator.assert_valid(
            method_name="removeAuthorizedAddressAtIndex",
            parameter_name="target",
            argument_value=target,
        )
        target = self.validate_and_checksum_address(target)
        self.validator.assert_valid(
            method_name="removeAuthorizedAddressAtIndex",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (target, index)

    def call(
        self, target: str, index: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Removes authorizion of an address.

        :param index: Index of target in authorities array.
        :param target: Address to remove authorization from.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (target, index) = self.validate_and_normalize_inputs(target, index)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(target, index).call(tx_params.as_dict())

    def send_transaction(
        self, target: str, index: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Removes authorizion of an address.

        :param index: Index of target in authorities array.
        :param target: Address to remove authorization from.
        :param tx_params: transaction parameters
        """
        (target, index) = self.validate_and_normalize_inputs(target, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target, index).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, target: str, index: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (target, index) = self.validate_and_normalize_inputs(target, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target, index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, target: str, index: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (target, index) = self.validate_and_normalize_inputs(target, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target, index).estimateGas(
            tx_params.as_dict()
        )


class RewardDelegatedStakeWeightMethod(ContractMethod):
    """Various interfaces to the rewardDelegatedStakeWeight method."""

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


class RewardsByPoolIdMethod(ContractMethod):
    """Various interfaces to the rewardsByPoolId method."""

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
        """Validate the inputs to the rewardsByPoolId method."""
        self.validator.assert_valid(
            method_name="rewardsByPoolId",
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


class StakingContractMethod(ContractMethod):
    """Various interfaces to the stakingContract method."""

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


class ValidExchangesMethod(ContractMethod):
    """Various interfaces to the validExchanges method."""

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
        """Validate the inputs to the validExchanges method."""
        self.validator.assert_valid(
            method_name="validExchanges",
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


class WethReservedForPoolRewardsMethod(ContractMethod):
    """Various interfaces to the wethReservedForPoolRewards method."""

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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class StakingProxy:
    """Wrapper class for StakingProxy Solidity contract."""

    add_authorized_address: AddAuthorizedAddressMethod
    """Constructor-initialized instance of
    :class:`AddAuthorizedAddressMethod`.
    """

    aggregated_stats_by_epoch: AggregatedStatsByEpochMethod
    """Constructor-initialized instance of
    :class:`AggregatedStatsByEpochMethod`.
    """

    assert_valid_storage_params: AssertValidStorageParamsMethod
    """Constructor-initialized instance of
    :class:`AssertValidStorageParamsMethod`.
    """

    attach_staking_contract: AttachStakingContractMethod
    """Constructor-initialized instance of
    :class:`AttachStakingContractMethod`.
    """

    authorities: AuthoritiesMethod
    """Constructor-initialized instance of
    :class:`AuthoritiesMethod`.
    """

    authorized: AuthorizedMethod
    """Constructor-initialized instance of
    :class:`AuthorizedMethod`.
    """

    batch_execute: BatchExecuteMethod
    """Constructor-initialized instance of
    :class:`BatchExecuteMethod`.
    """

    cobb_douglas_alpha_denominator: CobbDouglasAlphaDenominatorMethod
    """Constructor-initialized instance of
    :class:`CobbDouglasAlphaDenominatorMethod`.
    """

    cobb_douglas_alpha_numerator: CobbDouglasAlphaNumeratorMethod
    """Constructor-initialized instance of
    :class:`CobbDouglasAlphaNumeratorMethod`.
    """

    current_epoch: CurrentEpochMethod
    """Constructor-initialized instance of
    :class:`CurrentEpochMethod`.
    """

    current_epoch_start_time_in_seconds: CurrentEpochStartTimeInSecondsMethod
    """Constructor-initialized instance of
    :class:`CurrentEpochStartTimeInSecondsMethod`.
    """

    detach_staking_contract: DetachStakingContractMethod
    """Constructor-initialized instance of
    :class:`DetachStakingContractMethod`.
    """

    epoch_duration_in_seconds: EpochDurationInSecondsMethod
    """Constructor-initialized instance of
    :class:`EpochDurationInSecondsMethod`.
    """

    get_authorized_addresses: GetAuthorizedAddressesMethod
    """Constructor-initialized instance of
    :class:`GetAuthorizedAddressesMethod`.
    """

    last_pool_id: LastPoolIdMethod
    """Constructor-initialized instance of
    :class:`LastPoolIdMethod`.
    """

    minimum_pool_stake: MinimumPoolStakeMethod
    """Constructor-initialized instance of
    :class:`MinimumPoolStakeMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    pool_id_by_maker: PoolIdByMakerMethod
    """Constructor-initialized instance of
    :class:`PoolIdByMakerMethod`.
    """

    pool_stats_by_epoch: PoolStatsByEpochMethod
    """Constructor-initialized instance of
    :class:`PoolStatsByEpochMethod`.
    """

    remove_authorized_address: RemoveAuthorizedAddressMethod
    """Constructor-initialized instance of
    :class:`RemoveAuthorizedAddressMethod`.
    """

    remove_authorized_address_at_index: RemoveAuthorizedAddressAtIndexMethod
    """Constructor-initialized instance of
    :class:`RemoveAuthorizedAddressAtIndexMethod`.
    """

    reward_delegated_stake_weight: RewardDelegatedStakeWeightMethod
    """Constructor-initialized instance of
    :class:`RewardDelegatedStakeWeightMethod`.
    """

    rewards_by_pool_id: RewardsByPoolIdMethod
    """Constructor-initialized instance of
    :class:`RewardsByPoolIdMethod`.
    """

    staking_contract: StakingContractMethod
    """Constructor-initialized instance of
    :class:`StakingContractMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    valid_exchanges: ValidExchangesMethod
    """Constructor-initialized instance of
    :class:`ValidExchangesMethod`.
    """

    weth_reserved_for_pool_rewards: WethReservedForPoolRewardsMethod
    """Constructor-initialized instance of
    :class:`WethReservedForPoolRewardsMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: StakingProxyValidator = None,
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
            validator = StakingProxyValidator(
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
            abi=StakingProxy.abi(),
        ).functions

        self.add_authorized_address = AddAuthorizedAddressMethod(
            web3_or_provider,
            contract_address,
            functions.addAuthorizedAddress,
            validator,
        )

        self.aggregated_stats_by_epoch = AggregatedStatsByEpochMethod(
            web3_or_provider,
            contract_address,
            functions.aggregatedStatsByEpoch,
            validator,
        )

        self.assert_valid_storage_params = AssertValidStorageParamsMethod(
            web3_or_provider,
            contract_address,
            functions.assertValidStorageParams,
        )

        self.attach_staking_contract = AttachStakingContractMethod(
            web3_or_provider,
            contract_address,
            functions.attachStakingContract,
            validator,
        )

        self.authorities = AuthoritiesMethod(
            web3_or_provider,
            contract_address,
            functions.authorities,
            validator,
        )

        self.authorized = AuthorizedMethod(
            web3_or_provider, contract_address, functions.authorized, validator
        )

        self.batch_execute = BatchExecuteMethod(
            web3_or_provider,
            contract_address,
            functions.batchExecute,
            validator,
        )

        self.cobb_douglas_alpha_denominator = CobbDouglasAlphaDenominatorMethod(
            web3_or_provider,
            contract_address,
            functions.cobbDouglasAlphaDenominator,
        )

        self.cobb_douglas_alpha_numerator = CobbDouglasAlphaNumeratorMethod(
            web3_or_provider,
            contract_address,
            functions.cobbDouglasAlphaNumerator,
        )

        self.current_epoch = CurrentEpochMethod(
            web3_or_provider, contract_address, functions.currentEpoch
        )

        self.current_epoch_start_time_in_seconds = CurrentEpochStartTimeInSecondsMethod(
            web3_or_provider,
            contract_address,
            functions.currentEpochStartTimeInSeconds,
        )

        self.detach_staking_contract = DetachStakingContractMethod(
            web3_or_provider, contract_address, functions.detachStakingContract
        )

        self.epoch_duration_in_seconds = EpochDurationInSecondsMethod(
            web3_or_provider,
            contract_address,
            functions.epochDurationInSeconds,
        )

        self.get_authorized_addresses = GetAuthorizedAddressesMethod(
            web3_or_provider,
            contract_address,
            functions.getAuthorizedAddresses,
        )

        self.last_pool_id = LastPoolIdMethod(
            web3_or_provider, contract_address, functions.lastPoolId
        )

        self.minimum_pool_stake = MinimumPoolStakeMethod(
            web3_or_provider, contract_address, functions.minimumPoolStake
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
        )

        self.pool_id_by_maker = PoolIdByMakerMethod(
            web3_or_provider,
            contract_address,
            functions.poolIdByMaker,
            validator,
        )

        self.pool_stats_by_epoch = PoolStatsByEpochMethod(
            web3_or_provider,
            contract_address,
            functions.poolStatsByEpoch,
            validator,
        )

        self.remove_authorized_address = RemoveAuthorizedAddressMethod(
            web3_or_provider,
            contract_address,
            functions.removeAuthorizedAddress,
            validator,
        )

        self.remove_authorized_address_at_index = RemoveAuthorizedAddressAtIndexMethod(
            web3_or_provider,
            contract_address,
            functions.removeAuthorizedAddressAtIndex,
            validator,
        )

        self.reward_delegated_stake_weight = RewardDelegatedStakeWeightMethod(
            web3_or_provider,
            contract_address,
            functions.rewardDelegatedStakeWeight,
        )

        self.rewards_by_pool_id = RewardsByPoolIdMethod(
            web3_or_provider,
            contract_address,
            functions.rewardsByPoolId,
            validator,
        )

        self.staking_contract = StakingContractMethod(
            web3_or_provider, contract_address, functions.stakingContract
        )

        self.transfer_ownership = TransferOwnershipMethod(
            web3_or_provider,
            contract_address,
            functions.transferOwnership,
            validator,
        )

        self.valid_exchanges = ValidExchangesMethod(
            web3_or_provider,
            contract_address,
            functions.validExchanges,
            validator,
        )

        self.weth_reserved_for_pool_rewards = WethReservedForPoolRewardsMethod(
            web3_or_provider,
            contract_address,
            functions.wethReservedForPoolRewards,
        )

    def get_authorized_address_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuthorizedAddressAdded event.

        :param tx_hash: hash of transaction emitting AuthorizedAddressAdded
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=StakingProxy.abi(),
            )
            .events.AuthorizedAddressAdded()
            .processReceipt(tx_receipt)
        )

    def get_authorized_address_removed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuthorizedAddressRemoved event.

        :param tx_hash: hash of transaction emitting AuthorizedAddressRemoved
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=StakingProxy.abi(),
            )
            .events.AuthorizedAddressRemoved()
            .processReceipt(tx_receipt)
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
                abi=StakingProxy.abi(),
            )
            .events.OwnershipTransferred()
            .processReceipt(tx_receipt)
        )

    def get_staking_contract_attached_to_proxy_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for StakingContractAttachedToProxy event.

        :param tx_hash: hash of transaction emitting
            StakingContractAttachedToProxy event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=StakingProxy.abi(),
            )
            .events.StakingContractAttachedToProxy()
            .processReceipt(tx_receipt)
        )

    def get_staking_contract_detached_from_proxy_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for StakingContractDetachedFromProxy event.

        :param tx_hash: hash of transaction emitting
            StakingContractDetachedFromProxy event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=StakingProxy.abi(),
            )
            .events.StakingContractDetachedFromProxy()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_stakingContract","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AuthorizedAddressAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AuthorizedAddressRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"newStakingContractAddress","type":"address"}],"name":"StakingContractAttachedToProxy","type":"event"},{"anonymous":false,"inputs":[],"name":"StakingContractDetachedFromProxy","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"addAuthorizedAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"aggregatedStatsByEpoch","outputs":[{"internalType":"uint256","name":"rewardsAvailable","type":"uint256"},{"internalType":"uint256","name":"numPoolsToFinalize","type":"uint256"},{"internalType":"uint256","name":"totalFeesCollected","type":"uint256"},{"internalType":"uint256","name":"totalWeightedStake","type":"uint256"},{"internalType":"uint256","name":"totalRewardsFinalized","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"assertValidStorageParams","outputs":[],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_stakingContract","type":"address"}],"name":"attachStakingContract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"authorities","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"authorized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"batchExecute","outputs":[{"internalType":"bytes[]","name":"batchReturnData","type":"bytes[]"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"cobbDouglasAlphaDenominator","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"cobbDouglasAlphaNumerator","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"currentEpoch","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"currentEpochStartTimeInSeconds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"detachStakingContract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"epochDurationInSeconds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAuthorizedAddresses","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastPoolId","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"minimumPoolStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"poolIdByMaker","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"},{"internalType":"uint256","name":"index_1","type":"uint256"}],"name":"poolStatsByEpoch","outputs":[{"internalType":"uint256","name":"feesCollected","type":"uint256"},{"internalType":"uint256","name":"weightedStake","type":"uint256"},{"internalType":"uint256","name":"membersStake","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"removeAuthorizedAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"removeAuthorizedAddressAtIndex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"rewardDelegatedStakeWeight","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"rewardsByPoolId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"stakingContract","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"validExchanges","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"wethReservedForPoolRewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
