class KnowledgeGraph:
    """
    Dynamic knowledge storage.

    Caine does not store objects.
    It stores concepts and relationships.
    """


    def __init__(self):

        self.concepts = {}

        self.relationships = []



    def add_concept(
        self,
        name,
        category="unknown"
    ):


        if name not in self.concepts:

            self.concepts[name] = {

                "name": name,

                "category": category,

                "properties": [],

                "materials": [],

                "features": []

            }


        return self.concepts[name]




    def add_property(
        self,
        concept,
        property_name
    ):


        data = self.add_concept(
            concept
        )


        if property_name not in data["properties"]:

            data["properties"].append(
                property_name
            )




    def add_material(
        self,
        concept,
        material
    ):


        data = self.add_concept(
            concept
        )


        if material not in data["materials"]:

            data["materials"].append(
                material
            )




    def add_feature(
        self,
        concept,
        feature
    ):


        data = self.add_concept(
            concept
        )


        if feature not in data["features"]:

            data["features"].append(
                feature
            )




    def add_relationship(
        self,
        subject,
        relation,
        target
    ):


        relationship = {

            "subject": subject,

            "relation": relation,

            "target": target

        }


        if relationship not in self.relationships:

            self.relationships.append(
                relationship
            )




    def get_concept(
        self,
        name
    ):


        return self.concepts.get(
            name
        )




    def search(
        self,
        keyword
    ):


        results = []


        keyword = keyword.lower()


        for name, data in self.concepts.items():


            if keyword in name.lower():

                results.append(
                    data
                )


        return results




    def describe(self):


        return {

            "concepts":

            self.concepts,


            "relationships":

            self.relationships

        }