from knowledge.graph import KnowledgeGraph

from knowledge.bootstrap import load_basic_knowledge

from search.researcher import Researcher



def run_test():


    print("==============================")
    print(" CAINE RESEARCH SYSTEM TEST ")
    print("==============================")



    print(
        "\nCreating knowledge base..."
    )


    knowledge = KnowledgeGraph()



    load_basic_knowledge(
        knowledge
    )



    researcher = Researcher(
        knowledge
    )



    test_analysis = {


        "main_object":
        "castle",



        "modifiers":
        [

            "magical",

            "flying",

            "candy"

        ],



        "environment":
        [

            "forest"

        ],



        "relationships":
        [

            {
                "subject":
                "castle",

                "property":
                "magical"

            },

            {
                "subject":
                "castle",

                "property":
                "flying"

            }

        ]

    }



    print(
        "\n--- STARTING RESEARCH ---"
    )



    result = researcher.research(
        test_analysis
    )



    print(
        "\n--- RESULTS ---"
    )


    for query, data in result.items():


        print(
            "\nQUERY:",
            query
        )


        print(
            data
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