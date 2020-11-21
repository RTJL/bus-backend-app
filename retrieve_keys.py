import os
import boto3

client = boto3.client('ssm')

def get_secret(key):
    resp = client.get_parameter(
        Name=key,
        WithDecryption=False
    )
    return resp['Parameter']['Value']

def get_lta_key():
    lta_key = os.environ.get('LTA_ACCOUNT_KEY')
    if lta_key == None:
        lta_key = get_secret('/bus/lta_api_key')
    return lta_key