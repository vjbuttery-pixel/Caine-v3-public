import socket

from network.messages import Message


class BridgeClient:

    def __init__(

        self,

        host="127.0.0.1",

        port=5000

    ):

        self.host = host

        self.port = port

        self.socket = socket.socket(

            socket.AF_INET,

            socket.SOCK_STREAM

        )


    def connect(self):

        self.socket.connect(

            (self.host, self.port)

        )


    def send(

        self,

        message

    ):

        self.socket.sendall(

            message.to_json().encode()

        )


    def receive(self):

        data = self.socket.recv(

            8192

        )

        return Message.from_json(

            data.decode()

        )