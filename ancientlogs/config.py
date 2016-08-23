import sockets

def test_validator(data):
  return len(data) > 0

master_config = {
  "graphite": {
    "socket": sockets.UDPSocket,
    "validator": test_validator
  }
}

def make_config(uploader_name, options={}):
  """Return a smart config object"""
  config = master_config[uploader_name]
 
  # now initialize the socket
  config['socket'] = config['socket'](host=options.get('host'), port=options.get('port'))

  return config
