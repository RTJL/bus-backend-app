# Standard library imports
# Standard library imports
import json
import os
import logging

# Third party imports

# Local app imports
from services import busstops
from services import cache_wrapper

BUSSTOP_HASH_KEY = "bus_hash"
BUSSTOP_HASH_PREFIX = "busstop-"
BUSSTOP_HASH_ALL = "busstop-all"

def update_busstops():
  busstop_list = busstops.getAll()

  latest_hash = hash(str(busstop_list))
  current_hash = cache_wrapper.getValue(BUSSTOP_HASH_KEY)

  if (current_hash != latest_hash):
    set_busstops_cache(busstop_list, latest_hash)
    logging.info("Cache miss. Updating with latest bus services list")

def set_busstops_cache(busstop_list, latest_hash):
  cache_wrapper.setValue(BUSSTOP_HASH_ALL, json.dumps(busstop_list))
  cache_wrapper.setValue(BUSSTOP_HASH_KEY, latest_hash)
  for busstop in busstop_list:
    cache_wrapper.setValue(BUSSTOP_HASH_PREFIX + busstop['BusStopCode'], json.dumps(busstop))
