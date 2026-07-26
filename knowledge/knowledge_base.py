from knowledge.concept import Concept
from knowledge.relationship import Relationship



class KnowledgeBase:
    """
    Caine's long term understanding.

    Stores concepts and connections.
    """



    def __init__(self):

        self.concepts = {}

        self.relationships = []

        self.load_defaults()



    def add_concept(
        self,
        concept
    ):

        self.concepts[
            concept.name
        ] = concept



    def get(
        self,
        name
    ):

        return self.concepts.get(
            name.lower()
        )



    def add_relationship(
        self,
        subject,
        relation,
        target
    ):

        connection = Relationship(

            subject,

            relation,

            target

        )


        self.relationships.append(
            connection
        )



    def load_defaults(self):


        # -------------------------
        # ARCHITECTURE
        # -------------------------

        castle = Concept(
            "castle",
            "architecture"
        )

        castle.add_feature(
            "towers"
        )

        castle.add_feature(
            "walls"
        )

        castle.add_feature(
            "rooms"
        )

        castle.add_feature(
            "gate"
        )

        castle.add_material(
            "stone"
        )

        castle.add_material(
            "wood"
        )

        self.add_concept(
            castle
        )



        # -------------------------
        # MAGIC SYSTEM
        # -------------------------

        magic = Concept(
            "magic",
            "fantasy_system"
        )

        magic.add_feature(
            "energy"
        )

        magic.add_feature(
            "symbols"
        )

        magic.add_feature(
            "particles"
        )

        magic.add_material(
            "crystal"
        )

        self.add_concept(
            magic
        )



        # -------------------------
        # FLIGHT / LEVITATION
        # -------------------------

        flying = Concept(
            "flying",
            "movement_system"
        )

        flying.add_feature(
            "levitation"
        )

        flying.add_feature(
            "air movement"
        )

        flying.add_feature(
            "floating"
        )

        self.add_concept(
            flying
        )



        # -------------------------
        # CANDY THEME
        # -------------------------

        candy = Concept(
            "candy",
            "material_style"
        )

        candy.add_feature(
            "colourful"
        )

        candy.add_feature(
            "sweet architecture"
        )

        candy.add_material(
            "sugar"
        )

        candy.add_material(
            "chocolate"
        )

        candy.add_material(
            "caramel"
        )

        self.add_concept(
            candy
        )



        # -------------------------
        # ENVIRONMENT
        # -------------------------

        forest = Concept(
            "forest",
            "environment"
        )

        forest.add_feature(
            "trees"
        )

        forest.add_feature(
            "plants"
        )

        forest.add_feature(
            "terrain"
        )

        self.add_concept(
            forest
        )



        # -------------------------
        # RELATIONSHIPS
        # -------------------------


        self.add_relationship(

            "castle",

            "can use",

            "magic"

        )


        self.add_relationship(

            "castle",

            "can have",

            "flying"

        )


        self.add_relationship(

            "castle",

            "can use style",

            "candy"

        )


        self.add_relationship(

            "castle",

            "can exist in",

            "forest"

        )


    def search(
        self,
        concept
    ):


        result = self.get(
            concept
        )


        if result:

            return result.describe()


        return None