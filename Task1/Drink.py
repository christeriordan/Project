import Orders
from Discount import Discount as disc


class Drinks(disc):
    def __init__(self):
        super().__init__()  # inherit the Discount class

    def price_one_order(self):
        return self.calculate_price(self.price)

    def total_price(self):
        orders = Orders.Order().get_order()
        current_price = 0
        for i in orders:
            current_price += i.price
        final_price = self.calculate_price(current_price)
        return final_price


class Beer(Drinks):
    def __init__(self, name, amount, price):
        super().__init__()
        self.name = name
        self.price = amount * price


class Wine(Drinks):
    def __init__(self, name, amount, price):
        super().__init__()
        self.name = name
        self.price = amount * price


class Juice(Drinks):
    def __init__(self, name, amount, price):
        super().__init__()
        self.name = name
        self.price = amount * price
