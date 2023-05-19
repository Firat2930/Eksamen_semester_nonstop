# Contract
class Contract:
    def __init__(self, contract_id, customer_id, content):
        self.id = contract_id
        self.customer_id = customer_id
        self.content = content
        self.status = 'draft'

    def get_status(self):
        return self.status

    def sign(self):
        self.status = 'signed'