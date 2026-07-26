import json


class Message:

    def __init__(self, message_type, payload):

        self.message_type = message_type

        self.payload = payload


    def to_json(self):

        return json.dumps({

            "type": self.message_type,

            "payload": self.payload

        })


    @staticmethod
    def from_json(data):

        obj = json.loads(data)

        return Message(

            obj["type"],

            obj["payload"]

        )