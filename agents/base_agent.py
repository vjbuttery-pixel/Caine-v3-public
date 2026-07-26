from datetime import datetime
import uuid


class AgentStatus:

    IDLE = "idle"

    WORKING = "working"

    COMPLETED = "completed"

    FAILED = "failed"



class BaseAgent:
    """
    Base class for every Caine worker.

    All specialist agents inherit from this.

    Examples:

    - ArchitectAgent
    - ModelAgent
    - AnimationAgent
    - VFXAgent
    - AudioAgent
    - ProgrammerAgent
    """

    def __init__(
        self,
        name: str,
        role: str,
        skills=None
    ):

        self.id = str(uuid.uuid4())

        self.name = name

        self.role = role


        self.skills = skills or []


        self.status = AgentStatus.IDLE


        self.current_job = None


        self.completed_jobs = []


        self.created_at = datetime.utcnow()



    def has_skill(self, skill):

        """
        Checks whether this agent
        can perform a type of work.
        """

        return skill in self.skills



    def assign_job(self, job):

        """
        Gives this agent a job.
        """

        if self.status != AgentStatus.IDLE:

            return False


        self.current_job = job

        self.status = AgentStatus.WORKING


        job.start(
            self.name
        )


        return True



    def complete_job(
        self,
        result=None
    ):

        """
        Finishes current work.
        """

        if self.current_job is None:

            return False


        self.current_job.complete(
            result
        )


        self.completed_jobs.append(
            self.current_job
        )


        self.current_job = None

        self.status = AgentStatus.IDLE


        return True



    def fail_job(
        self,
        reason
    ):

        if self.current_job is None:

            return False


        self.current_job.fail(
            reason
        )


        self.current_job = None

        self.status = AgentStatus.IDLE


        return True



    def work(self):

        """
        Main worker function.

        Specialist agents override this.

        Example:

        ModelAgent.work()
        creates geometry.

        AnimatorAgent.work()
        creates animations.
        """

        if self.current_job:

            return (
                f"{self.name} "
                "working on "
                f"{self.current_job.name}"
            )


        return (
            f"{self.name} "
            "has no job"
        )



    def get_status(self):

        return {

            "name": self.name,

            "role": self.role,

            "status": self.status,

            "skills": self.skills,

            "current_job":
                self.current_job.name
                if self.current_job
                else None

        }



    def __repr__(self):

        return (
            f"<Agent {self.name} "
            f"| {self.role}>"
        )