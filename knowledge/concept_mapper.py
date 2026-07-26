class ConceptMapper:
    """
    Converts extracted information into
    Caine's internal concept format.

    This turns raw detected information into:

    - concepts
    - features
    - materials
    - systems
    - relationships
    """



    def map(
        self,
        extracted
    ):


        if not extracted:

            return None



        concept = {


            "name":
            extracted.get(
                "name",
                ""
            ),


            "category":
            extracted.get(
                "category",
                "unknown"
            ),


            "features":
            [],


            "materials":
            [],


            "systems":
            [],


            "relationships":
            []

        }



        concept["features"].extend(

            extracted.get(
                "features",
                []
            )

        )



        concept["materials"].extend(

            extracted.get(
                "materials",
                []
            )

        )



        concept["systems"].extend(

            extracted.get(
                "systems",
                []
            )

        )



        concept["relationships"].extend(

            extracted.get(
                "relationships",
                []
            )

        )



        self.create_relationships(
            concept
        )


        return concept





    def create_relationships(
        self,
        concept
    ):


        name = concept["name"]



        features = concept["features"]



        if "floating" in features or "flying" in features:


            concept["systems"].append(
                "levitation"
            )


            concept["relationships"].append(

                {

                    "subject":
                    name,


                    "relation":
                    "requires",


                    "object":
                    "levitation system"

                }

            )



        if "magical" in features or "magic" in features:


            concept["systems"].append(
                "magic system"
            )


            concept["relationships"].append(

                {

                    "subject":
                    name,


                    "relation":
                    "powered by",


                    "object":
                    "magic"

                }

            )