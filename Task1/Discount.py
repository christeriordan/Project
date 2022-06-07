from PriceModel import PriceModel
from ExceptionHandlers import SetPriceModelException


class Discount():
    # Default state
    priceModel = PriceModel.Regular

    def get_priceModel(self):
        # Used in the test class
        return Discount.priceModel

    def set_priceModel(self, priceModel):
        # Sets the state of the Discount class.
        if not isinstance(priceModel, PriceModel):
            raise SetPriceModelException
        Discount.priceModel = priceModel

    def calculate_price(self, price):
        # Calculates the price of drinks with respect to the priceModel state.
        if Discount.priceModel == PriceModel.BlackFriday and price >= PriceModel.BlackFriday.value[1]:
            return price - PriceModel.BlackFriday.value[0]
        elif Discount.priceModel == PriceModel.HappyHour:
            return price - (price * Discount.priceModel.value)
        elif Discount.priceModel == PriceModel.Regular:
            return price - (price * Discount.priceModel.value)
        else:
            return price - (price * PriceModel.Regular.value)
