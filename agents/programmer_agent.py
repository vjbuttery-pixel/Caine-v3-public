from datetime import datetime

from agents.base_agent import BaseAgent


class ProgrammerAgent(BaseAgent):
    """
    Responsible for creating gameplay systems,
    AI logic and engine code.

    This agent creates implementation plans
    first, then code tasks that can later be
    executed by engine-specific generators.
    """

    def __init__(self):

        super().__init__(
            name="Logic",
            role="Programmer",
            skills=[
                "programming",
                "ai",
                "gameplay",
                "ui",
                "networking"
            ]
        )

        self.systems = []



    def create_system(
        self,
        name,
        category
    ):

        system = {

            "name": name,

            "category": category,

            "created": datetime.utcnow().isoformat(),

            "requirements": [],

            "classes": [],

            "events": [],

            "tests": [],

            "status": "planned"

        }

        self.systems.append(system)

        return system



    def add_requirement(
        self,
        system,
        requirement
    ):

        system["requirements"].append(requirement)



    def add_class(
        self,
        system,
        class_name
    ):

        system["classes"].append(class_name)



    def add_event(
        self,
        system,
        event_name
    ):

        system["events"].append(event_name)



    def add_test(
        self,
        system,
        description
    ):

        system["tests"].append(description)



    def mark_complete(
        self,
        system
    ):

        system["status"] = "complete"



    def validate(
        self,
        system
    ):

        return {

            "requirements":
                len(system["requirements"]),

            "classes":
                len(system["classes"]),

            "events":
                len(system["events"]),

            "tests":
                len(system["tests"]),

            "ready_for_qa": True

        }



    def work(self):

        if self.current_job:

            return (
                f"Programming "
                f"{self.current_job.name}"
            )

        return "Programmer Agent waiting"