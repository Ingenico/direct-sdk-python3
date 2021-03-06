# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.airline_data import AirlineData
from ingenico.direct.sdk.domain.loan_recipient import LoanRecipient
from ingenico.direct.sdk.domain.order_type_information import OrderTypeInformation


class AdditionalOrderInput(DataObject):
    """
    | Object containing additional input on the order
    """

    __airline_data = None
    __loan_recipient = None
    __type_information = None

    @property
    def airline_data(self) -> AirlineData:
        """
        | Object that holds airline specific data

        Type: :class:`ingenico.direct.sdk.domain.airline_data.AirlineData`
        """
        return self.__airline_data

    @airline_data.setter
    def airline_data(self, value: AirlineData):
        self.__airline_data = value

    @property
    def loan_recipient(self) -> LoanRecipient:
        """
        | Object containing specific data regarding the recipient of a loan in the UK

        Type: :class:`ingenico.direct.sdk.domain.loan_recipient.LoanRecipient`
        """
        return self.__loan_recipient

    @loan_recipient.setter
    def loan_recipient(self, value: LoanRecipient):
        self.__loan_recipient = value

    @property
    def type_information(self) -> OrderTypeInformation:
        """
        | Object that holds the purchase and usage type indicators

        Type: :class:`ingenico.direct.sdk.domain.order_type_information.OrderTypeInformation`
        """
        return self.__type_information

    @type_information.setter
    def type_information(self, value: OrderTypeInformation):
        self.__type_information = value

    def to_dictionary(self):
        dictionary = super(AdditionalOrderInput, self).to_dictionary()
        if self.airline_data is not None:
            dictionary['airlineData'] = self.airline_data.to_dictionary()
        if self.loan_recipient is not None:
            dictionary['loanRecipient'] = self.loan_recipient.to_dictionary()
        if self.type_information is not None:
            dictionary['typeInformation'] = self.type_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(AdditionalOrderInput, self).from_dictionary(dictionary)
        if 'airlineData' in dictionary:
            if not isinstance(dictionary['airlineData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['airlineData']))
            value = AirlineData()
            self.airline_data = value.from_dictionary(dictionary['airlineData'])
        if 'loanRecipient' in dictionary:
            if not isinstance(dictionary['loanRecipient'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['loanRecipient']))
            value = LoanRecipient()
            self.loan_recipient = value.from_dictionary(dictionary['loanRecipient'])
        if 'typeInformation' in dictionary:
            if not isinstance(dictionary['typeInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['typeInformation']))
            value = OrderTypeInformation()
            self.type_information = value.from_dictionary(dictionary['typeInformation'])
        return self
