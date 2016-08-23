import config

class Uploader(object):
  """Takes cues from config file and attaches the right bits to do the job."""

  def __init__(self, uploader_name, **kwargs):
    loader_config = config.make_config(uploader_name=uploader_name, options=kwargs)
    
    self._sock = loader_config['socket']
    self._validate = loader_config['validator']


  def upload(self, data):
    validated = self._validate(data)
    if validated:
      prepared = self._prepare(validated)
      self._send_data(prepared)

  def _send_data(self, prepared_data):
    """Use the unique socket to send the data"""
    self._sock.send(prepared_data)
