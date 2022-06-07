import Customer


class Order():
    def __init__(self):
        self.orders = []
        self.exit = False
        self.in_stock = ["Beer", "Wine", "Juice"]

    def get_order(self):
        # manually inserting Drink objects into self.orders for smoother testing
        cust = Customer.Customer("Christer", "Cash")
        self.orders.append(cust.customer_one_order("Beer", "Salikatt", 2))
        self.orders.append(cust.customer_one_order("Wine", "Radicon", 2))
        self.orders.append(cust.customer_one_order("Juice", "Apple", 3))

        return self.orders

    def get_order_from_users(self):
        while self.exit == False:
            for i in self.in_stock:
                print("In stock: %s" % i)
            beverage = input("What type of beverage do you want? ")
            beverageName = input("Name of beverage: ")
            amount = int(input("How many? "))

            self.orders.append(Customer.Customer("Christer", "Cash").customer_one_order(
                beverage, beverageName, amount))
            answer = input("Do you want to order something else y/n ")
            if answer == "n":
                self.exit = True
        return self.orders
