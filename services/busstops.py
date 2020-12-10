# Third party imports
from landtransportsg import PublicTransport

# Local app imports
from retrieve_keys import get_lta_key

lta_key = get_lta_key()
client = PublicTransport(lta_key)

def getAll():
  busstop_list = client.bus_stops()
  return busstop_list
