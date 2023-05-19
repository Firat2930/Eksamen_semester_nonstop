# Customer Repository
class CustomerRepository:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None