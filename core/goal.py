from datetime import datetime
import uuid


class GoalPriority:
    """
    Importance levels for goals.
    """

    LOW = 1

    NORMAL = 2

    HIGH = 3

    CRITICAL = 4



class GoalStatus:
    """
    Current goal state.
    """

    CREATED = "created"

    ACTIVE = "active"

    PAUSED = "paused"

    COMPLETED = "completed"

    FAILED = "failed"



class Goal:
    """
    Represents something Caine wants to achieve.

    Goals create and control projects.

    Examples:

    - Make residents happier
    - Expand the circus
    - Create a new adventure
    - Repair damaged buildings
    """

    def __init__(
        self,
        name: str,
        description: str,
        priority: int = GoalPriority.NORMAL
    ):

        self.id = str(uuid.uuid4())

        self.name = name

        self.description = description

        self.priority = priority

        self.status = GoalStatus.CREATED


        self.created_at = datetime.utcnow()

        self.completed_at = None


        self.projects = []


        # Future:
        # Who or what caused this goal.
        #
        # Examples:
        # "Caine"
        # "Player Alex"
        # "Resident Luna"
        self.source = None



    def activate(self):

        """
        Makes the goal active.
        """

        self.status = GoalStatus.ACTIVE



    def complete(self):

        """
        Marks the goal as finished.
        """

        self.status = GoalStatus.COMPLETED

        self.completed_at = datetime.utcnow()



    def fail(self):

        """
        Marks the goal as impossible.
        """

        self.status = GoalStatus.FAILED



    def add_project(self, project):

        """
        Connects a project to this goal.
        """

        self.projects.append(project)



    def progress(self):

        """
        Calculates progress from connected projects.
        """

        if len(self.projects) == 0:

            return 0


        total = 0


        for project in self.projects:

            total += project.progress()


        return round(
            total / len(self.projects),
            2
        )



    def is_complete(self):

        """
        Checks if all projects are complete.
        """

        if len(self.projects) == 0:

            return False


        for project in self.projects:

            if project.status != "completed":

                return False


        return True



    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "description": self.description,

            "priority": self.priority,

            "status": self.status,

            "source": self.source,

            "progress": self.progress(),

            "projects": [

                project.id

                for project in self.projects

            ]

        }



    def __repr__(self):

        return (
            f"<Goal {self.name} "
            f"{self.status}>"
        )