import os
import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_CONFIG = {
    "credentials": {
        "access_key": os.environ.get("cloud.aws.credentials.access_key"),
        "secret_key": os.environ.get("cloud.aws.credentials.secret_key")
    },
    "region": os.environ.get("cloud.aws.region"),
    "dynamodb": {
        "endpoint": os.environ.get("cloud.aws.dynamodb.endpoint"),
        "region": os.environ.get("cloud.aws.dynamodb.region"),
    }
}

def get_table(table_name):
    boto3.setup_default_session(
        aws_access_key_id=AWS_CONFIG['credentials']['access_key'],
        aws_secret_access_key=AWS_CONFIG['credentials']['secret_key'],
        region_name=AWS_CONFIG['region']
    )

    dynamodb = boto3.resource('dynamodb', endpoint_url=AWS_CONFIG['dynamodb']['endpoint'])
    return dynamodb.Table(table_name)