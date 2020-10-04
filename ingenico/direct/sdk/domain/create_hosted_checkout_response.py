# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from typing import List

from ingenico.direct.sdk.data_object import DataObject


class CreateHostedCheckoutResponse(DataObject):

    __returnmac = None
    __hosted_checkout_id = None
    __invalid_tokens = None
    __merchant_reference = None
    __partial_redirect_url = None

    @property
    def returnmac(self) -> str:
        """
        | When the customer is returned to your site we will append this property and value to the query-string. You should store this data, so you can identify the returning customer.

        Type: str
        """
        return self.__returnmac

    @returnmac.setter
    def returnmac(self, value: str):
        self.__returnmac = value

    @property
    def hosted_checkout_id(self) -> str:
        """
        | The ID of the Hosted Checkout Session in which the payment was made.

        Type: str
        """
        return self.__hosted_checkout_id

    @hosted_checkout_id.setter
    def hosted_checkout_id(self, value: str):
        self.__hosted_checkout_id = value

    @property
    def invalid_tokens(self) -> List[str]:
        """
        | Tokens that are submitted in the request are validated. In case any of the tokens can't be used anymore they are returned in this array. You should most likely remove those tokens from your system.

        Type: list[str]
        """
        return self.__invalid_tokens

    @invalid_tokens.setter
    def invalid_tokens(self, value: List[str]):
        self.__invalid_tokens = value

    @property
    def merchant_reference(self) -> str:
        """
        | Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files.

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: str):
        self.__merchant_reference = value

    @property
    def partial_redirect_url(self) -> str:
        """
        | The partial URL as generated by our system. You will need to add the protocol and the relevant subdomain to this URL, before redirecting your customer to this URL. A special 'payment' subdomain will always work so you can always add 'https://payment.' at the beginning of this response value to view your hosted pages.

        Type: str
        """
        return self.__partial_redirect_url

    @partial_redirect_url.setter
    def partial_redirect_url(self, value: str):
        self.__partial_redirect_url = value

    def to_dictionary(self):
        dictionary = super(CreateHostedCheckoutResponse, self).to_dictionary()
        if self.returnmac is not None:
            dictionary['RETURNMAC'] = self.returnmac
        if self.hosted_checkout_id is not None:
            dictionary['hostedCheckoutId'] = self.hosted_checkout_id
        if self.invalid_tokens is not None:
            dictionary['invalidTokens'] = []
            for element in self.invalid_tokens:
                if element is not None:
                    dictionary['invalidTokens'].append(element)
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.partial_redirect_url is not None:
            dictionary['partialRedirectUrl'] = self.partial_redirect_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateHostedCheckoutResponse, self).from_dictionary(dictionary)
        if 'RETURNMAC' in dictionary:
            self.returnmac = dictionary['RETURNMAC']
        if 'hostedCheckoutId' in dictionary:
            self.hosted_checkout_id = dictionary['hostedCheckoutId']
        if 'invalidTokens' in dictionary:
            if not isinstance(dictionary['invalidTokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['invalidTokens']))
            self.invalid_tokens = []
            for element in dictionary['invalidTokens']:
                self.invalid_tokens.append(element)
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'partialRedirectUrl' in dictionary:
            self.partial_redirect_url = dictionary['partialRedirectUrl']
        return self