import uuid
import random

transaction = {
    'user': 'john',
    'transaction_id': str(uuid.uuid4()),
    'amout': (100 + random.randint(1, 100))
}