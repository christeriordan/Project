from ExceptionHandlers import NonExcistingPaymentException


PAYMENTMETHODS = {"Cash": "$", "CreditCard": "#"}

# Future work. Add handlers for the payment methods


class PaymentMethod:
    def __init__(self, method):
        try:
            self.method = PAYMENTMETHODS[method]
        except KeyError:
            raise NonExcistingPaymentException

    def add_payment_method(self, method_name, method_handler):

        PAYMENTMETHODS[method_name] = method_handler
