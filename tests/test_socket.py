import datetime as dt
import itertools

import ancientlogs
import ancientlogs.sockets as als

import unittest
import socket

class TestTCPSocket(unittest.TestCase):
    def setUp(self):
        self.default_TCP_socket = als.TCPSocket()
        self.listener = socket.socket()
        self.listener.bind(('localhost', 9000))
        self.listener.listen(1)

    def tearDown(self):
        self.listener.close()

    def test_defaults(self):
        s = self.default_TCP_socket
        self.assertEqual(s._host, 'localhost')
        self.assertEqual(s._port, 9000) 
        self.assertEqual(s._maxsize, 512)
        self.assertEqual(s._connected, False)

    def test_update_max_size(self):
        s = self.default_TCP_socket
        s.update_max_size(1024)
        self.assertEqual(s._maxsize, 1024)

    def test_use_port(self):
        s = self.default_TCP_socket
        s.use_port(12345)
        self.assertEqual(s._port, 12345,
            msg="<socket>.use_port should update the port number")

    def test_connection_maintenance(self):
        s = self.default_TCP_socket
        s.close()
        self.assertEqual(s._connected, False,
            msg="Check for socket closure properly")