# Standard library imports
import json

# Third party imports

# Local app imports
from services import cache_wrapper
from services import constants

def getAll():
  busstop_list_str = cache_wrapper.getValue(constants.BUSSTOP_HASH_ALL)
  busstop_list_hash = cache_wrapper.getValue(constants.BUSSTOP_HASH_KEY)

  busstop_list = json.loads(busstop_list_str)

  body = {
    "busStops": busstop_list,
    "lastUpdate": busstop_list_hash
  }

  return body
