class Capability:
    """
    Represents one construction capability.

    A capability describes WHAT Caine can do,
    not WHAT object it creates.
    """

    def __init__(
        self,
        name,
        description,
        requirements=None,
        outputs=None
    ):

        self.name = name

        self.description = description

        self.requirements = requirements or []

        self.outputs = outputs or []



    def can_produce(
        self,
        requirement
    ):

        return requirement in self.outputs



    def describe(self):

        return {

            "name": self.name,

            "description": self.description,

            "requirements": self.requirements,

            "outputs": self.outputs

        }