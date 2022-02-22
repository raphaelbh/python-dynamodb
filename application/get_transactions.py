import utils.dynamodb_client as dynamodb_client
from utils.transaction import transaction
from boto3.dynamodb.conditions import Key

def get_transactions(user):
    table = dynamodb_client.get_table('Transactions')
    response = table.query(
        KeyConditionExpression = Key('user').eq(user)
    )
    return response['Items']

if __name__ == "__main__":
    transactions = get_transactions(transaction['user'])
    print("transactions:" + str(transactions))