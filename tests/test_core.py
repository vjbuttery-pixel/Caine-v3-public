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
    print(" CAINE CORE SYSTEM TEST")
    print("==============================\n")


    print("--- Creating Job ---")

    job = Job(
        "Create Castle Walls",
        "Generate the main castle structure",
        "architecture",
        JobPriority.HIGH
    )

    print(job)


    print("\n--- Creating Stage ---")

    stage = Stage(
        "Architecture",
        "Create castle structure"
    )

    stage.add_job(job)

    print(stage)


    print("\n--- Creating Project ---")

    project = Project(
        "Magical Flying Castle",
        "A floating castle above a candy forest"
    )

    project.add_stage(stage)

    project.start()

    print(project)


    print("\n--- Creating Goal ---")

    goal = Goal(
        "Create Resident Home",
        "Build a safe place for residents",
        GoalPriority.HIGH
    )

    goal.add_project(project)

    goal.activate()

    print(goal)


    print("\n--- Creating Systems ---")

    scheduler = Scheduler()

    governor = Governor()

    blackboard = Blackboard()

    events = EventBus()


    scheduler.add_goal(goal)


    cognitive = CognitiveCore(
        blackboard,
        scheduler,
        governor,
        events
    )


    print("\n--- Blackboard Test ---")

    blackboard.set(
        "world",
        "Main Circus"
    )

    print(
        blackboard.get("world")
    )


    print("\n--- Cognitive Cycle ---")

    result = cognitive.execute_cycle()


    print(
        "Selected Job:",
        result
    )


    print("\n==============================")
    print(" CORE TEST COMPLETE")
    print("==============================")


if __name__ == "__main__":

    run_test()