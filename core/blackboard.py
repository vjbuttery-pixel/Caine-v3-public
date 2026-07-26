from datetime import datetime
import uuid


class Blackboard:
    """
    Shared short-term information system.

    Stores the current situation
    that Caine and its specialists
    need to reason about.

    Examples:

    - Current world state
    - Active projects
    - Important events
    - Current problems
    """

    def __init__(self):

        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()

        self.data = {}

        self.history = []



    def set(self, key, value):

        """
        Stores or updates information.
        """

        old_value = self.data.get(key)


        self.data[key] = value


        self.history.append({

            "key": key,

            "old": old_value,

            "new": value,

            "time": datetime.utcnow().isoformat()

        })



    def get(self, key, default=None):

        """
        Retrieves information.
        """

        return self.data.get(
            key,
            default
        )



    def remove(self, key):

        """
        Removes information.
        """

        if key in self.data:

            del self.data[key]



    def has(self, key):

        """
        Checks if information exists.
        """

        return key in self.data



    def clear(self):

        """
        Clears temporary information.
        """

        self.data.clear()



    def get_all(self):

        """
        Returns current state.
        """

        return self.data



    def get_history(self):

        """
        Returns changes made.
        """

        return self.history



    def snapshot(self):

        """
        Creates a saved snapshot
        of the current situation.
        """

        return {

            "id": self.id,

            "time": datetime.utcnow().isoformat(),

            "data": self.data.copy()

        }



    def restore(self, snapshot):

        """
        Restores a previous state.
        """

        self.data = snapshot.get(
            "data",
            {}
        )



    def __repr__(self):

        return (
            f"<Blackboard "
            f"{len(self.data)} entries>"
        )