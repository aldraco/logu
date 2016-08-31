import socket
import pickle
import struct
import abc

class SocketBase(object):
  """Abstract base class for various kinds of socket connections"""
  
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def send(self):
    pass



class UDPSocket(SocketBase):
  """basic UDP socket to send and forget"""

  def __init__(self, host="localhost", port=None, maxsize=512):
    self._sock = socket.socket()
    self._host = host
    self._port = port
    self._connected = False

  def _connect(self):
    self._sock.connect((self._host, self._port))
    self._connected = True

  def _close_connection(self):
    self._sock.shutdown(socket.SHUT_RDWR)
    self._sock.close()

  def _prepare(self, data):
    payload = pickle.dumps(data, protocol=2)
    header = struct.pack("!L", len(payload))
    message = header + payload
    return message

  def send(self, data):
    if not self._connected:
      self._connect()
    data = self._prepare(data)
    self._sock.send(data)

  def close(self):
    self._close_connection()


