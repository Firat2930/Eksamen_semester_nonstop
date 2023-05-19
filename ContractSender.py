# Contract Sender
class ContractSender:
    def __init__(self, customer_repository, database_connector):
        self.customer_repository = customer_repository
        self.database_connector = database_connector

    def send_contract(self, customer_id, contract_content):
        customer = self.customer_repository.get_customer_by_id(customer_id)
        if customer is None:
            print("Customer not found!")
            return

        contract_id = len(customer.contracts) + 1
        contract = Contract(contract_id, customer_id, contract_content)
        customer.add_contract(contract)
        self.database_connector.save_contract(contract)
        print("Contract sent successfully to customer", customer.name)
