import ContractSender
import CustomerRepository
import DatabaseConnector
import Customer
import Contract


# Usage Example
def main():
    # Create database connector and connect to the database
    database_connector = DatabaseConnector("contracts.db")
    database_connector.connect()

    # Create customer repository
    customer_repository = CustomerRepository()

    # Create some customers
    customer1 = Customer(1, "John Doe", "john.doe@example.com")
    customer2 = Customer(2, "Jane Smith", "jane.smith@example.com")
    customer_repository.add_customer(customer1)
    customer_repository.add_customer(customer2)

    # Create contract sender
    contract_sender = ContractSender(customer_repository, database_connector)

    # Send a contract to a customer
    contract_sender.send_contract(1, "Contract 1 content")

    # Get the contracts for a customer
    customer_contracts = customer_repository.get_customer_by_id(1).get_contracts()
    print("Contracts for customer 1:")
    for contract in customer_contracts:
        print("Contract ID:", contract.id)
        print("Content:", contract.content)
        print("Status:", contract.get_status())

    # Close the database connection
    database_connector.connection

    if __name__ == "__main__":
        main()