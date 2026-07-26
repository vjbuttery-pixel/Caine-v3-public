class LocalKnowledgeSource:
    """
    Searches Caine's existing knowledge.

    This is the first research source.

    Later this can be replaced or expanded
    with external research tools.
    """



    def __init__(
        self,
        knowledge
    ):

        self.knowledge = knowledge




    def search(
        self,
        query
    ):


        words = query.lower().split()


        results = []


        for word in words:


            found = self.knowledge.search(
                word
            )


            if found:

                results.extend(
                    found
                )


        return results