from datetime import datetime

from agents.base_agent import BaseAgent


class ArchitectAgent(BaseAgent):
    """
    Designs layouts and structures.

    The Architect does not create meshes.

    Instead it produces construction plans
    that other agents build from.
    """

    def __init__(self):

        super().__init__(
            name="Atlas",
            role="Architect",
            skills=[
                "architecture",
                "layout",
                "building",
                "navigation",
                "planning"
            ]
        )

        self.designs = []



    def design_project(
        self,
        project,
        zone_type="adventure"
    ):
        """
        Produces a high-level architectural
        design for a project.
        """

        design = {

            "project": project.name,

            "zone_type": zone_type,

            "created": datetime.utcnow().isoformat(),

            "rooms": [],

            "paths": [],

            "landmarks": [],

            "notes": []

        }

        if zone_type == "main_circus":

            design["notes"].extend([

                "Permanent structures only",

                "No destructive world events",

                "Comfortable resident housing",

                "Future expansion supported"

            ])

        else:

            design["notes"].extend([

                "Dynamic environment",

                "Story driven",

                "Weather permitted",

                "Terrain evolution allowed"

            ])

        self.designs.append(design)

        return design



    def add_room(
        self,
        design,
        name,
        purpose
    ):

        design["rooms"].append({

            "name": name,

            "purpose": purpose

        })



    def connect_rooms(
        self,
        design,
        room_a,
        room_b
    ):

        design["paths"].append({

            "from": room_a,

            "to": room_b

        })



    def add_landmark(
        self,
        design,
        name
    ):

        design["landmarks"].append(name)



    def review_layout(
        self,
        design
    ):

        return {

            "rooms":
                len(design["rooms"]),

            "paths":
                len(design["paths"]),

            "landmarks":
                len(design["landmarks"]),

            "approved": True

        }



    def work(self):

        if self.current_job:

            return (
                f"Designing architecture for "
                f"{self.current_job.name}"
            )

        return "Architect waiting for assignment"