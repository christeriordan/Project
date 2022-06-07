class NonExcistingDrinkException(KeyError):
    def __init__(self, message="The selected drink is not available"):
        self.message = message
        super().__init__(message)


class NonExcistingPaymentException(KeyError):
    def __init__(self, message="The selected payment method is not available"):
        self.message = message
        super().__init__(message)


class SetPriceModelException(Exception):
    def __init__(self, message="Unaccepted input value, use type PriceModel"):
        self.message = message
        super().__init__(message)
