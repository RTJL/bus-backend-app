# Standard library imports
import json
import os

# Third party imports

# Local app imports
from services import busstops

def get(event, context):
    body = busstops.getAll()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
