"""Generated wrapper for ZrxVault Solidity contract."""

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
# constructor for ZrxVault below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ZrxVaultValidator,
    )
except ImportError:

    class ZrxVaultValidator(  # type: ignore
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

    def validate_and_normalize_inputs(self, staker: str):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name="balanceOf",
            parameter_name="staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        return staker

    def call(self, staker: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        Returns the balance in Zrx Tokens of the `staker`

        :param tx_params: transaction parameters
        :returns: Balance in Zrx.
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


class BalanceOfZrxVaultMethod(ContractMethod):
    """Various interfaces to the balanceOfZrxVault method."""

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

        Returns the entire balance of Zrx tokens in the vault.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class DepositFromMethod(ContractMethod):
    """Various interfaces to the depositFrom method."""

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

    def validate_and_normalize_inputs(self, staker: str, amount: int):
        """Validate the inputs to the depositFrom method."""
        self.validator.assert_valid(
            method_name="depositFrom",
            parameter_name="staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        self.validator.assert_valid(
            method_name="depositFrom",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (staker, amount)

    def call(
        self, staker: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Deposit an `amount` of Zrx Tokens from `staker` into the vault. Note
        that only the Staking contract can call this. Note that this can only
        be called when *not* in Catastrophic Failure mode.

        :param amount: of Zrx Tokens to deposit.
        :param staker: of Zrx Tokens.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (staker, amount) = self.validate_and_normalize_inputs(staker, amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(staker, amount).call(tx_params.as_dict())

    def send_transaction(
        self, staker: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Deposit an `amount` of Zrx Tokens from `staker` into the vault. Note
        that only the Staking contract can call this. Note that this can only
        be called when *not* in Catastrophic Failure mode.

        :param amount: of Zrx Tokens to deposit.
        :param staker: of Zrx Tokens.
        :param tx_params: transaction parameters
        """
        (staker, amount) = self.validate_and_normalize_inputs(staker, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, staker: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (staker, amount) = self.validate_and_normalize_inputs(staker, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, staker: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (staker, amount) = self.validate_and_normalize_inputs(staker, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker, amount).estimateGas(
            tx_params.as_dict()
        )


class EnterCatastrophicFailureMethod(ContractMethod):
    """Various interfaces to the enterCatastrophicFailure method."""

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

        Vault enters into Catastrophic Failure Mode. *** WARNING - ONCE IN
        CATOSTROPHIC FAILURE MODE, YOU CAN NEVER GO BACK! *** Note that only
        the contract owner can call this function.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Vault enters into Catastrophic Failure Mode. *** WARNING - ONCE IN
        CATOSTROPHIC FAILURE MODE, YOU CAN NEVER GO BACK! *** Note that only
        the contract owner can call this function.

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


class IsInCatastrophicFailureMethod(ContractMethod):
    """Various interfaces to the isInCatastrophicFailure method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return bool(returned)

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


class SetStakingProxyMethod(ContractMethod):
    """Various interfaces to the setStakingProxy method."""

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

    def validate_and_normalize_inputs(self, _staking_proxy_address: str):
        """Validate the inputs to the setStakingProxy method."""
        self.validator.assert_valid(
            method_name="setStakingProxy",
            parameter_name="_stakingProxyAddress",
            argument_value=_staking_proxy_address,
        )
        _staking_proxy_address = self.validate_and_checksum_address(
            _staking_proxy_address
        )
        return _staking_proxy_address

    def call(
        self, _staking_proxy_address: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Sets the address of the StakingProxy contract. Note that only the
        contract owner can call this function.

        :param _stakingProxyAddress: Address of Staking proxy contract.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_staking_proxy_address) = self.validate_and_normalize_inputs(
            _staking_proxy_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_staking_proxy_address).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self, _staking_proxy_address: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Sets the address of the StakingProxy contract. Note that only the
        contract owner can call this function.

        :param _stakingProxyAddress: Address of Staking proxy contract.
        :param tx_params: transaction parameters
        """
        (_staking_proxy_address) = self.validate_and_normalize_inputs(
            _staking_proxy_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_staking_proxy_address).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _staking_proxy_address: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_staking_proxy_address) = self.validate_and_normalize_inputs(
            _staking_proxy_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _staking_proxy_address
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self, _staking_proxy_address: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_staking_proxy_address) = self.validate_and_normalize_inputs(
            _staking_proxy_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_staking_proxy_address).estimateGas(
            tx_params.as_dict()
        )


class SetZrxProxyMethod(ContractMethod):
    """Various interfaces to the setZrxProxy method."""

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

    def validate_and_normalize_inputs(self, _zrx_proxy_address: str):
        """Validate the inputs to the setZrxProxy method."""
        self.validator.assert_valid(
            method_name="setZrxProxy",
            parameter_name="_zrxProxyAddress",
            argument_value=_zrx_proxy_address,
        )
        _zrx_proxy_address = self.validate_and_checksum_address(
            _zrx_proxy_address
        )
        return _zrx_proxy_address

    def call(
        self, _zrx_proxy_address: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Sets the Zrx proxy. Note that only an authorized address can call this
        function. Note that this can only be called when *not* in Catastrophic
        Failure mode.

        :param _zrxProxyAddress: Address of the 0x Zrx Proxy.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_zrx_proxy_address) = self.validate_and_normalize_inputs(
            _zrx_proxy_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_zrx_proxy_address).call(tx_params.as_dict())

    def send_transaction(
        self, _zrx_proxy_address: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Sets the Zrx proxy. Note that only an authorized address can call this
        function. Note that this can only be called when *not* in Catastrophic
        Failure mode.

        :param _zrxProxyAddress: Address of the 0x Zrx Proxy.
        :param tx_params: transaction parameters
        """
        (_zrx_proxy_address) = self.validate_and_normalize_inputs(
            _zrx_proxy_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_zrx_proxy_address).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, _zrx_proxy_address: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_zrx_proxy_address) = self.validate_and_normalize_inputs(
            _zrx_proxy_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_zrx_proxy_address).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _zrx_proxy_address: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_zrx_proxy_address) = self.validate_and_normalize_inputs(
            _zrx_proxy_address
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_zrx_proxy_address).estimateGas(
            tx_params.as_dict()
        )


class StakingProxyAddressMethod(ContractMethod):
    """Various interfaces to the stakingProxyAddress method."""

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


class WithdrawAllFromMethod(ContractMethod):
    """Various interfaces to the withdrawAllFrom method."""

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
        """Validate the inputs to the withdrawAllFrom method."""
        self.validator.assert_valid(
            method_name="withdrawAllFrom",
            parameter_name="staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        return staker

    def call(self, staker: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        Withdraw ALL Zrx Tokens to `staker` from the vault. Note that this can
        only be called when *in* Catastrophic Failure mode.

        :param staker: of Zrx Tokens.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(staker).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, staker: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Withdraw ALL Zrx Tokens to `staker` from the vault. Note that this can
        only be called when *in* Catastrophic Failure mode.

        :param staker: of Zrx Tokens.
        :param tx_params: transaction parameters
        """
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker).transact(tx_params.as_dict())

    def build_transaction(
        self, staker: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, staker: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker).estimateGas(tx_params.as_dict())


class WithdrawFromMethod(ContractMethod):
    """Various interfaces to the withdrawFrom method."""

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

    def validate_and_normalize_inputs(self, staker: str, amount: int):
        """Validate the inputs to the withdrawFrom method."""
        self.validator.assert_valid(
            method_name="withdrawFrom",
            parameter_name="staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        self.validator.assert_valid(
            method_name="withdrawFrom",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (staker, amount)

    def call(
        self, staker: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        Withdraw an `amount` of Zrx Tokens to `staker` from the vault. Note
        that only the Staking contract can call this. Note that this can only
        be called when *not* in Catastrophic Failure mode.

        :param amount: of Zrx Tokens to withdraw.
        :param staker: of Zrx Tokens.
        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (staker, amount) = self.validate_and_normalize_inputs(staker, amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(staker, amount).call(tx_params.as_dict())

    def send_transaction(
        self, staker: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        Withdraw an `amount` of Zrx Tokens to `staker` from the vault. Note
        that only the Staking contract can call this. Note that this can only
        be called when *not* in Catastrophic Failure mode.

        :param amount: of Zrx Tokens to withdraw.
        :param staker: of Zrx Tokens.
        :param tx_params: transaction parameters
        """
        (staker, amount) = self.validate_and_normalize_inputs(staker, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, staker: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (staker, amount) = self.validate_and_normalize_inputs(staker, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, staker: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (staker, amount) = self.validate_and_normalize_inputs(staker, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker, amount).estimateGas(
            tx_params.as_dict()
        )


class ZrxAssetProxyMethod(ContractMethod):
    """Various interfaces to the zrxAssetProxy method."""

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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ZrxVault:
    """Wrapper class for ZrxVault Solidity contract."""

    add_authorized_address: AddAuthorizedAddressMethod
    """Constructor-initialized instance of
    :class:`AddAuthorizedAddressMethod`.
    """

    authorities: AuthoritiesMethod
    """Constructor-initialized instance of
    :class:`AuthoritiesMethod`.
    """

    authorized: AuthorizedMethod
    """Constructor-initialized instance of
    :class:`AuthorizedMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    balance_of_zrx_vault: BalanceOfZrxVaultMethod
    """Constructor-initialized instance of
    :class:`BalanceOfZrxVaultMethod`.
    """

    deposit_from: DepositFromMethod
    """Constructor-initialized instance of
    :class:`DepositFromMethod`.
    """

    enter_catastrophic_failure: EnterCatastrophicFailureMethod
    """Constructor-initialized instance of
    :class:`EnterCatastrophicFailureMethod`.
    """

    get_authorized_addresses: GetAuthorizedAddressesMethod
    """Constructor-initialized instance of
    :class:`GetAuthorizedAddressesMethod`.
    """

    is_in_catastrophic_failure: IsInCatastrophicFailureMethod
    """Constructor-initialized instance of
    :class:`IsInCatastrophicFailureMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    remove_authorized_address: RemoveAuthorizedAddressMethod
    """Constructor-initialized instance of
    :class:`RemoveAuthorizedAddressMethod`.
    """

    remove_authorized_address_at_index: RemoveAuthorizedAddressAtIndexMethod
    """Constructor-initialized instance of
    :class:`RemoveAuthorizedAddressAtIndexMethod`.
    """

    set_staking_proxy: SetStakingProxyMethod
    """Constructor-initialized instance of
    :class:`SetStakingProxyMethod`.
    """

    set_zrx_proxy: SetZrxProxyMethod
    """Constructor-initialized instance of
    :class:`SetZrxProxyMethod`.
    """

    staking_proxy_address: StakingProxyAddressMethod
    """Constructor-initialized instance of
    :class:`StakingProxyAddressMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    withdraw_all_from: WithdrawAllFromMethod
    """Constructor-initialized instance of
    :class:`WithdrawAllFromMethod`.
    """

    withdraw_from: WithdrawFromMethod
    """Constructor-initialized instance of
    :class:`WithdrawFromMethod`.
    """

    zrx_asset_proxy: ZrxAssetProxyMethod
    """Constructor-initialized instance of
    :class:`ZrxAssetProxyMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ZrxVaultValidator = None,
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
            validator = ZrxVaultValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=ZrxVault.abi()
        ).functions

        self.add_authorized_address = AddAuthorizedAddressMethod(
            web3_or_provider,
            contract_address,
            functions.addAuthorizedAddress,
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

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.balance_of_zrx_vault = BalanceOfZrxVaultMethod(
            web3_or_provider, contract_address, functions.balanceOfZrxVault
        )

        self.deposit_from = DepositFromMethod(
            web3_or_provider,
            contract_address,
            functions.depositFrom,
            validator,
        )

        self.enter_catastrophic_failure = EnterCatastrophicFailureMethod(
            web3_or_provider,
            contract_address,
            functions.enterCatastrophicFailure,
        )

        self.get_authorized_addresses = GetAuthorizedAddressesMethod(
            web3_or_provider,
            contract_address,
            functions.getAuthorizedAddresses,
        )

        self.is_in_catastrophic_failure = IsInCatastrophicFailureMethod(
            web3_or_provider,
            contract_address,
            functions.isInCatastrophicFailure,
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
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

        self.set_staking_proxy = SetStakingProxyMethod(
            web3_or_provider,
            contract_address,
            functions.setStakingProxy,
            validator,
        )

        self.set_zrx_proxy = SetZrxProxyMethod(
            web3_or_provider,
            contract_address,
            functions.setZrxProxy,
            validator,
        )

        self.staking_proxy_address = StakingProxyAddressMethod(
            web3_or_provider, contract_address, functions.stakingProxyAddress
        )

        self.transfer_ownership = TransferOwnershipMethod(
            web3_or_provider,
            contract_address,
            functions.transferOwnership,
            validator,
        )

        self.withdraw_all_from = WithdrawAllFromMethod(
            web3_or_provider,
            contract_address,
            functions.withdrawAllFrom,
            validator,
        )

        self.withdraw_from = WithdrawFromMethod(
            web3_or_provider,
            contract_address,
            functions.withdrawFrom,
            validator,
        )

        self.zrx_asset_proxy = ZrxAssetProxyMethod(
            web3_or_provider, contract_address, functions.zrxAssetProxy
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
                abi=ZrxVault.abi(),
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
                abi=ZrxVault.abi(),
            )
            .events.AuthorizedAddressRemoved()
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
                abi=ZrxVault.abi(),
            )
            .events.Deposit()
            .processReceipt(tx_receipt)
        )

    def get_in_catastrophic_failure_mode_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for InCatastrophicFailureMode event.

        :param tx_hash: hash of transaction emitting InCatastrophicFailureMode
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ZrxVault.abi(),
            )
            .events.InCatastrophicFailureMode()
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
                abi=ZrxVault.abi(),
            )
            .events.OwnershipTransferred()
            .processReceipt(tx_receipt)
        )

    def get_staking_proxy_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for StakingProxySet event.

        :param tx_hash: hash of transaction emitting StakingProxySet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ZrxVault.abi(),
            )
            .events.StakingProxySet()
            .processReceipt(tx_receipt)
        )

    def get_withdraw_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Withdraw event.

        :param tx_hash: hash of transaction emitting Withdraw event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ZrxVault.abi(),
            )
            .events.Withdraw()
            .processReceipt(tx_receipt)
        )

    def get_zrx_proxy_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ZrxProxySet event.

        :param tx_hash: hash of transaction emitting ZrxProxySet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ZrxVault.abi(),
            )
            .events.ZrxProxySet()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_zrxProxyAddress","type":"address"},{"internalType":"address","name":"_zrxTokenAddress","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AuthorizedAddressAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AuthorizedAddressRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sender","type":"address"}],"name":"InCatastrophicFailureMode","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"stakingProxyAddress","type":"address"}],"name":"StakingProxySet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"zrxProxyAddress","type":"address"}],"name":"ZrxProxySet","type":"event"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"addAuthorizedAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"authorities","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"authorized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"staker","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"balanceOfZrxVault","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"staker","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"depositFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"enterCatastrophicFailure","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getAuthorizedAddresses","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isInCatastrophicFailure","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"removeAuthorizedAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"removeAuthorizedAddressAtIndex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_stakingProxyAddress","type":"address"}],"name":"setStakingProxy","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_zrxProxyAddress","type":"address"}],"name":"setZrxProxy","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"stakingProxyAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"staker","type":"address"}],"name":"withdrawAllFrom","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"staker","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdrawFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"zrxAssetProxy","outputs":[{"internalType":"contract IAssetProxy","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
