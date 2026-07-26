class CapabilityRegistry:
    """
    Stores creation abilities available to Caine.

    This does not contain objects like:
    castle_generator.py

    It contains abilities like:
    - structure creation
    - terrain creation
    - material creation
    - effects creation
    """


    def __init__(self):

        self.capabilities = {}



    def register(
        self,
        name,
        abilities,
        system
    ):

        self.capabilities[name] = {

            "abilities": set(abilities),

            "system": system

        }



    def find_capable_systems(
        self,
        requirements
    ):

        results = []

        required = set(requirements)


        for name, data in self.capabilities.items():

            available = data["abilities"]


            matches = required.intersection(
                available
            )


            if matches:

                results.append(
                    {
                        "name": name,

                        "matched": list(matches),

                        "missing": list(
                            required - available
                        ),

                        "system": data["system"]

                    }
                )


        results.sort(
            key=lambda item:
            len(item["matched"]),
            reverse=True
        )


        return results