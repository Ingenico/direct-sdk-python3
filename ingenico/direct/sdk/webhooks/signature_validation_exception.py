class SignatureValidationException(RuntimeError):
    """
    Represents an error while validating webhooks signatures.
    """

    def __init__(self, param, cause=False):
        if not cause:
            super(SignatureValidationException, self).__init__(param)
        else:
            super(SignatureValidationException, self).__init__(param, cause)
