"""Generated wrapper for IWallet Solidity contract."""

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
# constructor for IWallet below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IWalletValidator,
    )
except ImportError:

    class IWalletValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IsValidSignatureMethod(ContractMethod):
    """Various interfaces to the isValidSignature method."""

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
        self, _hash: Union[bytes, str], signature: Union[bytes, str]
    ):
        """Validate the inputs to the isValidSignature method."""
        self.validator.assert_valid(
            method_name="isValidSignature",
            parameter_name="hash",
            argument_value=_hash,
        )
        self.validator.assert_valid(
            method_name="isValidSignature",
            parameter_name="signature",
            argument_value=signature,
        )
        return (_hash, signature)

    def call(
        self,
        _hash: Union[bytes, str],
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        Validates a hash with the `Wallet` signature type.

        :param hash: Message hash that is signed.
        :param signature: Proof of signing.
        :param tx_params: transaction parameters
        :returns: magicValue `bytes4(0xb0671381)` if the signature check
            succeeds.
        """
        (_hash, signature) = self.validate_and_normalize_inputs(
            _hash, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_hash, signature).call(
            tx_params.as_dict()
        )
        return Union[bytes, str](returned)

    def estimate_gas(
        self,
        _hash: Union[bytes, str],
        signature: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_hash, signature) = self.validate_and_normalize_inputs(
            _hash, signature
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_hash, signature).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IWallet:
    """Wrapper class for IWallet Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    is_valid_signature: IsValidSignatureMethod
    """Constructor-initialized instance of
    :class:`IsValidSignatureMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IWalletValidator = None,
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
            validator = IWalletValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=IWallet.abi()
        ).functions

        self.is_valid_signature = IsValidSignatureMethod(
            web3_or_provider,
            contract_address,
            functions.isValidSignature,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":true,"inputs":[{"internalType":"bytes32","name":"hash","type":"bytes32"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"isValidSignature","outputs":[{"internalType":"bytes4","name":"magicValue","type":"bytes4"}],"payable":false,"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
