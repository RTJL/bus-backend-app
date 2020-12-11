# Standard library imports
import json

# Third party imports

# Local app imports
from services import cache_wrapper
from services import constants

def getAll():
  bus_list_str = cache_wrapper.getValue(constants.BUS_HASH_ALL)
  bus_list_hash = cache_wrapper.getValue(constants.BUS_HASH_KEY)

  bus_list = json.loads(bus_list_str)

  body = {
    "buses": bus_list,
    "lastUpdate": bus_list_hash
  }
  
  return body
