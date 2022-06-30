"""Generated wrapper for WETH9 Solidity contract."""

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
# constructor for WETH9 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        WETH9Validator,
    )
except ImportError:

    class WETH9Validator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


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

    def validate_and_normalize_inputs(self, guy: str, wad: int):
        """Validate the inputs to the approve method."""
        self.validator.assert_valid(
            method_name="approve", parameter_name="guy", argument_value=guy,
        )
        guy = self.validate_and_checksum_address(guy)
        self.validator.assert_valid(
            method_name="approve", parameter_name="wad", argument_value=wad,
        )
        # safeguard against fractional inputs
        wad = int(wad)
        return (guy, wad)

    def call(
        self, guy: str, wad: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (guy, wad) = self.validate_and_normalize_inputs(guy, wad)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(guy, wad).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, guy: str, wad: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (guy, wad) = self.validate_and_normalize_inputs(guy, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(guy, wad).transact(tx_params.as_dict())

    def build_transaction(
        self, guy: str, wad: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (guy, wad) = self.validate_and_normalize_inputs(guy, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(guy, wad).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, guy: str, wad: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (guy, wad) = self.validate_and_normalize_inputs(guy, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(guy, wad).estimateGas(
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

        :param tx_params: transaction parameters

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

    def validate_and_normalize_inputs(self, src: str, dst: str, wad: int):
        """Validate the inputs to the transferFrom method."""
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="src",
            argument_value=src,
        )
        src = self.validate_and_checksum_address(src)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="dst",
            argument_value=dst,
        )
        dst = self.validate_and_checksum_address(dst)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="wad",
            argument_value=wad,
        )
        # safeguard against fractional inputs
        wad = int(wad)
        return (src, dst, wad)

    def call(
        self,
        src: str,
        dst: str,
        wad: int,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (src, dst, wad) = self.validate_and_normalize_inputs(src, dst, wad)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(src, dst, wad).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        src: str,
        dst: str,
        wad: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (src, dst, wad) = self.validate_and_normalize_inputs(src, dst, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(src, dst, wad).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        src: str,
        dst: str,
        wad: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (src, dst, wad) = self.validate_and_normalize_inputs(src, dst, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(src, dst, wad).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        src: str,
        dst: str,
        wad: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (src, dst, wad) = self.validate_and_normalize_inputs(src, dst, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(src, dst, wad).estimateGas(
            tx_params.as_dict()
        )


class WithdrawMethod(ContractMethod):
    """Various interfaces to the withdraw method."""

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

    def validate_and_normalize_inputs(self, wad: int):
        """Validate the inputs to the withdraw method."""
        self.validator.assert_valid(
            method_name="withdraw", parameter_name="wad", argument_value=wad,
        )
        # safeguard against fractional inputs
        wad = int(wad)
        return wad

    def call(self, wad: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (wad) = self.validate_and_normalize_inputs(wad)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(wad).call(tx_params.as_dict())

    def send_transaction(
        self, wad: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (wad) = self.validate_and_normalize_inputs(wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(wad).transact(tx_params.as_dict())

    def build_transaction(
        self, wad: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (wad) = self.validate_and_normalize_inputs(wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(wad).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, wad: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (wad) = self.validate_and_normalize_inputs(wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(wad).estimateGas(tx_params.as_dict())


class DecimalsMethod(ContractMethod):
    """Various interfaces to the decimals method."""

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

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name="balanceOf",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def estimate_gas(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
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

    def validate_and_normalize_inputs(self, dst: str, wad: int):
        """Validate the inputs to the transfer method."""
        self.validator.assert_valid(
            method_name="transfer", parameter_name="dst", argument_value=dst,
        )
        dst = self.validate_and_checksum_address(dst)
        self.validator.assert_valid(
            method_name="transfer", parameter_name="wad", argument_value=wad,
        )
        # safeguard against fractional inputs
        wad = int(wad)
        return (dst, wad)

    def call(
        self, dst: str, wad: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (dst, wad) = self.validate_and_normalize_inputs(dst, wad)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(dst, wad).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, dst: str, wad: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (dst, wad) = self.validate_and_normalize_inputs(dst, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(dst, wad).transact(tx_params.as_dict())

    def build_transaction(
        self, dst: str, wad: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (dst, wad) = self.validate_and_normalize_inputs(dst, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(dst, wad).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, dst: str, wad: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (dst, wad) = self.validate_and_normalize_inputs(dst, wad)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(dst, wad).estimateGas(
            tx_params.as_dict()
        )


class DepositMethod(ContractMethod):
    """Various interfaces to the deposit method."""

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

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

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

    def validate_and_normalize_inputs(self, index_0: str, index_1: str):
        """Validate the inputs to the allowance method."""
        self.validator.assert_valid(
            method_name="allowance",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="allowance",
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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class WETH9:
    """Wrapper class for WETH9 Solidity contract."""

    name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
    """

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

    withdraw: WithdrawMethod
    """Constructor-initialized instance of
    :class:`WithdrawMethod`.
    """

    decimals: DecimalsMethod
    """Constructor-initialized instance of
    :class:`DecimalsMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    symbol: SymbolMethod
    """Constructor-initialized instance of
    :class:`SymbolMethod`.
    """

    transfer: TransferMethod
    """Constructor-initialized instance of
    :class:`TransferMethod`.
    """

    deposit: DepositMethod
    """Constructor-initialized instance of
    :class:`DepositMethod`.
    """

    allowance: AllowanceMethod
    """Constructor-initialized instance of
    :class:`AllowanceMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: WETH9Validator = None,
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
            validator = WETH9Validator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=WETH9.abi()
        ).functions

        self.name = NameMethod(
            web3_or_provider, contract_address, functions.name
        )

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

        self.withdraw = WithdrawMethod(
            web3_or_provider, contract_address, functions.withdraw, validator
        )

        self.decimals = DecimalsMethod(
            web3_or_provider, contract_address, functions.decimals
        )

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.symbol = SymbolMethod(
            web3_or_provider, contract_address, functions.symbol
        )

        self.transfer = TransferMethod(
            web3_or_provider, contract_address, functions.transfer, validator
        )

        self.deposit = DepositMethod(
            web3_or_provider, contract_address, functions.deposit
        )

        self.allowance = AllowanceMethod(
            web3_or_provider, contract_address, functions.allowance, validator
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
                abi=WETH9.abi(),
            )
            .events.Approval()
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
                abi=WETH9.abi(),
            )
            .events.Transfer()
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
                abi=WETH9.abi(),
            )
            .events.Deposit()
            .processReceipt(tx_receipt)
        )

    def get_withdrawal_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Withdrawal event.

        :param tx_hash: hash of transaction emitting Withdrawal event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=WETH9.abi(),
            )
            .events.Withdrawal()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"index_0","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"index_0","type":"address"},{"name":"index_1","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Withdrawal","type":"event"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
