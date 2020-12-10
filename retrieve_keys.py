import os
import boto3

client = boto3.client('ssm')
stage = os.environ.get('STAGE')

def get_secret(key):
    resp = client.get_parameter(
        Name=key,
        WithDecryption=False
    )
    return resp['Parameter']['Value']

def get_lta_key():
    local_key = "LTA_ACCOUNT_KEY"
    stage_key = "/bus/lta_api_key"
    lta_key = get_env_var(local_key, stage_key)
    return lta_key

def get_cache_endpoint():
    local_key = "CACHE_ENDPOINT"
    stage_key = '/bus-backend-infra/'+ stage + '/elasticache/endpoint'
    cache_endpoint = get_env_var(local_key, stage_key)
    return cache_endpoint

def get_env_var(local_env_key, stage_env_key):
    if stage == "local":
        value = os.environ.get(local_env_key)
    else:
        value = get_secret(stage_env_key)
    return value