from datetime import datetime
import uuid

from core.stage import Stage


class ProjectStatus:

    PLANNING = "planning"

    ACTIVE = "active"

    PAUSED = "paused"

    COMPLETED = "completed"

    FAILED = "failed"



class Project:
    """
    Represents a complete creation Caine is working on.

    Examples:

    - Magical Flying Castle
    - Multiplayer Adventure World
    - Player Avatar
    - NPC Character

    Projects contain stages,
    which contain jobs.
    """

    def __init__(
        self,
        name: str,
        description: str
    ):

        self.id = str(uuid.uuid4())

        self.name = name

        self.description = description

        self.status = ProjectStatus.PLANNING


        self.created_at = datetime.utcnow()

        self.started_at = None

        self.completed_at = None


        self.stages = []


        # Future system:
        # Stores the design document
        # that all specialists use.
        self.blueprint = None


        # Final outputs:
        # Models, worlds, scripts,
        # animations, etc.
        self.artifacts = []



    def add_stage(self, stage: Stage):

        """
        Adds a production stage.
        """

        self.stages.append(stage)



    def start(self):

        """
        Begins production.
        """

        self.status = ProjectStatus.ACTIVE

        self.started_at = datetime.utcnow()



    def pause(self):

        """
        Temporarily stops production.
        """

        self.status = ProjectStatus.PAUSED



    def progress(self):

        """
        Calculates overall project progress.
        """

        if len(self.stages) == 0:

            return 0


        total = 0


        for stage in self.stages:

            total += stage.progress()


        return round(
            total / len(self.stages),
            2
        )



    def check_completion(self):

        """
        Determines whether the entire
        project has finished.
        """

        if len(self.stages) == 0:

            return False


        for stage in self.stages:

            if not stage.is_complete():

                return False


        self.status = ProjectStatus.COMPLETED

        self.completed_at = datetime.utcnow()

        return True



    def add_artifact(self, artifact):

        """
        Adds a completed creation.

        Examples:

        - Blender file
        - Texture
        - Animation
        - World save
        """

        self.artifacts.append(artifact)



    def get_active_jobs(self):

        """
        Finds all jobs currently available.
        """

        jobs = []


        for stage in self.stages:

            jobs.extend(
                stage.get_available_jobs()
            )


        return jobs



    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "description": self.description,

            "status": self.status,

            "progress": self.progress(),

            "blueprint": self.blueprint,

            "artifacts": self.artifacts,

            "stages": [

                stage.to_dict()

                for stage in self.stages

            ]

        }



    def __repr__(self):

        return (
            f"<Project {self.name} "
            f"{self.progress()}%>"
        )