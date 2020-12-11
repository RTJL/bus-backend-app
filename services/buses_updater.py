# Standard library imports
import json
import os
import logging
from datetime import datetime

# Third party imports
from landtransportsg import PublicTransport

# Local app imports
from services import cache_wrapper
from services import constants
from retrieve_keys import get_lta_key

lta_key = get_lta_key()
client = PublicTransport(lta_key)

def update_buses():
  latest_bus_list = client.bus_services()

  latest_bus_list_str = json.dumps(latest_bus_list, sort_keys=True)
  current_bus_list_str = cache_wrapper.getValue(constants.BUS_HASH_ALL)

  if (latest_bus_list_str != current_bus_list_str):
    set_buses_cache(latest_bus_list, latest_bus_list_str)
    logging.info("buses cache miss")


def set_buses_cache(bus_list, bus_list_str):
  logging.info("buses cache set")
  now = datetime.now()
  cache_wrapper.setValue(constants.BUS_HASH_KEY, str(now))
  cache_wrapper.setValue(constants.BUS_HASH_ALL, bus_list_str)
  
  for bus in bus_list:
    cache_wrapper.setValue(constants.BUS_HASH_PREFIX + bus['ServiceNo'], json.dumps(bus))

def delete_buses_cache():
  logging.info("buses cache delete")
  cache_wrapper.deleteKey(constants.BUS_HASH_KEY)
  cache_wrapper.deleteKey(constants.BUS_HASH_ALL)
  cache_wrapper.deletePrefixKey(constants.BUS_HASH_PREFIX)
