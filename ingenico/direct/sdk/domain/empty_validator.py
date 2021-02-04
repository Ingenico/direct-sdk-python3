# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject


class EmptyValidator(DataObject):

    def to_dictionary(self):
        dictionary = super(EmptyValidator, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(EmptyValidator, self).from_dictionary(dictionary)
        return self
