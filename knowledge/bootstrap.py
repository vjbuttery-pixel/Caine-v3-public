def load_basic_knowledge(
    graph
):
    """
    Gives Caine basic concepts.

    This is foundational knowledge,
    not a database of objects.
    """



    graph.add_concept(
        "object",
        "general"
    )


    graph.add_concept(
        "material",
        "general"
    )


    graph.add_concept(
        "environment",
        "general"
    )


    graph.add_concept(
        "structure",
        "general"
    )


    graph.add_concept(
        "system",
        "general"
    )



    graph.add_relationship(

        "structure",

        "made from",

        "material"

    )


    graph.add_relationship(

        "object",

        "exists in",

        "environment"

    )


    graph.add_relationship(

        "system",

        "changes",

        "object"

    )