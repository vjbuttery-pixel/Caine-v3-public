class SearchQueryBuilder:
    """
    Converts Caine's understanding into meaningful searches.
    """


    def build(
        self,
        analysis
    ):


        queries = []


        main = analysis.get(
            "core_object"
        )


        modifiers = analysis.get(
            "modifiers",
            []
        )


        environment = analysis.get(
            "environment",
            []
        )


        if main:

            queries.append(
                main
            )


        for modifier in modifiers:

            queries.append(

                f"{modifier} {main}"

            )



        for item in environment:

            queries.append(

                f"{main} in {item}"

            )


        return queries