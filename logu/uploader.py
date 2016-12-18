import abc
from sockets import TCPSocket
from validators import validate_pickle_protocol
from errors import DataFormattingError

class UploaderBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, host='localhost', port=2003):
        self.host = host
        self.port = port

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cleanup()

    @abc.abstractmethod
    def send(self):
        pass

    @abc.abstractmethod
    def _cleanup(self):
        pass

    def use_port(self, value):
        self.socket.use_port(value)
        self.port = value


class GraphiteUploader(UploaderBase):
    def __init__(self, host="localhost", port=2004):
        super(GraphiteUploader, self).__init__(host=host, port=port)
        self.socket = TCPSocket(host=host, port=port)
        self._validate = validate_pickle_protocol

    def send(self, data):
        try:
            data = self._validate(data)
        except DataFormattingError as e:
            print e
        else:
            self.socket.send(data)

    def _cleanup(self):
        self.socket.close()
