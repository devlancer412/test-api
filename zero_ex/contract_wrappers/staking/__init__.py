"""Generated wrapper for Staking Solidity contract."""

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
# constructor for Staking below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        StakingValidator,
    )
except ImportError:

    class StakingValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IStructsStoredBalance(TypedDict):
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

    currentEpoch: int

    currentEpochBalance: int

    nextEpochBalance: int


class IStructsPool(TypedDict):
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

    operator: str

    operatorShare: int


class IStructsPoolStats(TypedDict):
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

    feesCollected: int

    weightedStake: int

    membersStake: int


class IStructsStakeInfo(TypedDict):
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

    status: int

    poolId: Union[bytes, str]


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


class AddExchangeAddressMethod(ContractMethod):
    """Various interfaces to the addExchangeAddress method."""

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

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the addExchangeAddress method."""
        self.validator.assert_valid(
            method_name="addExchangeAddress",
            parameter_name="addr",
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return addr

    def call(self, addr: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Adds a new exchange address

        :param addr: Address of exchange contract to add
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(addr).call(tx_params.as_dict())

    def send_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Adds a new exchange address

        :param addr: Address of exchange contract to add
        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


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


class ComputeRewardBalanceOfDelegatorMethod(ContractMethod):
    """Various interfaces to the computeRewardBalanceOfDelegator method."""

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
        self, pool_id: Union[bytes, str], member: str
    ):
        """Validate the inputs to the computeRewardBalanceOfDelegator method."""
        self.validator.assert_valid(
            method_name="computeRewardBalanceOfDelegator",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        self.validator.assert_valid(
            method_name="computeRewardBalanceOfDelegator",
            parameter_name="member",
            argument_value=member,
        )
        member = self.validate_and_checksum_address(member)
        return (pool_id, member)

    def call(
        self,
        pool_id: Union[bytes, str],
        member: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        Computes the reward balance in ETH of a specific member of a pool.

        :param member: The member of the pool.
        :param poolId: Unique id of pool.
        :param tx_params: transaction parameters
        :returns: totalReward Balance in ETH.
        """
        (pool_id, member) = self.validate_and_normalize_inputs(pool_id, member)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(pool_id, member).call(
            tx_params.as_dict()
        )
        return int(returned)

    def estimate_gas(
        self,
        pool_id: Union[bytes, str],
        member: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id, member) = self.validate_and_normalize_inputs(pool_id, member)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id, member).estimateGas(
            tx_params.as_dict()
        )


class ComputeRewardBalanceOfOperatorMethod(ContractMethod):
    """Various interfaces to the computeRewardBalanceOfOperator method."""

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

    def validate_and_normalize_inputs(self, pool_id: Union[bytes, str]):
        """Validate the inputs to the computeRewardBalanceOfOperator method."""
        self.validator.assert_valid(
            method_name="computeRewardBalanceOfOperator",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        return pool_id

    def call(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        Computes the reward balance in ETH of the operator of a pool.

        :param poolId: Unique id of pool.
        :param tx_params: transaction parameters
        :returns: totalReward Balance in ETH.
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(pool_id).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).estimateGas(
            tx_params.as_dict()
        )


class CreateStakingPoolMethod(ContractMethod):
    """Various interfaces to the createStakingPool method."""

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
        self, operator_share: int, add_operator_as_maker: bool
    ):
        """Validate the inputs to the createStakingPool method."""
        self.validator.assert_valid(
            method_name="createStakingPool",
            parameter_name="operatorShare",
            argument_value=operator_share,
        )
        self.validator.assert_valid(
            method_name="createStakingPool",
            parameter_name="addOperatorAsMaker",
            argument_value=add_operator_as_maker,
        )
        return (operator_share, add_operator_as_maker)

    def call(
        self,
        operator_share: int,
        add_operator_as_maker: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Create a new staking pool. The sender will be the operator of this
        pool. Note that an operator must be payable.

        :param addOperatorAsMaker: Adds operator to the created pool as a maker
            for convenience iff true.
        :param operatorShare: Portion of rewards owned by the operator, in ppm.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            operator_share,
            add_operator_as_maker,
        ) = self.validate_and_normalize_inputs(
            operator_share, add_operator_as_maker
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            operator_share, add_operator_as_maker
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        operator_share: int,
        add_operator_as_maker: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Create a new staking pool. The sender will be the operator of this
        pool. Note that an operator must be payable.

        :param addOperatorAsMaker: Adds operator to the created pool as a maker
            for convenience iff true.
        :param operatorShare: Portion of rewards owned by the operator, in ppm.
        :param tx_params: transaction parameters
        """
        (
            operator_share,
            add_operator_as_maker,
        ) = self.validate_and_normalize_inputs(
            operator_share, add_operator_as_maker
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator_share, add_operator_as_maker
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        operator_share: int,
        add_operator_as_maker: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            operator_share,
            add_operator_as_maker,
        ) = self.validate_and_normalize_inputs(
            operator_share, add_operator_as_maker
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator_share, add_operator_as_maker
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        operator_share: int,
        add_operator_as_maker: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            operator_share,
            add_operator_as_maker,
        ) = self.validate_and_normalize_inputs(
            operator_share, add_operator_as_maker
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator_share, add_operator_as_maker
        ).estimateGas(tx_params.as_dict())


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


class DecreaseStakingPoolOperatorShareMethod(ContractMethod):
    """Various interfaces to the decreaseStakingPoolOperatorShare method."""

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
        self, pool_id: Union[bytes, str], new_operator_share: int
    ):
        """Validate the inputs to the decreaseStakingPoolOperatorShare method."""
        self.validator.assert_valid(
            method_name="decreaseStakingPoolOperatorShare",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        self.validator.assert_valid(
            method_name="decreaseStakingPoolOperatorShare",
            parameter_name="newOperatorShare",
            argument_value=new_operator_share,
        )
        return (pool_id, new_operator_share)

    def call(
        self,
        pool_id: Union[bytes, str],
        new_operator_share: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Decreases the operator share for the given pool (i.e. increases pool
        rewards for members).

        :param newOperatorShare: The newly decreased percentage of any rewards
            owned by the operator.
        :param poolId: Unique Id of pool.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (pool_id, new_operator_share) = self.validate_and_normalize_inputs(
            pool_id, new_operator_share
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(pool_id, new_operator_share).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        pool_id: Union[bytes, str],
        new_operator_share: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Decreases the operator share for the given pool (i.e. increases pool
        rewards for members).

        :param newOperatorShare: The newly decreased percentage of any rewards
            owned by the operator.
        :param poolId: Unique Id of pool.
        :param tx_params: transaction parameters
        """
        (pool_id, new_operator_share) = self.validate_and_normalize_inputs(
            pool_id, new_operator_share
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id, new_operator_share).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        pool_id: Union[bytes, str],
        new_operator_share: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (pool_id, new_operator_share) = self.validate_and_normalize_inputs(
            pool_id, new_operator_share
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            pool_id, new_operator_share
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        pool_id: Union[bytes, str],
        new_operator_share: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id, new_operator_share) = self.validate_and_normalize_inputs(
            pool_id, new_operator_share
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            pool_id, new_operator_share
        ).estimateGas(tx_params.as_dict())


class EndEpochMethod(ContractMethod):
    """Various interfaces to the endEpoch method."""

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

        Begins a new epoch, preparing the prior one for finalization. Throws if
        not enough time has passed between epochs or if the previous epoch was
        not fully finalized.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Begins a new epoch, preparing the prior one for finalization. Throws if
        not enough time has passed between epochs or if the previous epoch was
        not fully finalized.

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


class FinalizePoolMethod(ContractMethod):
    """Various interfaces to the finalizePool method."""

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

    def validate_and_normalize_inputs(self, pool_id: Union[bytes, str]):
        """Validate the inputs to the finalizePool method."""
        self.validator.assert_valid(
            method_name="finalizePool",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        return pool_id

    def call(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Instantly finalizes a single pool that earned rewards in the previous
        epoch, crediting it rewards for members and withdrawing operator's
        rewards as WETH. This can be called by internal functions that need to
        finalize a pool immediately. Does nothing if the pool is already
        finalized or did not earn rewards in the previous epoch.

        :param poolId: The pool ID to finalize.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(pool_id).call(tx_params.as_dict())

    def send_transaction(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Instantly finalizes a single pool that earned rewards in the previous
        epoch, crediting it rewards for members and withdrawing operator's
        rewards as WETH. This can be called by internal functions that need to
        finalize a pool immediately. Does nothing if the pool is already
        finalized or did not earn rewards in the previous epoch.

        :param poolId: The pool ID to finalize.
        :param tx_params: transaction parameters
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).transact(tx_params.as_dict())

    def build_transaction(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).estimateGas(
            tx_params.as_dict()
        )


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


class GetCurrentEpochEarliestEndTimeInSecondsMethod(ContractMethod):
    """Various interfaces to the getCurrentEpochEarliestEndTimeInSeconds method."""

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

        Returns the earliest end time in seconds of this epoch. The next epoch
        can begin once this time is reached. Epoch period =
        [startTimeInSeconds..endTimeInSeconds)

        :param tx_params: transaction parameters
        :returns: Time in seconds.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class GetGlobalStakeByStatusMethod(ContractMethod):
    """Various interfaces to the getGlobalStakeByStatus method."""

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

    def validate_and_normalize_inputs(self, stake_status: int):
        """Validate the inputs to the getGlobalStakeByStatus method."""
        self.validator.assert_valid(
            method_name="getGlobalStakeByStatus",
            parameter_name="stakeStatus",
            argument_value=stake_status,
        )
        return stake_status

    def call(
        self, stake_status: int, tx_params: Optional[TxParams] = None
    ) -> IStructsStoredBalance:
        """Execute underlying contract method via eth_call.

        Gets global stake for a given status.

        :param stakeStatus: UNDELEGATED or DELEGATED
        :param tx_params: transaction parameters
        :returns: Global stake for given status.
        """
        (stake_status) = self.validate_and_normalize_inputs(stake_status)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(stake_status).call(
            tx_params.as_dict()
        )
        return IStructsStoredBalance(
            currentEpoch=returned[0],
            currentEpochBalance=returned[1],
            nextEpochBalance=returned[2],
        )

    def estimate_gas(
        self, stake_status: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (stake_status) = self.validate_and_normalize_inputs(stake_status)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(stake_status).estimateGas(
            tx_params.as_dict()
        )


class GetOwnerStakeByStatusMethod(ContractMethod):
    """Various interfaces to the getOwnerStakeByStatus method."""

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

    def validate_and_normalize_inputs(self, staker: str, stake_status: int):
        """Validate the inputs to the getOwnerStakeByStatus method."""
        self.validator.assert_valid(
            method_name="getOwnerStakeByStatus",
            parameter_name="staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        self.validator.assert_valid(
            method_name="getOwnerStakeByStatus",
            parameter_name="stakeStatus",
            argument_value=stake_status,
        )
        return (staker, stake_status)

    def call(
        self,
        staker: str,
        stake_status: int,
        tx_params: Optional[TxParams] = None,
    ) -> IStructsStoredBalance:
        """Execute underlying contract method via eth_call.

        Gets an owner's stake balances by status.

        :param stakeStatus: UNDELEGATED or DELEGATED
        :param staker: Owner of stake.
        :param tx_params: transaction parameters
        :returns: Owner's stake balances for given status.
        """
        (staker, stake_status) = self.validate_and_normalize_inputs(
            staker, stake_status
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(staker, stake_status).call(
            tx_params.as_dict()
        )
        return IStructsStoredBalance(
            currentEpoch=returned[0],
            currentEpochBalance=returned[1],
            nextEpochBalance=returned[2],
        )

    def estimate_gas(
        self,
        staker: str,
        stake_status: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (staker, stake_status) = self.validate_and_normalize_inputs(
            staker, stake_status
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker, stake_status).estimateGas(
            tx_params.as_dict()
        )


class GetParamsMethod(ContractMethod):
    """Various interfaces to the getParams method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(
        self, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int, int, int, int]:
        """Execute underlying contract method via eth_call.

        Retrieves all configurable parameter values.

        :param tx_params: transaction parameters
        :returns: _epochDurationInSeconds Minimum seconds between
            epochs._rewardDelegatedStakeWeight How much delegated stake is
            weighted vs operator stake, in ppm._minimumPoolStake Minimum amount
            of stake required in a pool to collect
            rewards._cobbDouglasAlphaNumerator Numerator for cobb douglas alpha
            factor._cobbDouglasAlphaDenominator Denominator for cobb douglas
            alpha factor.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
            returned[4],
        )

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class GetStakeDelegatedToPoolByOwnerMethod(ContractMethod):
    """Various interfaces to the getStakeDelegatedToPoolByOwner method."""

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
        self, staker: str, pool_id: Union[bytes, str]
    ):
        """Validate the inputs to the getStakeDelegatedToPoolByOwner method."""
        self.validator.assert_valid(
            method_name="getStakeDelegatedToPoolByOwner",
            parameter_name="staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        self.validator.assert_valid(
            method_name="getStakeDelegatedToPoolByOwner",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        return (staker, pool_id)

    def call(
        self,
        staker: str,
        pool_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> IStructsStoredBalance:
        """Execute underlying contract method via eth_call.

        Returns the stake delegated to a specific staking pool, by a given
        staker.

        :param poolId: Unique Id of pool.
        :param staker: of stake.
        :param tx_params: transaction parameters
        :returns: Stake delegated to pool by staker.
        """
        (staker, pool_id) = self.validate_and_normalize_inputs(staker, pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(staker, pool_id).call(
            tx_params.as_dict()
        )
        return IStructsStoredBalance(
            currentEpoch=returned[0],
            currentEpochBalance=returned[1],
            nextEpochBalance=returned[2],
        )

    def estimate_gas(
        self,
        staker: str,
        pool_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (staker, pool_id) = self.validate_and_normalize_inputs(staker, pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker, pool_id).estimateGas(
            tx_params.as_dict()
        )


class GetStakingPoolMethod(ContractMethod):
    """Various interfaces to the getStakingPool method."""

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

    def validate_and_normalize_inputs(self, pool_id: Union[bytes, str]):
        """Validate the inputs to the getStakingPool method."""
        self.validator.assert_valid(
            method_name="getStakingPool",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        return pool_id

    def call(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> IStructsPool:
        """Execute underlying contract method via eth_call.

        Returns a staking pool

        :param poolId: Unique id of pool.
        :param tx_params: transaction parameters

        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(pool_id).call(tx_params.as_dict())
        return IStructsPool(operator=returned[0], operatorShare=returned[1],)

    def estimate_gas(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).estimateGas(
            tx_params.as_dict()
        )


class GetStakingPoolStatsThisEpochMethod(ContractMethod):
    """Various interfaces to the getStakingPoolStatsThisEpoch method."""

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

    def validate_and_normalize_inputs(self, pool_id: Union[bytes, str]):
        """Validate the inputs to the getStakingPoolStatsThisEpoch method."""
        self.validator.assert_valid(
            method_name="getStakingPoolStatsThisEpoch",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        return pool_id

    def call(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> IStructsPoolStats:
        """Execute underlying contract method via eth_call.

        Get stats on a staking pool in this epoch.

        :param poolId: Pool Id to query.
        :param tx_params: transaction parameters
        :returns: PoolStats struct for pool id.
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(pool_id).call(tx_params.as_dict())
        return IStructsPoolStats(
            feesCollected=returned[0],
            weightedStake=returned[1],
            membersStake=returned[2],
        )

    def estimate_gas(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).estimateGas(
            tx_params.as_dict()
        )


class GetTotalStakeMethod(ContractMethod):
    """Various interfaces to the getTotalStake method."""

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

    def validate_and_normalize_inputs(self, staker: str):
        """Validate the inputs to the getTotalStake method."""
        self.validator.assert_valid(
            method_name="getTotalStake",
            parameter_name="staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        return staker

    def call(self, staker: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        Returns the total stake for a given staker.

        :param staker: of stake.
        :param tx_params: transaction parameters
        :returns: Total ZRX staked by `staker`.
        """
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(staker).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, staker: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker).estimateGas(tx_params.as_dict())


class GetTotalStakeDelegatedToPoolMethod(ContractMethod):
    """Various interfaces to the getTotalStakeDelegatedToPool method."""

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

    def validate_and_normalize_inputs(self, pool_id: Union[bytes, str]):
        """Validate the inputs to the getTotalStakeDelegatedToPool method."""
        self.validator.assert_valid(
            method_name="getTotalStakeDelegatedToPool",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        return pool_id

    def call(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> IStructsStoredBalance:
        """Execute underlying contract method via eth_call.

        Returns the total stake delegated to a specific staking pool, across
        all members.

        :param poolId: Unique Id of pool.
        :param tx_params: transaction parameters
        :returns: Total stake delegated to pool.
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(pool_id).call(tx_params.as_dict())
        return IStructsStoredBalance(
            currentEpoch=returned[0],
            currentEpochBalance=returned[1],
            nextEpochBalance=returned[2],
        )

    def estimate_gas(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).estimateGas(
            tx_params.as_dict()
        )


class GetWethContractMethod(ContractMethod):
    """Various interfaces to the getWethContract method."""

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

        Returns the current weth contract address

        :param tx_params: transaction parameters
        :returns: wethContract The WETH contract instance.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class GetZrxVaultMethod(ContractMethod):
    """Various interfaces to the getZrxVault method."""

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

        Returns the current zrxVault address.

        :param tx_params: transaction parameters
        :returns: zrxVault The zrxVault contract.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class InitMethod(ContractMethod):
    """Various interfaces to the init method."""

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

        Initialize storage owned by this contract. This function should not be
        called directly. The StakingProxy contract will call it in
        `attachStakingContract()`.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Initialize storage owned by this contract. This function should not be
        called directly. The StakingProxy contract will call it in
        `attachStakingContract()`.

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


class JoinStakingPoolAsMakerMethod(ContractMethod):
    """Various interfaces to the joinStakingPoolAsMaker method."""

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

    def validate_and_normalize_inputs(self, pool_id: Union[bytes, str]):
        """Validate the inputs to the joinStakingPoolAsMaker method."""
        self.validator.assert_valid(
            method_name="joinStakingPoolAsMaker",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        return pool_id

    def call(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Allows caller to join a staking pool as a maker.

        :param poolId: Unique id of pool.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(pool_id).call(tx_params.as_dict())

    def send_transaction(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Allows caller to join a staking pool as a maker.

        :param poolId: Unique id of pool.
        :param tx_params: transaction parameters
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).transact(tx_params.as_dict())

    def build_transaction(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).estimateGas(
            tx_params.as_dict()
        )


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


class MoveStakeMethod(ContractMethod):
    """Various interfaces to the moveStake method."""

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
        self, _from: IStructsStakeInfo, to: IStructsStakeInfo, amount: int
    ):
        """Validate the inputs to the moveStake method."""
        self.validator.assert_valid(
            method_name="moveStake",
            parameter_name="from",
            argument_value=_from,
        )
        self.validator.assert_valid(
            method_name="moveStake", parameter_name="to", argument_value=to,
        )
        self.validator.assert_valid(
            method_name="moveStake",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (_from, to, amount)

    def call(
        self,
        _from: IStructsStakeInfo,
        to: IStructsStakeInfo,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Moves stake between statuses: 'undelegated' or 'delegated'. Delegated
        stake can also be moved between pools. This change comes into effect
        next epoch.

        :param amount: of stake to move.
        :param from: status to move stake out of.
        :param to: status to move stake into.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, amount).call(tx_params.as_dict())

    def send_transaction(
        self,
        _from: IStructsStakeInfo,
        to: IStructsStakeInfo,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Moves stake between statuses: 'undelegated' or 'delegated'. Delegated
        stake can also be moved between pools. This change comes into effect
        next epoch.

        :param amount: of stake to move.
        :param from: status to move stake out of.
        :param to: status to move stake into.
        :param tx_params: transaction parameters
        """
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: IStructsStakeInfo,
        to: IStructsStakeInfo,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _from: IStructsStakeInfo,
        to: IStructsStakeInfo,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).estimateGas(
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


class PayProtocolFeeMethod(ContractMethod):
    """Various interfaces to the payProtocolFee method."""

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
        self, maker_address: str, payer_address: str, protocol_fee: int
    ):
        """Validate the inputs to the payProtocolFee method."""
        self.validator.assert_valid(
            method_name="payProtocolFee",
            parameter_name="makerAddress",
            argument_value=maker_address,
        )
        maker_address = self.validate_and_checksum_address(maker_address)
        self.validator.assert_valid(
            method_name="payProtocolFee",
            parameter_name="payerAddress",
            argument_value=payer_address,
        )
        payer_address = self.validate_and_checksum_address(payer_address)
        self.validator.assert_valid(
            method_name="payProtocolFee",
            parameter_name="protocolFee",
            argument_value=protocol_fee,
        )
        # safeguard against fractional inputs
        protocol_fee = int(protocol_fee)
        return (maker_address, payer_address, protocol_fee)

    def call(
        self,
        maker_address: str,
        payer_address: str,
        protocol_fee: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Pays a protocol fee in ETH or WETH. Only a known 0x exchange can call
        this method. See (MixinExchangeManager).

        :param makerAddress: The address of the order's maker.
        :param payerAddress: The address of the protocol fee payer.
        :param protocolFee: The protocol fee amount. This is either passed as
            ETH or transferred as WETH.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            maker_address,
            payer_address,
            protocol_fee,
        ) = self.validate_and_normalize_inputs(
            maker_address, payer_address, protocol_fee
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            maker_address, payer_address, protocol_fee
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        maker_address: str,
        payer_address: str,
        protocol_fee: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Pays a protocol fee in ETH or WETH. Only a known 0x exchange can call
        this method. See (MixinExchangeManager).

        :param makerAddress: The address of the order's maker.
        :param payerAddress: The address of the protocol fee payer.
        :param protocolFee: The protocol fee amount. This is either passed as
            ETH or transferred as WETH.
        :param tx_params: transaction parameters
        """
        (
            maker_address,
            payer_address,
            protocol_fee,
        ) = self.validate_and_normalize_inputs(
            maker_address, payer_address, protocol_fee
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            maker_address, payer_address, protocol_fee
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        maker_address: str,
        payer_address: str,
        protocol_fee: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            maker_address,
            payer_address,
            protocol_fee,
        ) = self.validate_and_normalize_inputs(
            maker_address, payer_address, protocol_fee
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            maker_address, payer_address, protocol_fee
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        maker_address: str,
        payer_address: str,
        protocol_fee: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            maker_address,
            payer_address,
            protocol_fee,
        ) = self.validate_and_normalize_inputs(
            maker_address, payer_address, protocol_fee
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            maker_address, payer_address, protocol_fee
        ).estimateGas(tx_params.as_dict())


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


class RemoveExchangeAddressMethod(ContractMethod):
    """Various interfaces to the removeExchangeAddress method."""

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

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the removeExchangeAddress method."""
        self.validator.assert_valid(
            method_name="removeExchangeAddress",
            parameter_name="addr",
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return addr

    def call(self, addr: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Removes an existing exchange address

        :param addr: Address of exchange contract to remove
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(addr).call(tx_params.as_dict())

    def send_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Removes an existing exchange address

        :param addr: Address of exchange contract to remove
        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


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


class SetParamsMethod(ContractMethod):
    """Various interfaces to the setParams method."""

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
        _epoch_duration_in_seconds: int,
        _reward_delegated_stake_weight: int,
        _minimum_pool_stake: int,
        _cobb_douglas_alpha_numerator: int,
        _cobb_douglas_alpha_denominator: int,
    ):
        """Validate the inputs to the setParams method."""
        self.validator.assert_valid(
            method_name="setParams",
            parameter_name="_epochDurationInSeconds",
            argument_value=_epoch_duration_in_seconds,
        )
        # safeguard against fractional inputs
        _epoch_duration_in_seconds = int(_epoch_duration_in_seconds)
        self.validator.assert_valid(
            method_name="setParams",
            parameter_name="_rewardDelegatedStakeWeight",
            argument_value=_reward_delegated_stake_weight,
        )
        self.validator.assert_valid(
            method_name="setParams",
            parameter_name="_minimumPoolStake",
            argument_value=_minimum_pool_stake,
        )
        # safeguard against fractional inputs
        _minimum_pool_stake = int(_minimum_pool_stake)
        self.validator.assert_valid(
            method_name="setParams",
            parameter_name="_cobbDouglasAlphaNumerator",
            argument_value=_cobb_douglas_alpha_numerator,
        )
        self.validator.assert_valid(
            method_name="setParams",
            parameter_name="_cobbDouglasAlphaDenominator",
            argument_value=_cobb_douglas_alpha_denominator,
        )
        return (
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        )

    def call(
        self,
        _epoch_duration_in_seconds: int,
        _reward_delegated_stake_weight: int,
        _minimum_pool_stake: int,
        _cobb_douglas_alpha_numerator: int,
        _cobb_douglas_alpha_denominator: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        Set all configurable parameters at once.

        :param _cobbDouglasAlphaDenominator: Denominator for cobb douglas alpha
            factor.
        :param _cobbDouglasAlphaNumerator: Numerator for cobb douglas alpha
            factor.
        :param _epochDurationInSeconds: Minimum seconds between epochs.
        :param _minimumPoolStake: Minimum amount of stake required in a pool to
            collect rewards.
        :param _rewardDelegatedStakeWeight: How much delegated stake is
            weighted vs operator stake, in ppm.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        ) = self.validate_and_normalize_inputs(
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        _epoch_duration_in_seconds: int,
        _reward_delegated_stake_weight: int,
        _minimum_pool_stake: int,
        _cobb_douglas_alpha_numerator: int,
        _cobb_douglas_alpha_denominator: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Set all configurable parameters at once.

        :param _cobbDouglasAlphaDenominator: Denominator for cobb douglas alpha
            factor.
        :param _cobbDouglasAlphaNumerator: Numerator for cobb douglas alpha
            factor.
        :param _epochDurationInSeconds: Minimum seconds between epochs.
        :param _minimumPoolStake: Minimum amount of stake required in a pool to
            collect rewards.
        :param _rewardDelegatedStakeWeight: How much delegated stake is
            weighted vs operator stake, in ppm.
        :param tx_params: transaction parameters
        """
        (
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        ) = self.validate_and_normalize_inputs(
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        _epoch_duration_in_seconds: int,
        _reward_delegated_stake_weight: int,
        _minimum_pool_stake: int,
        _cobb_douglas_alpha_numerator: int,
        _cobb_douglas_alpha_denominator: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        ) = self.validate_and_normalize_inputs(
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        _epoch_duration_in_seconds: int,
        _reward_delegated_stake_weight: int,
        _minimum_pool_stake: int,
        _cobb_douglas_alpha_numerator: int,
        _cobb_douglas_alpha_denominator: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        ) = self.validate_and_normalize_inputs(
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _epoch_duration_in_seconds,
            _reward_delegated_stake_weight,
            _minimum_pool_stake,
            _cobb_douglas_alpha_numerator,
            _cobb_douglas_alpha_denominator,
        ).estimateGas(tx_params.as_dict())


class StakeMethod(ContractMethod):
    """Various interfaces to the stake method."""

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

    def validate_and_normalize_inputs(self, amount: int):
        """Validate the inputs to the stake method."""
        self.validator.assert_valid(
            method_name="stake",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return amount

    def call(self, amount: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Stake ZRX tokens. Tokens are deposited into the ZRX Vault. Unstake to
        retrieve the ZRX. Stake is in the 'Active' status.

        :param amount: of ZRX to stake.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(amount).call(tx_params.as_dict())

    def send_transaction(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Stake ZRX tokens. Tokens are deposited into the ZRX Vault. Unstake to
        retrieve the ZRX. Stake is in the 'Active' status.

        :param amount: of ZRX to stake.
        :param tx_params: transaction parameters
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).transact(tx_params.as_dict())

    def build_transaction(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).estimateGas(tx_params.as_dict())


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


class UnstakeMethod(ContractMethod):
    """Various interfaces to the unstake method."""

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

    def validate_and_normalize_inputs(self, amount: int):
        """Validate the inputs to the unstake method."""
        self.validator.assert_valid(
            method_name="unstake",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return amount

    def call(self, amount: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        Unstake. Tokens are withdrawn from the ZRX Vault and returned to the
        staker. Stake must be in the 'undelegated' status in both the current
        and next epoch in order to be unstaked.

        :param amount: of ZRX to unstake.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(amount).call(tx_params.as_dict())

    def send_transaction(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Unstake. Tokens are withdrawn from the ZRX Vault and returned to the
        staker. Stake must be in the 'undelegated' status in both the current
        and next epoch in order to be unstaked.

        :param amount: of ZRX to unstake.
        :param tx_params: transaction parameters
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).transact(tx_params.as_dict())

    def build_transaction(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).estimateGas(tx_params.as_dict())


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


class WithdrawDelegatorRewardsMethod(ContractMethod):
    """Various interfaces to the withdrawDelegatorRewards method."""

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

    def validate_and_normalize_inputs(self, pool_id: Union[bytes, str]):
        """Validate the inputs to the withdrawDelegatorRewards method."""
        self.validator.assert_valid(
            method_name="withdrawDelegatorRewards",
            parameter_name="poolId",
            argument_value=pool_id,
        )
        return pool_id

    def call(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Withdraws the caller's WETH rewards that have accumulated until the
        last epoch.

        :param poolId: Unique id of pool.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(pool_id).call(tx_params.as_dict())

    def send_transaction(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Withdraws the caller's WETH rewards that have accumulated until the
        last epoch.

        :param poolId: Unique id of pool.
        :param tx_params: transaction parameters
        """
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).transact(tx_params.as_dict())

    def build_transaction(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, pool_id: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (pool_id) = self.validate_and_normalize_inputs(pool_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pool_id).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Staking:
    """Wrapper class for Staking Solidity contract."""

    add_authorized_address: AddAuthorizedAddressMethod
    """Constructor-initialized instance of
    :class:`AddAuthorizedAddressMethod`.
    """

    add_exchange_address: AddExchangeAddressMethod
    """Constructor-initialized instance of
    :class:`AddExchangeAddressMethod`.
    """

    aggregated_stats_by_epoch: AggregatedStatsByEpochMethod
    """Constructor-initialized instance of
    :class:`AggregatedStatsByEpochMethod`.
    """

    authorities: AuthoritiesMethod
    """Constructor-initialized instance of
    :class:`AuthoritiesMethod`.
    """

    authorized: AuthorizedMethod
    """Constructor-initialized instance of
    :class:`AuthorizedMethod`.
    """

    cobb_douglas_alpha_denominator: CobbDouglasAlphaDenominatorMethod
    """Constructor-initialized instance of
    :class:`CobbDouglasAlphaDenominatorMethod`.
    """

    cobb_douglas_alpha_numerator: CobbDouglasAlphaNumeratorMethod
    """Constructor-initialized instance of
    :class:`CobbDouglasAlphaNumeratorMethod`.
    """

    compute_reward_balance_of_delegator: ComputeRewardBalanceOfDelegatorMethod
    """Constructor-initialized instance of
    :class:`ComputeRewardBalanceOfDelegatorMethod`.
    """

    compute_reward_balance_of_operator: ComputeRewardBalanceOfOperatorMethod
    """Constructor-initialized instance of
    :class:`ComputeRewardBalanceOfOperatorMethod`.
    """

    create_staking_pool: CreateStakingPoolMethod
    """Constructor-initialized instance of
    :class:`CreateStakingPoolMethod`.
    """

    current_epoch: CurrentEpochMethod
    """Constructor-initialized instance of
    :class:`CurrentEpochMethod`.
    """

    current_epoch_start_time_in_seconds: CurrentEpochStartTimeInSecondsMethod
    """Constructor-initialized instance of
    :class:`CurrentEpochStartTimeInSecondsMethod`.
    """

    decrease_staking_pool_operator_share: DecreaseStakingPoolOperatorShareMethod
    """Constructor-initialized instance of
    :class:`DecreaseStakingPoolOperatorShareMethod`.
    """

    end_epoch: EndEpochMethod
    """Constructor-initialized instance of
    :class:`EndEpochMethod`.
    """

    epoch_duration_in_seconds: EpochDurationInSecondsMethod
    """Constructor-initialized instance of
    :class:`EpochDurationInSecondsMethod`.
    """

    finalize_pool: FinalizePoolMethod
    """Constructor-initialized instance of
    :class:`FinalizePoolMethod`.
    """

    get_authorized_addresses: GetAuthorizedAddressesMethod
    """Constructor-initialized instance of
    :class:`GetAuthorizedAddressesMethod`.
    """

    get_current_epoch_earliest_end_time_in_seconds: GetCurrentEpochEarliestEndTimeInSecondsMethod
    """Constructor-initialized instance of
    :class:`GetCurrentEpochEarliestEndTimeInSecondsMethod`.
    """

    get_global_stake_by_status: GetGlobalStakeByStatusMethod
    """Constructor-initialized instance of
    :class:`GetGlobalStakeByStatusMethod`.
    """

    get_owner_stake_by_status: GetOwnerStakeByStatusMethod
    """Constructor-initialized instance of
    :class:`GetOwnerStakeByStatusMethod`.
    """

    get_params: GetParamsMethod
    """Constructor-initialized instance of
    :class:`GetParamsMethod`.
    """

    get_stake_delegated_to_pool_by_owner: GetStakeDelegatedToPoolByOwnerMethod
    """Constructor-initialized instance of
    :class:`GetStakeDelegatedToPoolByOwnerMethod`.
    """

    get_staking_pool: GetStakingPoolMethod
    """Constructor-initialized instance of
    :class:`GetStakingPoolMethod`.
    """

    get_staking_pool_stats_this_epoch: GetStakingPoolStatsThisEpochMethod
    """Constructor-initialized instance of
    :class:`GetStakingPoolStatsThisEpochMethod`.
    """

    get_total_stake: GetTotalStakeMethod
    """Constructor-initialized instance of
    :class:`GetTotalStakeMethod`.
    """

    get_total_stake_delegated_to_pool: GetTotalStakeDelegatedToPoolMethod
    """Constructor-initialized instance of
    :class:`GetTotalStakeDelegatedToPoolMethod`.
    """

    get_weth_contract: GetWethContractMethod
    """Constructor-initialized instance of
    :class:`GetWethContractMethod`.
    """

    get_zrx_vault: GetZrxVaultMethod
    """Constructor-initialized instance of
    :class:`GetZrxVaultMethod`.
    """

    init: InitMethod
    """Constructor-initialized instance of
    :class:`InitMethod`.
    """

    join_staking_pool_as_maker: JoinStakingPoolAsMakerMethod
    """Constructor-initialized instance of
    :class:`JoinStakingPoolAsMakerMethod`.
    """

    last_pool_id: LastPoolIdMethod
    """Constructor-initialized instance of
    :class:`LastPoolIdMethod`.
    """

    minimum_pool_stake: MinimumPoolStakeMethod
    """Constructor-initialized instance of
    :class:`MinimumPoolStakeMethod`.
    """

    move_stake: MoveStakeMethod
    """Constructor-initialized instance of
    :class:`MoveStakeMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    pay_protocol_fee: PayProtocolFeeMethod
    """Constructor-initialized instance of
    :class:`PayProtocolFeeMethod`.
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

    remove_exchange_address: RemoveExchangeAddressMethod
    """Constructor-initialized instance of
    :class:`RemoveExchangeAddressMethod`.
    """

    reward_delegated_stake_weight: RewardDelegatedStakeWeightMethod
    """Constructor-initialized instance of
    :class:`RewardDelegatedStakeWeightMethod`.
    """

    rewards_by_pool_id: RewardsByPoolIdMethod
    """Constructor-initialized instance of
    :class:`RewardsByPoolIdMethod`.
    """

    set_params: SetParamsMethod
    """Constructor-initialized instance of
    :class:`SetParamsMethod`.
    """

    stake: StakeMethod
    """Constructor-initialized instance of
    :class:`StakeMethod`.
    """

    staking_contract: StakingContractMethod
    """Constructor-initialized instance of
    :class:`StakingContractMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    unstake: UnstakeMethod
    """Constructor-initialized instance of
    :class:`UnstakeMethod`.
    """

    valid_exchanges: ValidExchangesMethod
    """Constructor-initialized instance of
    :class:`ValidExchangesMethod`.
    """

    weth_reserved_for_pool_rewards: WethReservedForPoolRewardsMethod
    """Constructor-initialized instance of
    :class:`WethReservedForPoolRewardsMethod`.
    """

    withdraw_delegator_rewards: WithdrawDelegatorRewardsMethod
    """Constructor-initialized instance of
    :class:`WithdrawDelegatorRewardsMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: StakingValidator = None,
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
            validator = StakingValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=Staking.abi()
        ).functions

        self.add_authorized_address = AddAuthorizedAddressMethod(
            web3_or_provider,
            contract_address,
            functions.addAuthorizedAddress,
            validator,
        )

        self.add_exchange_address = AddExchangeAddressMethod(
            web3_or_provider,
            contract_address,
            functions.addExchangeAddress,
            validator,
        )

        self.aggregated_stats_by_epoch = AggregatedStatsByEpochMethod(
            web3_or_provider,
            contract_address,
            functions.aggregatedStatsByEpoch,
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

        self.compute_reward_balance_of_delegator = ComputeRewardBalanceOfDelegatorMethod(
            web3_or_provider,
            contract_address,
            functions.computeRewardBalanceOfDelegator,
            validator,
        )

        self.compute_reward_balance_of_operator = ComputeRewardBalanceOfOperatorMethod(
            web3_or_provider,
            contract_address,
            functions.computeRewardBalanceOfOperator,
            validator,
        )

        self.create_staking_pool = CreateStakingPoolMethod(
            web3_or_provider,
            contract_address,
            functions.createStakingPool,
            validator,
        )

        self.current_epoch = CurrentEpochMethod(
            web3_or_provider, contract_address, functions.currentEpoch
        )

        self.current_epoch_start_time_in_seconds = CurrentEpochStartTimeInSecondsMethod(
            web3_or_provider,
            contract_address,
            functions.currentEpochStartTimeInSeconds,
        )

        self.decrease_staking_pool_operator_share = DecreaseStakingPoolOperatorShareMethod(
            web3_or_provider,
            contract_address,
            functions.decreaseStakingPoolOperatorShare,
            validator,
        )

        self.end_epoch = EndEpochMethod(
            web3_or_provider, contract_address, functions.endEpoch
        )

        self.epoch_duration_in_seconds = EpochDurationInSecondsMethod(
            web3_or_provider,
            contract_address,
            functions.epochDurationInSeconds,
        )

        self.finalize_pool = FinalizePoolMethod(
            web3_or_provider,
            contract_address,
            functions.finalizePool,
            validator,
        )

        self.get_authorized_addresses = GetAuthorizedAddressesMethod(
            web3_or_provider,
            contract_address,
            functions.getAuthorizedAddresses,
        )

        self.get_current_epoch_earliest_end_time_in_seconds = GetCurrentEpochEarliestEndTimeInSecondsMethod(
            web3_or_provider,
            contract_address,
            functions.getCurrentEpochEarliestEndTimeInSeconds,
        )

        self.get_global_stake_by_status = GetGlobalStakeByStatusMethod(
            web3_or_provider,
            contract_address,
            functions.getGlobalStakeByStatus,
            validator,
        )

        self.get_owner_stake_by_status = GetOwnerStakeByStatusMethod(
            web3_or_provider,
            contract_address,
            functions.getOwnerStakeByStatus,
            validator,
        )

        self.get_params = GetParamsMethod(
            web3_or_provider, contract_address, functions.getParams
        )

        self.get_stake_delegated_to_pool_by_owner = GetStakeDelegatedToPoolByOwnerMethod(
            web3_or_provider,
            contract_address,
            functions.getStakeDelegatedToPoolByOwner,
            validator,
        )

        self.get_staking_pool = GetStakingPoolMethod(
            web3_or_provider,
            contract_address,
            functions.getStakingPool,
            validator,
        )

        self.get_staking_pool_stats_this_epoch = GetStakingPoolStatsThisEpochMethod(
            web3_or_provider,
            contract_address,
            functions.getStakingPoolStatsThisEpoch,
            validator,
        )

        self.get_total_stake = GetTotalStakeMethod(
            web3_or_provider,
            contract_address,
            functions.getTotalStake,
            validator,
        )

        self.get_total_stake_delegated_to_pool = GetTotalStakeDelegatedToPoolMethod(
            web3_or_provider,
            contract_address,
            functions.getTotalStakeDelegatedToPool,
            validator,
        )

        self.get_weth_contract = GetWethContractMethod(
            web3_or_provider, contract_address, functions.getWethContract
        )

        self.get_zrx_vault = GetZrxVaultMethod(
            web3_or_provider, contract_address, functions.getZrxVault
        )

        self.init = InitMethod(
            web3_or_provider, contract_address, functions.init
        )

        self.join_staking_pool_as_maker = JoinStakingPoolAsMakerMethod(
            web3_or_provider,
            contract_address,
            functions.joinStakingPoolAsMaker,
            validator,
        )

        self.last_pool_id = LastPoolIdMethod(
            web3_or_provider, contract_address, functions.lastPoolId
        )

        self.minimum_pool_stake = MinimumPoolStakeMethod(
            web3_or_provider, contract_address, functions.minimumPoolStake
        )

        self.move_stake = MoveStakeMethod(
            web3_or_provider, contract_address, functions.moveStake, validator
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
        )

        self.pay_protocol_fee = PayProtocolFeeMethod(
            web3_or_provider,
            contract_address,
            functions.payProtocolFee,
            validator,
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

        self.remove_exchange_address = RemoveExchangeAddressMethod(
            web3_or_provider,
            contract_address,
            functions.removeExchangeAddress,
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

        self.set_params = SetParamsMethod(
            web3_or_provider, contract_address, functions.setParams, validator
        )

        self.stake = StakeMethod(
            web3_or_provider, contract_address, functions.stake, validator
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

        self.unstake = UnstakeMethod(
            web3_or_provider, contract_address, functions.unstake, validator
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

        self.withdraw_delegator_rewards = WithdrawDelegatorRewardsMethod(
            web3_or_provider,
            contract_address,
            functions.withdrawDelegatorRewards,
            validator,
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
                abi=Staking.abi(),
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
                abi=Staking.abi(),
            )
            .events.AuthorizedAddressRemoved()
            .processReceipt(tx_receipt)
        )

    def get_epoch_ended_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for EpochEnded event.

        :param tx_hash: hash of transaction emitting EpochEnded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.EpochEnded()
            .processReceipt(tx_receipt)
        )

    def get_epoch_finalized_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for EpochFinalized event.

        :param tx_hash: hash of transaction emitting EpochFinalized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.EpochFinalized()
            .processReceipt(tx_receipt)
        )

    def get_exchange_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ExchangeAdded event.

        :param tx_hash: hash of transaction emitting ExchangeAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.ExchangeAdded()
            .processReceipt(tx_receipt)
        )

    def get_exchange_removed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ExchangeRemoved event.

        :param tx_hash: hash of transaction emitting ExchangeRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.ExchangeRemoved()
            .processReceipt(tx_receipt)
        )

    def get_maker_staking_pool_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MakerStakingPoolSet event.

        :param tx_hash: hash of transaction emitting MakerStakingPoolSet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.MakerStakingPoolSet()
            .processReceipt(tx_receipt)
        )

    def get_move_stake_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MoveStake event.

        :param tx_hash: hash of transaction emitting MoveStake event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.MoveStake()
            .processReceipt(tx_receipt)
        )

    def get_operator_share_decreased_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OperatorShareDecreased event.

        :param tx_hash: hash of transaction emitting OperatorShareDecreased
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.OperatorShareDecreased()
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
                abi=Staking.abi(),
            )
            .events.OwnershipTransferred()
            .processReceipt(tx_receipt)
        )

    def get_params_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ParamsSet event.

        :param tx_hash: hash of transaction emitting ParamsSet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.ParamsSet()
            .processReceipt(tx_receipt)
        )

    def get_rewards_paid_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RewardsPaid event.

        :param tx_hash: hash of transaction emitting RewardsPaid event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.RewardsPaid()
            .processReceipt(tx_receipt)
        )

    def get_stake_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Stake event.

        :param tx_hash: hash of transaction emitting Stake event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.Stake()
            .processReceipt(tx_receipt)
        )

    def get_staking_pool_created_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for StakingPoolCreated event.

        :param tx_hash: hash of transaction emitting StakingPoolCreated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.StakingPoolCreated()
            .processReceipt(tx_receipt)
        )

    def get_staking_pool_earned_rewards_in_epoch_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for StakingPoolEarnedRewardsInEpoch event.

        :param tx_hash: hash of transaction emitting
            StakingPoolEarnedRewardsInEpoch event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.StakingPoolEarnedRewardsInEpoch()
            .processReceipt(tx_receipt)
        )

    def get_unstake_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Unstake event.

        :param tx_hash: hash of transaction emitting Unstake event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Staking.abi(),
            )
            .events.Unstake()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"wethAddress","type":"address"},{"internalType":"address","name":"zrxVaultAddress","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AuthorizedAddressAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AuthorizedAddressRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"epoch","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"numPoolsToFinalize","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rewardsAvailable","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalFeesCollected","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalWeightedStake","type":"uint256"}],"name":"EpochEnded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"epoch","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rewardsPaid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rewardsRemaining","type":"uint256"}],"name":"EpochFinalized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"exchangeAddress","type":"address"}],"name":"ExchangeAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"exchangeAddress","type":"address"}],"name":"ExchangeRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"makerAddress","type":"address"},{"indexed":true,"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"MakerStakingPoolSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"fromStatus","type":"uint8"},{"indexed":true,"internalType":"bytes32","name":"fromPool","type":"bytes32"},{"indexed":false,"internalType":"uint8","name":"toStatus","type":"uint8"},{"indexed":true,"internalType":"bytes32","name":"toPool","type":"bytes32"}],"name":"MoveStake","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"poolId","type":"bytes32"},{"indexed":false,"internalType":"uint32","name":"oldOperatorShare","type":"uint32"},{"indexed":false,"internalType":"uint32","name":"newOperatorShare","type":"uint32"}],"name":"OperatorShareDecreased","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"epochDurationInSeconds","type":"uint256"},{"indexed":false,"internalType":"uint32","name":"rewardDelegatedStakeWeight","type":"uint32"},{"indexed":false,"internalType":"uint256","name":"minimumPoolStake","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"cobbDouglasAlphaNumerator","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"cobbDouglasAlphaDenominator","type":"uint256"}],"name":"ParamsSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"epoch","type":"uint256"},{"indexed":true,"internalType":"bytes32","name":"poolId","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"operatorReward","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"membersReward","type":"uint256"}],"name":"RewardsPaid","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Stake","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"poolId","type":"bytes32"},{"indexed":false,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"uint32","name":"operatorShare","type":"uint32"}],"name":"StakingPoolCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"epoch","type":"uint256"},{"indexed":true,"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"StakingPoolEarnedRewardsInEpoch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Unstake","type":"event"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"addAuthorizedAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"addExchangeAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"aggregatedStatsByEpoch","outputs":[{"internalType":"uint256","name":"rewardsAvailable","type":"uint256"},{"internalType":"uint256","name":"numPoolsToFinalize","type":"uint256"},{"internalType":"uint256","name":"totalFeesCollected","type":"uint256"},{"internalType":"uint256","name":"totalWeightedStake","type":"uint256"},{"internalType":"uint256","name":"totalRewardsFinalized","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"authorities","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"authorized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"cobbDouglasAlphaDenominator","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"cobbDouglasAlphaNumerator","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"},{"internalType":"address","name":"member","type":"address"}],"name":"computeRewardBalanceOfDelegator","outputs":[{"internalType":"uint256","name":"reward","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"computeRewardBalanceOfOperator","outputs":[{"internalType":"uint256","name":"reward","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint32","name":"operatorShare","type":"uint32"},{"internalType":"bool","name":"addOperatorAsMaker","type":"bool"}],"name":"createStakingPool","outputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"currentEpoch","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"currentEpochStartTimeInSeconds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"},{"internalType":"uint32","name":"newOperatorShare","type":"uint32"}],"name":"decreaseStakingPoolOperatorShare","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"endEpoch","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"epochDurationInSeconds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"finalizePool","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getAuthorizedAddresses","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getCurrentEpochEarliestEndTimeInSeconds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"enum IStructs.StakeStatus","name":"stakeStatus","type":"uint8"}],"name":"getGlobalStakeByStatus","outputs":[{"components":[{"internalType":"uint64","name":"currentEpoch","type":"uint64"},{"internalType":"uint96","name":"currentEpochBalance","type":"uint96"},{"internalType":"uint96","name":"nextEpochBalance","type":"uint96"}],"internalType":"struct IStructs.StoredBalance","name":"balance","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"staker","type":"address"},{"internalType":"enum IStructs.StakeStatus","name":"stakeStatus","type":"uint8"}],"name":"getOwnerStakeByStatus","outputs":[{"components":[{"internalType":"uint64","name":"currentEpoch","type":"uint64"},{"internalType":"uint96","name":"currentEpochBalance","type":"uint96"},{"internalType":"uint96","name":"nextEpochBalance","type":"uint96"}],"internalType":"struct IStructs.StoredBalance","name":"balance","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getParams","outputs":[{"internalType":"uint256","name":"_epochDurationInSeconds","type":"uint256"},{"internalType":"uint32","name":"_rewardDelegatedStakeWeight","type":"uint32"},{"internalType":"uint256","name":"_minimumPoolStake","type":"uint256"},{"internalType":"uint32","name":"_cobbDouglasAlphaNumerator","type":"uint32"},{"internalType":"uint32","name":"_cobbDouglasAlphaDenominator","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"staker","type":"address"},{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"getStakeDelegatedToPoolByOwner","outputs":[{"components":[{"internalType":"uint64","name":"currentEpoch","type":"uint64"},{"internalType":"uint96","name":"currentEpochBalance","type":"uint96"},{"internalType":"uint96","name":"nextEpochBalance","type":"uint96"}],"internalType":"struct IStructs.StoredBalance","name":"balance","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"getStakingPool","outputs":[{"components":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"uint32","name":"operatorShare","type":"uint32"}],"internalType":"struct IStructs.Pool","name":"","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"getStakingPoolStatsThisEpoch","outputs":[{"components":[{"internalType":"uint256","name":"feesCollected","type":"uint256"},{"internalType":"uint256","name":"weightedStake","type":"uint256"},{"internalType":"uint256","name":"membersStake","type":"uint256"}],"internalType":"struct IStructs.PoolStats","name":"","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"staker","type":"address"}],"name":"getTotalStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"getTotalStakeDelegatedToPool","outputs":[{"components":[{"internalType":"uint64","name":"currentEpoch","type":"uint64"},{"internalType":"uint96","name":"currentEpochBalance","type":"uint96"},{"internalType":"uint96","name":"nextEpochBalance","type":"uint96"}],"internalType":"struct IStructs.StoredBalance","name":"balance","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getWethContract","outputs":[{"internalType":"contract IEtherToken","name":"wethContract","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getZrxVault","outputs":[{"internalType":"contract IZrxVault","name":"zrxVault","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"init","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"joinStakingPoolAsMaker","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"lastPoolId","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"minimumPoolStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"components":[{"internalType":"enum IStructs.StakeStatus","name":"status","type":"uint8"},{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"internalType":"struct IStructs.StakeInfo","name":"from","type":"tuple"},{"components":[{"internalType":"enum IStructs.StakeStatus","name":"status","type":"uint8"},{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"internalType":"struct IStructs.StakeInfo","name":"to","type":"tuple"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"moveStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"makerAddress","type":"address"},{"internalType":"address","name":"payerAddress","type":"address"},{"internalType":"uint256","name":"protocolFee","type":"uint256"}],"name":"payProtocolFee","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"poolIdByMaker","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"},{"internalType":"uint256","name":"index_1","type":"uint256"}],"name":"poolStatsByEpoch","outputs":[{"internalType":"uint256","name":"feesCollected","type":"uint256"},{"internalType":"uint256","name":"weightedStake","type":"uint256"},{"internalType":"uint256","name":"membersStake","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"removeAuthorizedAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"removeAuthorizedAddressAtIndex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"removeExchangeAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"rewardDelegatedStakeWeight","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"rewardsByPoolId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_epochDurationInSeconds","type":"uint256"},{"internalType":"uint32","name":"_rewardDelegatedStakeWeight","type":"uint32"},{"internalType":"uint256","name":"_minimumPoolStake","type":"uint256"},{"internalType":"uint32","name":"_cobbDouglasAlphaNumerator","type":"uint32"},{"internalType":"uint32","name":"_cobbDouglasAlphaDenominator","type":"uint32"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"stake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"stakingContract","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"unstake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"validExchanges","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"wethReservedForPoolRewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"poolId","type":"bytes32"}],"name":"withdrawDelegatorRewards","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
