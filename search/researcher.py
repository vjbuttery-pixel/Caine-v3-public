from search.query_expander import QueryExpander
from search.local_source import LocalKnowledgeSource
from search.web_source import WebKnowledgeSource

from knowledge.extractor import InformationExtractor
from knowledge.concept_mapper import ConceptMapper



class Researcher:
    """
    Controls Caine's research pipeline.

    Flow:

    Idea analysis
        |
        v
    Query expansion
        |
        v
    Research sources
        |
        v
    Information extraction
        |
        v
    Concept mapping
        |
        v
    Structured knowledge
    """



    def __init__(
        self,
        knowledge
    ):


        self.knowledge = knowledge


        self.expander = QueryExpander()


        self.extractor = InformationExtractor()


        self.mapper = ConceptMapper()



        self.sources = [

            LocalKnowledgeSource(
                knowledge
            ),


            WebKnowledgeSource()

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


            print(
                "Researching:",
                query
            )


            raw_results = self.search_sources(
                query
            )


            structured_results = []



            for item in raw_results:


                extracted = self.extractor.extract(
                    item
                )


                if extracted:


                    mapped = self.mapper.map(
                        extracted
                    )


                    if mapped:

                        structured_results.append(
                            mapped
                        )



            results[query] = structured_results



        return results





    def search_sources(
        self,
        query
    ):


        collected = []



        for source in self.sources:


            try:


                result = source.search(
                    query
                )


                if result:


                    collected.extend(
                        result
                    )



            except Exception as error:


                print(
                    "Research source error:",
                    error
                )



        return collected