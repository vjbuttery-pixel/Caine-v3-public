from search.query_expander import QueryExpander
from search.local_source import LocalKnowledgeSource



class Researcher:
    """
    Research coordinator.

    Creates searches and collects
    information from sources.
    """



    def __init__(
        self,
        knowledge
    ):


        self.knowledge = knowledge


        self.expander = QueryExpander()


        self.sources = [

            LocalKnowledgeSource(
                knowledge
            )

        ]




    def research(
        self,
        analysis
    ):


        queries = self.expander.expand(
            analysis
        )


        results = {}


        for query in queries:


            results[query] = self.search_sources(
                query
            )



        return results




    def search_sources(
        self,
        query
    ):


        collected = []


        for source in self.sources:


            data = source.search(
                query
            )


            collected.extend(
                data
            )



        return collected