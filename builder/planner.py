class BuilderPlanner:
    """
    Converts a creation specification
    into required construction abilities.
    """



    def plan(
        self,
        creation
    ):


        required = []


        # Main structures

        for structure in creation.structures:

            required.append(
                "structure"
            )


        # Systems

        for system in creation.systems:


            if system in [

                "flying",
                "levitation",
                "magic levitation"

            ]:

                required.append(
                    "levitation"
                )


            if system in [

                "magical",
                "magic",
                "energy fields"

            ]:

                required.append(
                    "magic_effect"
                )



        # Environment

        for environment in creation.environment:


            if environment == "forest":

                required.append(
                    "vegetation"
                )


        return list(
            set(required)
        )