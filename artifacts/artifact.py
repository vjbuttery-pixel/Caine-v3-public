from dataclasses import dataclass, field


@dataclass
class Artifact:
    """
    Represents anything Caine creates.

    Examples:

    - Mesh
    - Rig
    - Animation
    - Material
    - Texture
    - Particle System
    - Behaviour Tree
    - Script
    - Sound
    - UI
    """

    name: str

    artifact_type: str

    description: str = ""

    requirements: list = field(default_factory=list)

    dependencies: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    completed: bool = False


    def add_requirement(
        self,
        requirement
    ):

        self.requirements.append(
            requirement
        )


    def add_dependency(
        self,
        dependency
    ):

        self.dependencies.append(
            dependency
        )


    def mark_complete(
        self
    ):

        self.completed = True


    def describe(
        self
    ):

        return {

            "name": self.name,

            "type": self.artifact_type,

            "description": self.description,

            "requirements": self.requirements,

            "dependencies": self.dependencies,

            "completed": self.completed

        }