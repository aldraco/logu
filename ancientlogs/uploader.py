import abc
from sockets import UDPSocket, TCPSocket

class UploaderBase(object):
  __metaclass__ = abc.ABCMeta

  def __init__(self, host='localhost', port=2003):
    self._host = host
    self._port = port

  @abc.abstractmethod
  def send(self):
    pass

  @abc.abstractmethod
  def validate_data(self, data):
    pass

  def port():
      doc = "The port property being used by the socket."
      def fget(self):
          return self._port
      def fset(self, value):
          self._port = value
      def fdel(self):
          del self._port
      return locals()
  port = property(**port())

  def host():
      doc = "The host property being written to."
      def fget(self):
          return self._host
      def fset(self, value):
          self._host = value
      def fdel(self):
          del self._host
      return locals()
  host = property(**host())




class GraphiteUploader(UploaderBase):

  def __init__(self, host="localhost", port=2004):
    super(GraphiteUploader, self).__init__(host=host, port=port)
    self.socket = TCPSocket(host=host, port=port)
    self._protocol = "pickle"

  def send(self, data):
    data = self._validate_data(self, data)
    self.socket.send(data)
    self.socket.close()

  def validate_data(self, data):
    return data

  def use_UDP_socket(self):
    self.socket.close()
    self.socket = UDPSocket(host=self._host, port=self._port)

  def use_plaintext_protocol(self):
    self._protocol = "plaintext"
    # should also change to default port or allow user to say port


