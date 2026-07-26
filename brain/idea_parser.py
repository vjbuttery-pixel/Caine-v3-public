class IdeaParser:
    """
    Extracts the conceptual structure of an idea.

    This is not a generator.
    It identifies:
    - what the thing is
    - what modifies it
    - where it exists
    """


    def parse(
        self,
        idea
    ):

        words = idea.lower().split()


        result = {

            "original_idea": idea,

            "core_object": None,

            "modifiers": [],

            "environment": [],

            "relationships": []

        }


        objects = [
            "castle",
            "house",
            "tower",
            "city",
            "forest",
            "ship",
            "island",
            "planet",
            "village",
            "building"
        ]


        modifiers = [
            "magical",
            "flying",
            "ancient",
            "giant",
            "tiny",
            "dark",
            "crystal",
            "candy",
            "floating"
        ]


        environments = [
            "forest",
            "ocean",
            "desert",
            "mountain",
            "sky",
            "space"
        ]



        # Find main object first

        for word in words:

            if word in objects:

                result["core_object"] = word

                break



        # Find modifiers

        for word in words:

            if word in modifiers:

                result["modifiers"].append(
                    word
                )



        # Find environments

        for word in words:

            if word in environments:

                if word != result["core_object"]:

                    result["environment"].append(
                        word
                    )



        # Create relationships

        if result["core_object"]:

            for modifier in result["modifiers"]:

                result["relationships"].append(
                    {
                        "subject":
                        result["core_object"],

                        "property":
                        modifier
                    }
                )


        return result