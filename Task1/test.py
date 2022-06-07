import unittest
import Drink
import Discount
import Customer
import Orders
from PriceModel import PriceModel


class Test(unittest.TestCase):
    # Sets the Discount.Discountount.PriceModel to Regular for tests where
    # set_priceModel() is not used.
    def setUp(self):
        Discount.Discount().set_priceModel(PriceModel.Regular)

    # ---   Discount    ---

    def test_set_PriceModel_is_static(self):
        # Test to check if Discount.Discountount.priceModel is a static variable.
        Discount.Discount1 = Discount.Discount()
        Discount.Discount2 = Discount.Discount()
        Discount.Discount1.set_priceModel(PriceModel.HappyHour)
        Discount.Discount2.set_priceModel(PriceModel.Regular)

        self.assertEqual(Discount.Discount1.get_priceModel(),
                         Discount.Discount2.get_priceModel())

    def test_set_priceModel_exception(self):
        # test to see if Pricemodel.priceModel.set_priceModel()
        # raises an exception if an invalid parameter is given.
        self.assertRaises(Exception, Discount.Discount().set_priceModel,
                          "Incorrect parameter")

    def test_set_priceModel_no_exception(self):
        # test to se if Pricemodel.priceModel.set_priceModel()
        # does not raise an exception if a valid parameter is given.
        try:
            Discount.Discount().set_priceModel(PriceModel.HappyHour)
        except:
            self.fail()

    def test_price_model(self):
        # test to see if PriceModel.priceModel yields the correct value.
        self.assertEqual(0, Discount.Discount().priceModel.value)

    def test_calculate_price_regular(self):
        # test to see if Discount.Discountount.calculate_price() yeilds the correct value for the
        # default value for priceModel = Regular
        self.assertEqual(Discount.Discount().calculate_price(100), 100)

    def test_calculate_price_HappyHour(self):
        # test to see if calculate_price() works as intended for HappyHour
        Discount.Discount().set_priceModel(PriceModel.HappyHour)
        self.assertEqual(Discount.Discount().calculate_price(900), 450)

    def test_calculate_price_BlackFriday(self):
        # test to see if calculate_price() works as inteded for BlackFriday
        Discount.Discount().set_priceModel(PriceModel.BlackFriday)
        self.assertEqual(Discount.Discount().calculate_price(900), 800)

    def test_calculate_price_BlackFriday_price_below_500(self):
        # Test to see if calculate_price() works as inteded for BlackFriday
        # if price < 500
        Discount.Discount().set_priceModel(PriceModel.BlackFriday)
        self.assertEqual(Discount.Discount().calculate_price(450), 450)
    # ---   Drink   ---

    def test_Beer_one_order(self):
        # Test to see if Drink.Drinks.price_one_order() works as intended.
        beer = Drink.Beer("Beer", 2, 100)
        self.assertEqual(beer.price_one_order(), 200)

    def test_beer_price_per_unit_happyHour(self):
        # test to see if Discount.Discountount.calculate_price()
        #  yeilds the correct value for HappyHour
        beer = Drink.Beer("Beer", 2, 100)
        Discount.Discount().set_priceModel(PriceModel.HappyHour)
        self.assertEqual(beer.price_one_order(), 100)

    def test_beer_price_one_unit_BlackFriday(self):
        # test if total price returns 200, even though PriceModel is set to BlackFriday
        # Should only give discount if price >= 500
        Discount.Discount().set_priceModel(PriceModel.BlackFriday)
        beer = Drink.Beer("Beer", 2, 100)
        self.assertEqual(beer.price_one_order(), 200)

        # test if BlackFriday works as intended and subtracts 100 from the total price.
        new_beer = Drink.Beer("Beer", 10, 100)
        self.assertEqual(new_beer.price_one_order(), 900)

    def test_Beer_total_price(self):
        # Test the Drink.Drinks().total_price() works as intended
        beer = Drink.Drinks()
        self.assertEqual(beer.total_price(), 650)

    # ----    Customer    ---

    def test_customer_one_order_raise_exeption(self):
        # Test to see if an exception is cast if customer_one_order() gets an invalid
        # parameter
        self.assertRaises(Exception, Customer.Customer(
            "Christer", "Cash").customer_one_order, "wrongParameter", "Tou", 1)

    def test_customer_one_order_no_exception(self):
        try:
            Customer.Customer("Christer", "CreditCard").customer_one_order(
                "Beer", "Salikatt", 3)
        except:
            self.fail()

    def test_customer_one_order(self):
        # test if the customer_one_order() works as intended
        self.assertEqual(Customer.Customer(
            "Christer", "Cash").customer_one_order("Beer", "Tuborg", 1).price_one_order(), 100)

    def test_customer_multiple_orders(self):
        # Test the customer_multiple_orders()
        self.assertEqual(Customer.Customer(
            "Christer", "Cash").customer_multiple_orders(), 650)

    def test_customer_one_order_HappyHour(self):
        # Test to see if HappyHour state is working as intended through the Customer class
        Discount.Discount().set_priceModel(PriceModel.HappyHour)
        self.assertEqual(Customer.Customer(
            "Christer", "CreditCard").customer_one_order("Beer", "Salikatt", 1).price_one_order(), 50)

    def test_customer_multiple_orders_HappyHour(self):
        # Test to see if HappyHour state is working as intended through the Customer class
        Discount.Discount().set_priceModel(PriceModel.HappyHour)
        self.assertEqual(Customer.Customer(
            "Christer", "Cash").customer_multiple_orders(), 325)

    def test_customer_oneOrder_and_multiple_orders(self):
        # test to see if the correct price is generated when ordering a combination of
        # multiple orders and single orders.
        cust = Customer.Customer("Christer", "Cash")
        Discount.Discount().set_priceModel(PriceModel.BlackFriday)

        cust.customer_one_order("Beer", "Tou", 1)
        self.assertEqual(cust.get_current_amount(), 100)
        cust.customer_one_order("Beer", "Tou", 1)
        self.assertEqual(cust.get_current_amount(), 200)
        cust.customer_multiple_orders()  # price = 650
        self.assertEqual(cust.get_current_amount(), 750)
        cust.customer_multiple_orders()
        self.assertEqual(cust.get_current_amount(), 1300)
        cust.customer_multiple_orders()
        self.assertEqual(cust.get_current_amount(), 1850)
        cust.customer_one_order("Beer", "Tou", 1)
        self.assertEqual(cust.get_current_amount(), 1950)

    # ---   Order   ---
    def test_get_order_correct_type(self):
        # Test to see if the elements added to self.orders are of correct type
        for i in Orders.Order().get_order():
            self.assertIsInstance(i, Drink.Drinks)

    def test_get_order_from_user_append(self):
        # test the append method in get_order_from_users()
        self.assertEqual(len(Orders.Order().get_order_from_users()), 3)


if __name__ == "__main__":
    unittest.main()
