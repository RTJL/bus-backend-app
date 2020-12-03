import json
import os
import logging
from retrieve_keys import get_lta_key
from landtransportsg import PublicTransport

lta_key = get_lta_key()
client = PublicTransport(lta_key)

def hello(event, context):
    body = {}

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def bus_services():
    bus_list = client.bus_services()
    
    if len(bus_list) == 0:
        logging.error("LTA bus services list empty")
        return None
    
    new_hash = hash(str(bus_list))
    # TODO: Compare with redis cache
    old_hash = "89765343456"

    if new_hash == old_hash:
        logging.info("Cache hit. No changes in cache")
        return None
    
    # TODO: Update redis cache with new hash & values
    logging.info("Cache miss. Updating with latest bus services list")
    return bus_list
