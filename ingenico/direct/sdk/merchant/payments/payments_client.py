#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.api_resource import ApiResource
from ingenico.direct.sdk.call_context import CallContext
from ingenico.direct.sdk.response_exception import ResponseException
from ingenico.direct.sdk.domain.cancel_payment_response import CancelPaymentResponse
from ingenico.direct.sdk.domain.capture_payment_request import CapturePaymentRequest
from ingenico.direct.sdk.domain.capture_response import CaptureResponse
from ingenico.direct.sdk.domain.captures_response import CapturesResponse
from ingenico.direct.sdk.domain.complete_payment_request import CompletePaymentRequest
from ingenico.direct.sdk.domain.complete_payment_response import CompletePaymentResponse
from ingenico.direct.sdk.domain.create_payment_request import CreatePaymentRequest
from ingenico.direct.sdk.domain.create_payment_response import CreatePaymentResponse
from ingenico.direct.sdk.domain.error_response import ErrorResponse
from ingenico.direct.sdk.domain.payment_error_response import PaymentErrorResponse
from ingenico.direct.sdk.domain.payment_response import PaymentResponse
from ingenico.direct.sdk.domain.refund_error_response import RefundErrorResponse
from ingenico.direct.sdk.domain.refund_request import RefundRequest
from ingenico.direct.sdk.domain.refund_response import RefundResponse
from ingenico.direct.sdk.domain.refunds_response import RefundsResponse
from ingenico.direct.sdk.merchant.payments.i_payments_client import IPaymentsClient


class PaymentsClient(ApiResource, IPaymentsClient):
    """
    Payments client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.direct.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(PaymentsClient, self).__init__(parent, path_context)

    def create_payment(self, body: CreatePaymentRequest, context: CallContext = None) -> CreatePaymentResponse:
        """
        Resource /v2/{merchantId}/payments - Create payment

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/CreatePaymentApi

        :param body: :class:`ingenico.direct.sdk.domain.create_payment_request.CreatePaymentRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.create_payment_response.CreatePaymentResponse`
        :raise: DeclinedPaymentException if the Ingenico ePayments platform declined / rejected the payment. The payment result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v2/{merchantId}/payments", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreatePaymentResponse,
                    context)

        except ResponseException as e:
            error_type = PaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_payment(self, payment_id: str, context: CallContext = None) -> PaymentResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId} - Get payment

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetPaymentApi

        :param payment_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.payment_response.PaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    PaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def complete_payment(self, payment_id: str, body: CompletePaymentRequest, context: CallContext = None) -> CompletePaymentResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/complete - Complete payment

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/CompletePaymentApi

        :param payment_id: str
        :param body: :class:`ingenico.direct.sdk.domain.complete_payment_request.CompletePaymentRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.complete_payment_response.CompletePaymentResponse`
        :raise: DeclinedPaymentException if the Ingenico ePayments platform declined / rejected the payment. The payment result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/complete", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CompletePaymentResponse,
                    context)

        except ResponseException as e:
            error_type = PaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancel_payment(self, payment_id: str, context: CallContext = None) -> CancelPaymentResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/cancel - Cancel payment

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/CancelPaymentApi

        :param payment_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.cancel_payment_response.CancelPaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/cancel", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    CancelPaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def refund_payment(self, payment_id: str, body: RefundRequest, context: CallContext = None) -> RefundResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/refund - Refund payment

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/RefundPaymentApi

        :param payment_id: str
        :param body: :class:`ingenico.direct.sdk.domain.refund_request.RefundRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.refund_response.RefundResponse`
        :raise: DeclinedRefundException if the Ingenico ePayments platform declined / rejected the refund. The refund result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/refund", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    RefundResponse,
                    context)

        except ResponseException as e:
            error_type = RefundErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def capture_payment(self, payment_id: str, body: CapturePaymentRequest, context: CallContext = None) -> CaptureResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/capture - Capture payment

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/CapturePaymentApi

        :param payment_id: str
        :param body: :class:`ingenico.direct.sdk.domain.capture_payment_request.CapturePaymentRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.capture_response.CaptureResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/capture", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CaptureResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_captures(self, payment_id: str, context: CallContext = None) -> CapturesResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/captures - Get Captures Api

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetCapturesApi

        :param payment_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.captures_response.CapturesResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/captures", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    CapturesResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_refunds(self, payment_id: str, context: CallContext = None) -> RefundsResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/refunds - Get Refunds Api

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetRefundsApi

        :param payment_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.refunds_response.RefundsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/refunds", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    RefundsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
