# Standard library imports
import json
import os

# Third party imports

# Local app imports
from services import buses

def get(event, context):
    body = buses.getAll()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
