import json
import os
from retrieve_keys import get_lta_key
from landtransportsg import PublicTransport

lta_key = get_lta_key()
client = PublicTransport(lta_key)

def get(event, context):
    bus_list = client.bus_services()

    body = {
        "buses": bus_list
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
