from datetime import datetime
import uuid

from core.job import Job, JobStatus


class Stage:
    """
    A major section of a project.

    Stages contain jobs and represent
    meaningful milestones.

    Examples:

    - Architecture
    - Animation
    - VFX
    - Audio
    - Testing
    """

    def __init__(
        self,
        name: str,
        description: str
    ):

        self.id = str(uuid.uuid4())

        self.name = name

        self.description = description

        self.jobs = []

        self.created_at = datetime.utcnow()

        self.completed = False



    def add_job(self, job: Job):

        """
        Adds a production job
        to this stage.
        """

        self.jobs.append(job)



    def progress(self):

        """
        Returns completion percentage.
        """

        if len(self.jobs) == 0:

            return 0


        completed = 0


        for job in self.jobs:

            if job.status == JobStatus.COMPLETED:

                completed += 1


        return round(
            (completed / len(self.jobs)) * 100,
            2
        )



    def is_complete(self):

        """
        Checks whether every job
        in the stage is complete.
        """

        if len(self.jobs) == 0:

            return False


        for job in self.jobs:

            if job.status != JobStatus.COMPLETED:

                return False


        self.completed = True

        return True



    def get_available_jobs(self):

        """
        Returns jobs that are ready
        to be worked on.
        """

        available = []


        for job in self.jobs:

            if (
                job.status == JobStatus.CREATED
                and job.can_start()
            ):

                available.append(job)


        return available



    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "description": self.description,

            "progress": self.progress(),

            "completed": self.completed,

            "jobs": [

                job.to_dict()

                for job in self.jobs

            ]

        }



    def __repr__(self):

        return (
            f"<Stage {self.name} "
            f"{self.progress()}%>"
        )