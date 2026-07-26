import threading
import time

from network.bridge_server import BridgeServer
from network.bridge_client import BridgeClient
from network.messages import Message


def server():

    server = BridgeServer()

    server.start()

    msg = server.receive()

    print(

        "SERVER RECEIVED:",

        msg.payload

    )


def client():

    time.sleep(1)

    client = BridgeClient()

    client.connect()

    client.send(

        Message(

            "SpawnPrefab",

            {

                "prefab":

                "CentralTent"

            }

        )

    )


threading.Thread(

    target=server

).start()

threading.Thread(

    target=client

).start()