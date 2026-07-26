from artifacts.artifact import Artifact


class ArtifactLibrary:
    """
    Stores every artifact produced
    during one creation.
    """

    def __init__(self):

        self.artifacts = {}



    def add(
        self,
        artifact
    ):

        self.artifacts[
            artifact.name
        ] = artifact



    def get(
        self,
        name
    ):

        return self.artifacts.get(
            name
        )



    def all(
        self
    ):

        return list(
            self.artifacts.values()
        )



    def exists(
        self,
        name
    ):

        return name in self.artifacts



    def describe(
        self
    ):

        return {

            name: artifact.describe()

            for name, artifact

            in self.artifacts.items()

        }