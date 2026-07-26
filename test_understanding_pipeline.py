from brain.idea_parser import IdeaParser
from brain.concept_analyser import ConceptAnalyser

from search.query_expander import QueryExpander



def run_test():


    print("==============================")
    print(" CAINE UNDERSTANDING TEST ")
    print("==============================")



    idea = (
        "a magical flying castle above a candy forest"
    )



    print(
        "\nINPUT:"
    )

    print(
        idea
    )



    # --------------------------
    # PARSING
    # --------------------------


    parser = IdeaParser()



    print(
        "\n--- PARSING IDEA ---"
    )


    concepts = parser.parse(
        idea
    )


    print(
        concepts
    )



    # --------------------------
    # ANALYSIS
    # --------------------------


    analyser = ConceptAnalyser()



    print(
        "\n--- ANALYSING CONCEPTS ---"
    )


    analysis = analyser.analyse(
        concepts
    )


    print(
        analysis
    )



    # --------------------------
    # QUERY EXPANSION
    # --------------------------


    expander = QueryExpander()



    print(
        "\n--- GENERATED RESEARCH QUESTIONS ---"
    )


    queries = expander.expand(
        analysis
    )



    for query in queries:

        print(
            "-",
            query
        )



    print(
        "\n=============================="
    )


    print(
        " TEST COMPLETE "
    )


    print(
        "=============================="
    )




if __name__ == "__main__":

    run_test()