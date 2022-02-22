import utils.dynamodb_client as dynamodb_client
from utils.transaction import transaction

def save(input_transaction):
    table = dynamodb_client.get_table('Transactions')
    table.put_item(Item=input_transaction)
    
if __name__ == "__main__":
    save(transaction)