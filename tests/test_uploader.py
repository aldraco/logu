import logu
import logu.sockets as sockets
import unittest


class TestParameterizedUploaderAPIFunctions(unittest.TestCase):
    def setUp(self):
        self.parameterized_uploader = logu.GraphiteUploader(host='localhost', port=8080)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()