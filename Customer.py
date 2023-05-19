# Customer
class Customer:
    def __init__(self, customer_id, name, email):
        self.id = customer_id
        self.name = name
        self.email = email
        self.contracts = []

    def add_contract(self, contract):
        self.contracts.append(contract)

    def get_contracts(self):
        return self.contracts