class Relationship:
    """
    Connects two concepts together.

    Example:

    castle
      |
      uses
      |
    stone
    """


    def __init__(
        self,
        subject,
        relation,
        target
    ):

        self.subject = subject

        self.relation = relation

        self.target = target



    def describe(self):

        return {

            "subject":
            self.subject,


            "relation":
            self.relation,


            "target":
            self.target

        }