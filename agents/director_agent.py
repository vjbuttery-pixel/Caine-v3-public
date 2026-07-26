from datetime import datetime
import uuid

from agents.base_agent import BaseAgent



class DirectorAgent(BaseAgent):
    """
    Creative director agent.

    Responsible for planning,
    coordinating and monitoring
    large creations.

    Does not directly create assets.
    """


    def __init__(self):

        super().__init__(
            name="Caine Director",
            role="Director",
            skills=[
                "planning",
                "coordination",
                "management"
            ]
        )


        self.projects_managed = []

        self.reports = []



    def create_plan(self, project):
        """
        Creates a production structure
        for a project.
        """

        plan = {

            "project":
                project.name,

            "stages":[

                "Planning",

                "Design",

                "Creation",

                "Integration",

                "Testing",

                "Polish"

            ],

            "created":
                datetime.utcnow().isoformat()

        }


        project.blueprint = plan


        self.projects_managed.append(
            project
        )


        return plan



    def analyse_project(self, project):
        """
        Reviews project progress.
        """

        report = {

            "project":
                project.name,

            "progress":
                project.progress(),

            "status":
                project.status,

            "time":
                datetime.utcnow().isoformat()

        }


        self.reports.append(
            report
        )


        return report



    def assign_production_tasks(
        self,
        project
    ):
        """
        Converts project stages
        into production requirements.

        Later this will create
        actual jobs.
        """


        tasks = []


        for stage in project.stages:

            tasks.append({

                "stage":
                    stage.name,

                "required":
                    "specialist agent"

            })


        return tasks



    def review_creation(
        self,
        result
    ):
        """
        Performs creative review.

        Later this will include:

        - quality checks
        - style matching
        - design consistency
        """

        return {

            "approved": True,

            "notes":
                "Creation matches current design."

        }



    def work(self):

        if self.current_job:

            return (
                "Directing production of "
                f"{self.current_job.name}"
            )


        return (
            "Director waiting for projects"
        )