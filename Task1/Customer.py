from Payment import PaymentMethod as pm
import Drink
import ExceptionHandlers


class Customer(pm):
    def __init__(self, name, method):
        self.name = name
        self.method = method
        self.current_amount = 0
        super().__init__(method)  # inherit from PaymentMethod

    def get_current_amount(self):
        return self.current_amount

    def customer_one_order(self, beverage, name, amount):
        if beverage == "Beer":
            drink_object = Drink.Beer(name, amount, 100)
            self.current_amount += drink_object.price_one_order()
        elif beverage == "Wine":
            drink_object = Drink.Wine(name, amount, 150)
            self.current_amount += drink_object.price_one_order()
        elif beverage == "Juice":
            drink_object = Drink.Juice(name, amount, 50)
            self.current_amount += drink_object.price_one_order()
        else:
            raise ExceptionHandlers.NonExcistingDrinkException
        return drink_object

    def customer_multiple_orders(self):
        price = Drink.Drinks().total_price()
        self.current_amount = self.current_amount + price
        return self.current_amount

    def __str__(self):
        return 'Customer %s will be paying with %s. The total price is: %i' % (self.name, self.method, self.current_amount)
