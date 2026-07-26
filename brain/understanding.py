class WorldUnderstanding:
    """
    Caine's first reasoning layer.

    Converts ideas into concepts,
    modifiers and requirements.
    """


    def analyse(self, idea):

        idea = idea.lower()


        result = {

            "original_idea": idea,

            "core_object": None,

            "modifiers": [],

            "environment": [],

            "systems_required": []

        }


        objects = [

            "castle",
            "forest",
            "city",
            "house",
            "library",
            "tower",
            "ship",
            "village"

        ]


        for obj in objects:

            if obj in idea:

                result["core_object"] = obj
                break



        modifiers = {

            "flying":
            "levitation system",


            "magical":
            "magic effects",


            "ancient":
            "weathered materials",


            "dark":
            "dark atmosphere",


            "underwater":
            "water environment",


            "cyber":
            "technology systems"

        }


        for word, system in modifiers.items():

            if word in idea:

                result["modifiers"].append(word)

                result["systems_required"].append(system)



        environments = [

            "forest",
            "ocean",
            "sky",
            "mountain",
            "desert"

        ]


        for environment in environments:

            if environment in idea:

                result["environment"].append(environment)



        return result