import socket
import threading

from network.messages import Message


class BridgeServer:

    def __init__(

        self,

        host="127.0.0.1",

        port=5000

    ):

        self.host = host

        self.port = port

        self.server = None

        self.client = None



    def start(self):

        self.server = socket.socket(

            socket.AF_INET,

            socket.SOCK_STREAM

        )

        self.server.bind(

            (self.host, self.port)

        )

        self.server.listen(1)

        print(

            "Waiting for Unity..."

        )

        self.client, address = (

            self.server.accept()

        )

        print(

            f"Unity connected: {address}"

        )



    def send(

        self,

        message

    ):

        self.client.sendall(

            message.to_json().encode()

        )



    def receive(self):

        data = self.client.recv(

            8192

        )

        return Message.from_json(

            data.decode()

        )