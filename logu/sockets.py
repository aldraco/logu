import socket
import pickle
import struct
import abc

class SocketBase(object):
  """
  Using a metaclass to leave room for a UDP socket at a later date.
  """
  __metaclass__ = abc.ABCMeta

  def __init__(self, host="localhost", port=9000):
    self._host = host
    self._port = port
    self._connected = False

  @abc.abstractmethod
  def send(self):
    pass

  @abc.abstractmethod
  def close(self):
    pass

  def use_port(self, new_port):
    if self._connected:
      self._close_connection()
    self._port = new_port



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
    print "Connected to {}:{}".format(self._host, self._port)

  def _close_connection(self):
    self._sock.shutdown(socket.SHUT_RDWR)
    self._sock.close()
    self._connected = False
    print "Connection to {}:{} closed.".format(self._host, self._port)

  def _prepare(self, data):
    payload = pickle.dumps(data, protocol=2)
    header = struct.pack("!L", len(payload))
    message = header + payload
    return message