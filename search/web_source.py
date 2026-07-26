class WebKnowledgeSource:
    """
    External research source.

    This is an adapter layer.

    Future connections:
    - web APIs
    - search engines
    - databases
    - documents
    """


    def __init__(
        self
    ):

        self.enabled = False




    def search(
        self,
        query
    ):

        """
        Returns researched information.

        Currently disabled until
        external research integration
        is connected.
        """


        if not self.enabled:

            return []



        return []