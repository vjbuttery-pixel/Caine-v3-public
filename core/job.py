from datetime import datetime
from enum import Enum
import uuid


class JobStatus(Enum):
    """
    Current state of a production job.
    """

    CREATED = "created"

    PLANNING = "planning"

    WAITING = "waiting"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"



class JobPriority(Enum):
    """
    Importance level of a job.
    """

    LOW = 1

    NORMAL = 2

    HIGH = 3

    CRITICAL = 4



class Job:
    """
    The smallest meaningful unit of work Caine can assign.

    Examples:

    - Generate castle mesh
    - Create NPC rig
    - Research dragon anatomy
    - Validate animation
    - Generate particle effect

    Jobs are engine independent.
    """

    def __init__(
        self,
        name: str,
        description: str,
        category: str = "general",
        priority: JobPriority = JobPriority.NORMAL
    ):

        self.id = str(uuid.uuid4())

        self.name = name

        self.description = description

        self.category = category

        self.priority = priority

        self.status = JobStatus.CREATED


        self.created_at = datetime.utcnow()

        self.started_at = None

        self.completed_at = None


        self.assigned_agent = None


        self.dependencies = []

        self.results = None


    def add_dependency(self, job):

        """
        Adds another job that must complete first.
        """

        self.dependencies.append(job.id)



    def can_start(self):

        """
        Checks whether all required jobs are finished.
        """

        for dependency in self.dependencies:

            if dependency.status != JobStatus.COMPLETED:

                return False


        return True



    def start(self, agent_name):

        if not self.can_start():

            return False


        self.status = JobStatus.RUNNING

        self.assigned_agent = agent_name

        self.started_at = datetime.utcnow()

        return True



    def complete(self, result=None):

        self.status = JobStatus.COMPLETED

        self.results = result

        self.completed_at = datetime.utcnow()



    def fail(self, reason):

        self.status = JobStatus.FAILED

        self.results = {

            "error": reason

        }



    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "description": self.description,

            "category": self.category,

            "priority": self.priority.name,

            "status": self.status.value,

            "assigned_agent": self.assigned_agent,

            "dependencies": self.dependencies,

            "results": self.results

        }


    def __repr__(self):

        return (
            f"<Job {self.name} "
            f"| {self.status.value}>"
        )