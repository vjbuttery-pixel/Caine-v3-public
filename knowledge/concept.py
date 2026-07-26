class Concept:
    """
    Represents a piece of knowledge.

    Concepts are connected together
    through relationships.
    """


    def __init__(
        self,
        name,
        category
    ):

        self.name = name

        self.category = category

        self.features = []

        self.materials = []

        self.relationships = []



    def add_feature(
        self,
        feature
    ):

        if feature not in self.features:

            self.features.append(
                feature
            )



    def add_material(
        self,
        material
    ):

        if material not in self.materials:

            self.materials.append(
                material
            )



    def add_relationship(
        self,
        relationship
    ):

        self.relationships.append(
            relationship
        )



    def describe(self):

        return {

            "name":
            self.name,


            "category":
            self.category,


            "features":
            self.features,


            "materials":
            self.materials,


            "relationships":
            self.relationships

        }