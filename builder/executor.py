class BuilderExecutor:
    """
    Executes a construction plan.

    The executor does not know specific objects.
    It only applies capabilities.
    """


    def __init__(
        self,
        capability_library
    ):

        self.library = capability_library



    def execute(
        self,
        creation,
        plan
    ):

        result = {

            "name": creation.name,

            "components": []

        }



        for capability_name in plan:


            capability = self.library.get(

                capability_name

            )


            if capability is None:

                continue



            component = self.apply_capability(

                capability,

                creation

            )


            result["components"].append(

                component

            )



        return result




    def apply_capability(
        self,
        capability,
        creation
    ):


        return {

            "capability":

            capability.name,


            "category":

            capability.category,


            "description":

            capability.description,


            "target":

            creation.name

        }