# Standard library imports
import json
import os

# Third party imports

# Local app imports
from services import busstops

def get(event, context):
    busstop_list = busstops.getAll()

    body = {
        "busStops": busstop_list
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
