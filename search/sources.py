class ResearchSource:
    """
    Base class for knowledge sources.

    Future versions can connect:
    - web search
    - documents
    - APIs
    - databases
    """


    def search(
        self,
        query
    ):

        raise NotImplementedError