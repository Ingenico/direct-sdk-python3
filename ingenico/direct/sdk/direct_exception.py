from ingenico.direct.sdk.api_exception import ApiException


class DirectException(ApiException):
    """
    Represents an error response from the Ingenico ePayments platform when something
    went wrong at the Ingenico ePayments platform or further downstream.
    """

    def __init__(self, status_code, response_body, error_id, errors, message="the Ingenico ePayments platform returned an error response"):
        super(DirectException, self).__init__(status_code, response_body, error_id, errors, message)
