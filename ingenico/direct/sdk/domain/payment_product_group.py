# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.account_on_file import AccountOnFile
from ingenico.direct.sdk.domain.payment_product_display_hints import PaymentProductDisplayHints


class PaymentProductGroup(DataObject):

    __account_on_file = None
    __display_hints = None
    __id = None

    @property
    def account_on_file(self) -> AccountOnFile:
        """
        Type: :class:`ingenico.direct.sdk.domain.account_on_file.AccountOnFile`
        """
        return self.__account_on_file

    @account_on_file.setter
    def account_on_file(self, value: AccountOnFile):
        self.__account_on_file = value

    @property
    def display_hints(self) -> PaymentProductDisplayHints:
        """
        | Object containing display hints like the order of the product when shown in a list, the name of the product and the logo

        Type: :class:`ingenico.direct.sdk.domain.payment_product_display_hints.PaymentProductDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value: PaymentProductDisplayHints):
        self.__display_hints = value

    @property
    def id(self) -> str:
        """
        | The ID of the payment product group in our system

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    def to_dictionary(self):
        dictionary = super(PaymentProductGroup, self).to_dictionary()
        if self.account_on_file is not None:
            dictionary['accountOnFile'] = self.account_on_file.to_dictionary()
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductGroup, self).from_dictionary(dictionary)
        if 'accountOnFile' in dictionary:
            if not isinstance(dictionary['accountOnFile'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['accountOnFile']))
            value = AccountOnFile()
            self.account_on_file = value.from_dictionary(dictionary['accountOnFile'])
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        return self
