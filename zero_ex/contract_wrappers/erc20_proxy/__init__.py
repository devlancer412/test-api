"""Generated wrapper for ERC20Proxy Solidity contract."""

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
# constructor for ERC20Proxy below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ERC20ProxyValidator,
    )
except ImportError:

    class ERC20ProxyValidator(  # type: ignore
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


class GetProxyIdMethod(ContractMethod):
    """Various interfaces to the getProxyId method."""

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

        Gets the proxy id associated with the proxy address.

        :param tx_params: transaction parameters
        :returns: Proxy id.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


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
class ERC20Proxy:
    """Wrapper class for ERC20Proxy Solidity contract."""

    add_authorized_address: AddAuthorizedAddressMethod
    """Constructor-initialized instance of
    :class:`AddAuthorizedAddressMethod`.
    """

    authorities: AuthoritiesMethod
    """Constructor-initialized instance of
    :class:`AuthoritiesMethod`.
    """

    remove_authorized_address: RemoveAuthorizedAddressMethod
    """Constructor-initialized instance of
    :class:`RemoveAuthorizedAddressMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    remove_authorized_address_at_index: RemoveAuthorizedAddressAtIndexMethod
    """Constructor-initialized instance of
    :class:`RemoveAuthorizedAddressAtIndexMethod`.
    """

    get_proxy_id: GetProxyIdMethod
    """Constructor-initialized instance of
    :class:`GetProxyIdMethod`.
    """

    authorized: AuthorizedMethod
    """Constructor-initialized instance of
    :class:`AuthorizedMethod`.
    """

    get_authorized_addresses: GetAuthorizedAddressesMethod
    """Constructor-initialized instance of
    :class:`GetAuthorizedAddressesMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ERC20ProxyValidator = None,
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
            validator = ERC20ProxyValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=ERC20Proxy.abi()
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

        self.remove_authorized_address = RemoveAuthorizedAddressMethod(
            web3_or_provider,
            contract_address,
            functions.removeAuthorizedAddress,
            validator,
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
        )

        self.remove_authorized_address_at_index = RemoveAuthorizedAddressAtIndexMethod(
            web3_or_provider,
            contract_address,
            functions.removeAuthorizedAddressAtIndex,
            validator,
        )

        self.get_proxy_id = GetProxyIdMethod(
            web3_or_provider, contract_address, functions.getProxyId
        )

        self.authorized = AuthorizedMethod(
            web3_or_provider, contract_address, functions.authorized, validator
        )

        self.get_authorized_addresses = GetAuthorizedAddressesMethod(
            web3_or_provider,
            contract_address,
            functions.getAuthorizedAddresses,
        )

        self.transfer_ownership = TransferOwnershipMethod(
            web3_or_provider,
            contract_address,
            functions.transferOwnership,
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
                abi=ERC20Proxy.abi(),
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
                abi=ERC20Proxy.abi(),
            )
            .events.AuthorizedAddressRemoved()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"addAuthorizedAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"authorities","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"removeAuthorizedAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"removeAuthorizedAddressAtIndex","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getProxyId","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"authorized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAuthorizedAddresses","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"payable":false,"stateMutability":"nonpayable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AuthorizedAddressAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AuthorizedAddressRemoved","type":"event"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
