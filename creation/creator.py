from creation.specification import CreationSpecification



class CreationCreator:
    """
    Converts Caine's understanding into a design.
    """


    def create(
        self,
        idea,
        analysis,
        knowledge
    ):


        creation = CreationSpecification(
            analysis["main_object"]
        )


        creation.category = "generated creation"



        creation.description = idea



        # Main object

        creation.add_structure(

            analysis["main_object"]

        )



        # Modifiers become systems

        for modifier in analysis["modifiers"]:

            creation.add_system(

                modifier

            )



        # Environment

        creation.environment = (

            analysis["environment"]

        )



        # Pull visual information

        for concept, data in knowledge.items():


            if "materials" in data:

                creation.materials.extend(

                    data["materials"]

                )



            if "features" in data:

                creation.visual_identity.extend(

                    data["features"]

                )


            if "effects" in data:

                creation.visual_identity.extend(

                    data["effects"]

                )



            if "methods" in data:

                creation.systems.extend(

                    data["methods"]

                )



            if "colours" in data:

                creation.colour_palette.extend(

                    data["colours"]

                )



        creation.relationships = (

            analysis["relationships"]

        )



        return creation