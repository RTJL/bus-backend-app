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

def update_busstops():
  latest_busstop_list = client.bus_stops()
  
  latest_busstop_list_str = json.dumps(latest_busstop_list, sort_keys=True)
  current_bus_list_str = cache_wrapper.getValue(constants.BUSSTOP_HASH_ALL)

  if (latest_busstop_list_str != current_bus_list_str):
    delete_busstops_cache()
    set_busstops_cache(latest_busstop_list, latest_busstop_list_str)
    logging.info("busstops cache miss")

def set_busstops_cache(busstop_list, bus_list_str):
  now = datetime.now()
  cache_wrapper.setValue(constants.BUSSTOP_HASH_KEY, str(now))
  cache_wrapper.setValue(constants.BUSSTOP_HASH_ALL, bus_list_str)
  
  for busstop in busstop_list:
    cache_wrapper.setValue(constants.BUSSTOP_HASH_PREFIX + busstop['BusStopCode'], json.dumps(busstop))
  
  logging.info("busstops cache set")

def delete_busstops_cache():
  cache_wrapper.deleteKey(constants.BUSSTOP_HASH_KEY)
  cache_wrapper.deleteKey(constants.BUSSTOP_HASH_ALL)
  cache_wrapper.deletePrefixKey(constants.BUSSTOP_HASH_PREFIX)
  
  logging.info("busstops cache delete")
