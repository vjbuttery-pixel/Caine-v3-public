class QueryExpander:
    """
    Turns Caine concepts into meaningful research queries.

    This does not know specific objects.
    It creates relationships between ideas.
    """



    def expand(
        self,
        analysis
    ):


        queries = []


        main = analysis.get(
            "main_object"
        )


        modifiers = analysis.get(
            "modifiers",
            []
        )


        environment = analysis.get(
            "environment",
            []
        )



        # Main object research

        if main:

            queries.append(
                f"{main} definition"
            )

            queries.append(
                f"{main} structure"
            )

            queries.append(
                f"{main} materials"
            )



        # Modifier combinations

        for modifier in modifiers:


            if main:


                queries.append(

                    f"{modifier} {main}"

                )


            queries.append(

                f"{modifier} system"

            )



        # Environment

        for place in environment:


            queries.append(

                f"{place} environment"

            )


            if main:


                queries.append(

                    f"{main} in {place}"

                )



        return self.remove_duplicates(
            queries
        )




    def remove_duplicates(
        self,
        queries
    ):


        result = []


        for query in queries:


            if query not in result:

                result.append(
                    query
                )


        return result