import socket
import pickle
import struct
import abc

class SocketBase(object):
  __metaclass__ = abc.ABCMeta

  def __init__(self, host="localhost", port=9000):
    self._host = host
    self._port = port
    self._connected = False
    self._maxsize = 512

  @abc.abstractmethod
  def send(self):
    pass

  def update_max_size(self, newSize):
    self._maxsize = newSize

  def use_port(self, new_port):
    if self._connected:
      self._close_connection()
    self._port = new_port




class UDPSocket(SocketBase):
  def __init__(self, host="localhost", port=9000):
    super(UDPSocket, self).__init__(host=host, port=port)
    # set up socket

  def send(self):
    pass




class TCPSocket(SocketBase):
  def __init__(self, host="localhost", port=9000):
    super(TCPSocket, self).__init__(host=host, port=port)
    self._sock = socket.socket()
    
  def send(self, data):
    if not self._connected:
      self._connect()
    data = self._prepare(data)
    self._sock.send(data)

  def close(self):
    if self._connected:
      self._close_connection()

  def _connect(self):
    self._sock.connect((self._host, self._port))
    self._connected = True

  def _close_connection(self):
    self._sock.shutdown(socket.SHUT_RDWR)
    self._sock.close()
    self._connected = False

  def _prepare(self, data):
    payload = pickle.dumps(data, protocol=2)
    header = struct.pack("!L", len(payload))
    message = header + payload
    return message