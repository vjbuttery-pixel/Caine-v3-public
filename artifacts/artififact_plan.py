from artifacts.artifact import Artifact


class ArtifactPlan:
    """
    A complete production plan.

    Example:

    Castle

        Mesh

        Rig

        Materials

        Particles

        Animation

        Scripts
    """

    def __init__(self):

        self.artifacts = []



    def add(
        self,
        artifact
    ):

        self.artifacts.append(
            artifact
        )



    def all(
        self
    ):

        return self.artifacts



    def describe(
        self
    ):

        return [

            artifact.describe()

            for artifact

            in self.artifacts

        ]