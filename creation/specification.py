class CreationSpecification:
    """
    The final design document created by Caine.

    This is engine independent.
    Blender, Unity, Unreal etc. will read this later.
    """


    def __init__(self, name):

        self.name = name


        # What is being created

        self.category = ""

        self.purpose = ""

        self.description = ""



        # Visual identity

        self.visual_identity = []

        self.shape_language = []

        self.atmosphere = []

        self.colour_palette = []

        self.materials = []



        # Construction

        self.structures = []

        self.environment = []

        self.systems = []



        # Relationships

        self.relationships = []



        # Generation hints

        self.complexity = "medium"

        self.notes = []



    def add_structure(self, structure):

        self.structures.append(
            structure
        )


    def add_system(self, system):

        self.systems.append(
            system
        )


    def describe(self):

        return {

            "name":
            self.name,


            "category":
            self.category,


            "purpose":
            self.purpose,


            "description":
            self.description,


            "visual_identity":
            self.visual_identity,


            "shape_language":
            self.shape_language,


            "atmosphere":
            self.atmosphere,


            "colours":
            self.colour_palette,


            "materials":
            self.materials,


            "structures":
            self.structures,


            "environment":
            self.environment,


            "systems":
            self.systems,


            "relationships":
            self.relationships,


            "complexity":
            self.complexity,


            "notes":
            self.notes

        }