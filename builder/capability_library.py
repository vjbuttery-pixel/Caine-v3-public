from builder.capability import Capability


class CapabilityLibrary:
    """
    Stores every capability Caine possesses.
    """

    def __init__(self):

        self.capabilities = {}



    def register(
        self,
        capability
    ):

        self.capabilities[
            capability.name
        ] = capability



    def find_capabilities(
        self,
        required_outputs
    ):

        matches = []

        for capability in self.capabilities.values():

            if any(
                output in capability.outputs
                for output in required_outputs
            ):

                matches.append(
                    capability
                )

        return matches



    def all_capabilities(self):

        return list(
            self.capabilities.values()
        )