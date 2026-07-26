class KnowledgeLearner:
    """
    Converts discovered information into knowledge.

    The learner does not know specific objects.
    It only understands information patterns.
    """


    def __init__(
        self,
        knowledge_graph
    ):

        self.graph = knowledge_graph




    def learn(
        self,
        information
    ):
        """
        Accepts research information.

        Example:

        {
            "name":"castle",
            "category":"architecture",
            "features":["towers"],
            "materials":["stone"]
        }
        """


        concept_name = information.get(
            "name"
        )


        if not concept_name:

            return False



        category = information.get(
            "category",
            "unknown"
        )



        self.graph.add_concept(

            concept_name,

            category

        )



        self.learn_features(
            concept_name,
            information
        )


        self.learn_materials(
            concept_name,
            information
        )


        self.learn_relationships(
            concept_name,
            information
        )


        return True




    def learn_features(
        self,
        concept,
        information
    ):


        for feature in information.get(
            "features",
            []
        ):


            self.graph.add_feature(

                concept,

                feature

            )




    def learn_materials(
        self,
        concept,
        information
    ):


        for material in information.get(
            "materials",
            []
        ):


            self.graph.add_material(

                concept,

                material

            )




    def learn_relationships(
        self,
        concept,
        information
    ):


        relationships = information.get(
            "relationships",
            []
        )


        for relationship in relationships:


            self.graph.add_relationship(

                concept,

                relationship.get(
                    "relation",
                    "related to"
                ),

                relationship.get(
                    "target"
                )

            )