# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from typing import List
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.api_error import APIError


class ErrorResponse(DataObject):

    __error_id = None
    __errors = None

    @property
    def error_id(self) -> str:
        """
        | Unique reference, for debugging purposes, of this error response

        Type: str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value: str):
        self.__error_id = value

    @property
    def errors(self) -> List[APIError]:
        """
        | List of one or more errors

        Type: list[:class:`ingenico.direct.sdk.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: List[APIError]):
        self.__errors = value

    def to_dictionary(self):
        dictionary = super(ErrorResponse, self).to_dictionary()
        if self.error_id is not None:
            dictionary['errorId'] = self.error_id
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(ErrorResponse, self).from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        return self
