import abc
from sockets import UDPSocket, TCPSocket
from validators import validate_pickle_protocol, validate_plaintext_protocol

class UploaderBase(object):
  __metaclass__ = abc.ABCMeta

  def __init__(self, host='localhost', port=2003):
    self.host = host
    self.port = port

  @abc.abstractmethod
  def send(self):
    pass

  @abc.abstractmethod
  def validate_data(self, data):
    pass

  @abc.abstractmethod
  def _cleanup(self):
    pass

  def use_port(self, value):
      self.socket.use_port(value)

  def __enter__(self):
    return self


  def __exit__(self, exc_type, exc_val, exc_tb):
    self._cleanup()
    pass



class GraphiteUploader(UploaderBase):

  def __init__(self, host="localhost", port=2004):
    super(GraphiteUploader, self).__init__(host=host, port=port)
    self.socket = TCPSocket(host=host, port=port)
    self._validate = validate_pickle_protocol

  def send(self, data):
    data = self.validate_data(data)
    self.socket.send(data)

  def validate_data(self, data):
    data = self._validate(data)
    return data

  def use_UDP_socket(self):
    self.socket.close()
    self.socket = UDPSocket(host=self.host, port=self.port)

  def use_plaintext_protocol(self):
    self._validate = validate_plaintext_protocol
    self.use_port(2003)
    # should also change to default port or allow user to say port

  def _cleanup(self):
    self.socket.close()
    pass