from datetime import datetime
import uuid


class Event:
    """
    Represents something that happened
    inside Caine's universe.

    Examples:

    - player_joined
    - project_completed
    - resident_created
    - adventure_started
    """

    def __init__(
        self,
        event_type: str,
        data=None
    ):

        self.id = str(uuid.uuid4())

        self.event_type = event_type

        self.data = data or {}

        self.created_at = datetime.utcnow()



    def to_dict(self):

        return {

            "id": self.id,

            "type": self.event_type,

            "data": self.data,

            "time": self.created_at.isoformat()

        }



class EventBus:
    """
    Allows systems to communicate.

    Systems subscribe to events
    they care about.

    When an event occurs,
    only those systems are notified.
    """

    def __init__(self):

        self.listeners = {}

        self.history = []



    def subscribe(
        self,
        event_type,
        callback
    ):

        """
        Registers a listener.

        Example:

        subscribe(
            "player_joined",
            welcome_player
        )
        """

        if event_type not in self.listeners:

            self.listeners[event_type] = []


        self.listeners[event_type].append(
            callback
        )



    def unsubscribe(
        self,
        event_type,
        callback
    ):

        if event_type in self.listeners:

            if callback in self.listeners[event_type]:

                self.listeners[event_type].remove(
                    callback
                )



    def emit(
        self,
        event_type,
        data=None
    ):

        """
        Creates and broadcasts
        an event.
        """

        event = Event(
            event_type,
            data
        )


        self.history.append(event)



        listeners = self.listeners.get(
            event_type,
            []
        )


        for callback in listeners:

            callback(event)



        return event



    def get_history(self):

        return [

            event.to_dict()

            for event in self.history

        ]



    def clear_history(self):

        self.history.clear()