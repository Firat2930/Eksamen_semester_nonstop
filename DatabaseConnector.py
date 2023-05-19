import mysql.connector
import Customer
import ContractSender
import Contract
import CustomerRepository


class DatabaseConnector:
    def __init__(self, database_url):
        self.database_url = database_url

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.database_url,
                user='brugernavn',
                password='adgangskode',
                database='databasenavn'
            )
            self.cursor = self.connection.cursor()
            print("Forbindelse til databasen oprettet.")
        except mysql.connector.Error as error:
            print(f"Fejl under oprettelse af forbindelse til databasen: {error}")

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Forbindelse til databasen lukket.")

    def fetch_customer(self, customer_id):
        query = f"SELECT * FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        customer_data = self.cursor.fetchone()
        if customer_data:
            customer = Customer(*customer_data)
            return customer
        else:
            print("Kunde ikke fundet.")
            return None


# Opret en instans af DatabaseConnector
database_connector = DatabaseConnector("localhost")

# Opret forbindelse til databasen
database_connector.connect()

# Hent kundeoplysninger fra databasen
customer_id = 1
customer = database_connector.fetch_customer(customer_id)

if customer:
    print("Kunde fundet:")
    print("ID:", customer.id)
    print("Navn:", customer.name)
    print("E-mail:", customer.email)
    print("CVR:", customer.cvr)
else:
    print("Kunde ikke fundet.")

# Luk forbindelsen til databasen
database_connector.disconnect()
