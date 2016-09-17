import datetime as dt
import itertools

import ancientlogs
import ancientlogs.sockets as sockets
import unittest

class TestDefaultUploaderCreation(unittest.TestCase):
    def setUp(self):
        self.default_uploader = ancientlogs.GraphiteUploader()

    def tearDown(self):
        pass

    def test_default_values(self):
        pass

    def test_data_validation(self):
        # should validate the data structure for graphite, based
        # on the kind of implementation being used
        pass

    def test_default_protocol_is_pickle(self):
        self.assertEqual(self.default_uploader._protocol, "pickle",
            msg="Implement: default protocol is Pickle")

class TestParameterizedUploaderCreation(unittest.TestCase):
    def setUp(self):
        self.parameterized_uploader = ancientlogs.GraphiteUploader(host='localhost', port=8080)

    def tearDown(self):
        pass


class TestDefaultUploaderAPIFunctions(unittest.TestCase):
    def setUp(self):
        self.default_uploader = ancientlogs.GraphiteUploader()

    def test_use_UDP_socket(self):
        u = self.default_uploader
        u.use_UDP_socket()
        self.assertIsInstance(u.socket, sockets.UDPSocket,
            msg="should switch default TCP sock to a UDP socket")
        self.assertIsInstance(u.socket._port, int,
            msg="should correctly create a socket with a port number")

    def test_use_plaintext_protocol(self):
        self.default_uploader.use_plaintext_protocol()
        self.assertEqual(self.default_uploader._protocol, "plaintext",
            msg="Should change the protocol to plaintext")

class TestParameterizedUploaderAPIFunctions(unittest.TestCase):
    def setUp(self):
        self.parameterized_uploader = ancientlogs.GraphiteUploader(host='localhost', port=8080)

    def tearDown(self):
        pass

    def test_use_UDP_socket(self):
        p_u = self.parameterized_uploader
        previousPort = p_u.port
        previousHost = p_u.host
        
        p_u.use_UDP_socket()

        self.assertIsInstance(p_u.socket, sockets.UDPSocket,
            msg="should switch default TCP sock to a UDP socket")
        self.assertEqual(p_u.socket._port, previousPort,
            msg="should preserve the port number from the client")
        self.assertEqual(p_u.socket._host, previousHost,
            msg="should preserve the port number from the client")

if __name__ == "__main__":
    unittest.main()