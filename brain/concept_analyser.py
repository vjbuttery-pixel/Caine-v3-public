class ConceptAnalyser:
    """
    Understands the meaning of Caine's parsed idea.

    Separates:
    - main creation
    - modifiers
    - environment
    - relationships
    """


    def analyse(self, concepts):

        result = {

            "main_object": None,

            "modifiers": [],

            "environment": [],

            "relationships": []

        }


        # ----------------------------
        # Main object
        # ----------------------------

        result["main_object"] = concepts.get(
            "core_object"
        )


        # ----------------------------
        # Modifiers
        # ----------------------------

        result["modifiers"] = concepts.get(
            "modifiers",
            []
        )


        # ----------------------------
        # Environment
        # ----------------------------

        result["environment"] = concepts.get(
            "environment",
            []
        )


        # ----------------------------
        # Relationships
        # ----------------------------

        result["relationships"] = concepts.get(
            "relationships",
            []
        )


        return result