import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from core.job import Job, JobPriority
from core.stage import Stage
from core.project import Project
from core.goal import Goal, GoalPriority
from core.scheduler import Scheduler
from core.governor import Governor
from core.blackboard import Blackboard
from core.event_bus import EventBus
from core.cognitive_core import CognitiveCore


def run_test():

    print("==============================")
    print(" CAINE CREATION PIPELINE TEST")
    print("==============================\n")


    project = Project(
        "Candy Forest Castle",
        "A magical flying castle above a candy forest"
    )


    architecture = Stage(
        "Architecture",
        "Build castle structure"
    )


    magic = Stage(
        "Magic",
        "Add magical systems"
    )


    architecture_job = Job(
        "Generate Castle",
        "Create castle geometry",
        "model",
        JobPriority.HIGH
    )


    magic_job = Job(
        "Create Flying System",
        "Make castle float",
        "vfx",
        JobPriority.NORMAL
    )


    architecture.add_job(
        architecture_job
    )

    magic.add_job(
        magic_job
    )


    project.add_stage(
        architecture
    )

    project.add_stage(
        magic
    )


    goal = Goal(
        "Create Fantasy World",
        "Build a complete magical environment"
    )


    goal.add_project(
        project
    )


    print("Project:")
    print(project.name)


    print("\nInitial Progress:")

    print(
        project.progress(),
        "%"
    )


    print("\nCompleting architecture job...")

    architecture_job.complete(
        "Castle mesh created"
    )


    print(
        "Architecture:",
        architecture.progress(),
        "%"
    )


    print(
        "Project:",
        project.progress(),
        "%"
    )


    print("\n==============================")
    print(" PIPELINE TEST COMPLETE")
    print("==============================")


if __name__ == "__main__":

    run_test()