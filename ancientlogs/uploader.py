import abc
import sockets

class UploaderBase(object):

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def send(self):
    pass


class GraphiteUploader(UploaderBase):

  def __init__(self, host="localhost", port=2004, maxsize=512):
    self._host = host
    self._port = port
    self._maxsize = maxsize
    self._sock = sockets.UDPSocket(host=self._host, port=self._port, maxsize=self._maxsize)

  def send(self, data):
    self._sock.send(data)
    self._sock.close()
