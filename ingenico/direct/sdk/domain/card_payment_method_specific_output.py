# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.card_essentials import CardEssentials
from ingenico.direct.sdk.domain.card_fraud_results import CardFraudResults
from ingenico.direct.sdk.domain.three_d_secure_results import ThreeDSecureResults


class CardPaymentMethodSpecificOutput(DataObject):
    """
    | Object containing the card payment method details
    """

    __authorisation_code = None
    __card = None
    __fraud_results = None
    __initial_scheme_transaction_id = None
    __payment_option = None
    __payment_product_id = None
    __three_d_secure_results = None
    __token = None

    @property
    def authorisation_code(self) -> str:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: str):
        self.__authorisation_code = value

    @property
    def card(self) -> CardEssentials:
        """
        | Object containing card details

        Type: :class:`ingenico.direct.sdk.domain.card_essentials.CardEssentials`
        """
        return self.__card

    @card.setter
    def card(self, value: CardEssentials):
        self.__card = value

    @property
    def fraud_results(self) -> CardFraudResults:
        """
        | Fraud results contained in the CardFraudResults object

        Type: :class:`ingenico.direct.sdk.domain.card_fraud_results.CardFraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value: CardFraudResults):
        self.__fraud_results = value

    @property
    def initial_scheme_transaction_id(self) -> str:
        """
        | The unique scheme transactionId of the initial transaction that was performed with SCA. In case this is unknown a scheme transactionId of an earlier transaction part of the same sequence can be used as a fall-back. Strongly advised to be submitted for any MerchantInitiated or recurring transaction (a subsequent one).

        Type: str
        """
        return self.__initial_scheme_transaction_id

    @initial_scheme_transaction_id.setter
    def initial_scheme_transaction_id(self, value: str):
        self.__initial_scheme_transaction_id = value

    @property
    def payment_option(self) -> str:
        """
        | The specific payment option for the payment. To be used as a complement of the more generic paymentProductId (oney, banquecasino, cofidis), which allows to define a variation of the selected paymentProductId (ex: facilypay3x, banquecasino4x, cofidis3x-sansfrais, ...). List of modalities included in the payment product page.

        Type: str
        """
        return self.__payment_option

    @payment_option.setter
    def payment_option(self, value: str):
        self.__payment_option = value

    @property
    def payment_product_id(self) -> int:
        """
        | Payment product identifier - Please see [payment products](https://support.direct.ingenico.com/documentation/api/reference/index.html#tag/Products) for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int):
        self.__payment_product_id = value

    @property
    def three_d_secure_results(self) -> ThreeDSecureResults:
        """
        | 3D Secure results object

        Type: :class:`ingenico.direct.sdk.domain.three_d_secure_results.ThreeDSecureResults`
        """
        return self.__three_d_secure_results

    @three_d_secure_results.setter
    def three_d_secure_results(self, value: ThreeDSecureResults):
        self.__three_d_secure_results = value

    @property
    def token(self) -> str:
        """
        | ID of the token. This property is populated when the payment was done with a token or when the payment was tokenized.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificOutput, self).to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.initial_scheme_transaction_id is not None:
            dictionary['initialSchemeTransactionId'] = self.initial_scheme_transaction_id
        if self.payment_option is not None:
            dictionary['paymentOption'] = self.payment_option
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.three_d_secure_results is not None:
            dictionary['threeDSecureResults'] = self.three_d_secure_results.to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardEssentials()
            self.card = value.from_dictionary(dictionary['card'])
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = CardFraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'initialSchemeTransactionId' in dictionary:
            self.initial_scheme_transaction_id = dictionary['initialSchemeTransactionId']
        if 'paymentOption' in dictionary:
            self.payment_option = dictionary['paymentOption']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'threeDSecureResults' in dictionary:
            if not isinstance(dictionary['threeDSecureResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecureResults']))
            value = ThreeDSecureResults()
            self.three_d_secure_results = value.from_dictionary(dictionary['threeDSecureResults'])
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
