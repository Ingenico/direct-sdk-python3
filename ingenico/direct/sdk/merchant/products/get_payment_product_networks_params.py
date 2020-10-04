# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.param_request import ParamRequest
from ingenico.direct.sdk.request_param import RequestParam


class GetPaymentProductNetworksParams(ParamRequest):
    """
    Query parameters for Get payment product networks

    See also https://support.direct.ingenico.com/documentation/api/reference/index.html#operation/GetPaymentProductNetworks
    """

    __country_code = None
    __currency_code = None
    __amount = None
    __is_recurring = None

    @property
    def country_code(self):
        """
        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def currency_code(self):
        """
        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value):
        self.__currency_code = value

    @property
    def amount(self):
        """
        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def is_recurring(self):
        """
        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        if self.country_code is not None:
            result.append(RequestParam("countryCode", self.country_code))
        if self.currency_code is not None:
            result.append(RequestParam("currencyCode", self.currency_code))
        if self.amount is not None:
            result.append(RequestParam("amount", str(self.amount)))
        if self.is_recurring is not None:
            result.append(RequestParam("isRecurring", str(self.is_recurring)))
        return result