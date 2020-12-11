# Standard library imports
import json
import os

# Third party imports

# Local app imports
from services import busstops_updater
from services import buses_updater

def hello(event, context):
    body = {}

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def busstops(event, context):
    busstops_updater.update_busstops()
    return {}

def buses(event, context):
    buses_updater.update_buses()
    return {}
