import uuid
from datetime import datetime


class EntityIdentity:
    """
    Permanent identity for anything that exists in Caine's universe.

    This identity never changes.

    Controller, appearance, location and role may change,
    but the entity remains the same.
    """

    def __init__(
        self,
        name: str,
        entity_type: str = "human"
    ):

        self.id = str(uuid.uuid4())

        self.name = name

        self.entity_type = entity_type

        self.created = datetime.utcnow()

        self.active = True


    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "entity_type": self.entity_type,

            "created": self.created.isoformat(),

            "active": self.active

        }


    def __repr__(self):

        return (
            f"<Entity {self.name} "
            f"({self.entity_type}) "
            f"{self.id}>"
        )