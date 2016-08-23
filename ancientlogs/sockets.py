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
    print "Making another instance"
    self._sock = socket.socket()
    self._host = host
    self._port = port
    self._connected = False

  def _connect(self):
    self._sock.connect((self._host, self._port))
    self._connected = True

  def _close_connection(self):
    # TODO shutdown
    self._sock.close()

  def send(self, data):
    if self._connected:
      self._sock.sendall(data)
      self._close_connection()


