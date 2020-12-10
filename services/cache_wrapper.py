# Standard library imports
import redis

# Third party imports

# Local app imports
from retrieve_keys import get_cache_endpoint

endpoint = get_cache_endpoint()
r = redis.Redis(host=endpoint)

def getValue(key):
  if isPresent(key):
    return r.get(key).decode("utf-8")
  else:
    return None

def isPresent(key):
  return r.exists(key)

def setValue(key, value):
  r.set(key, value)

def setDict(dict):
  r.mset(dict)