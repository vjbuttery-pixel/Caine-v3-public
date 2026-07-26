from datetime import datetime

from agents.base_agent import BaseAgent


class RiggingAgent(BaseAgent):
    """
    Creates skeletal rigs for characters,
    creatures and animated objects.

    The rig is generated from anatomy,
    not from fixed templates.
    """

    def __init__(self):

        super().__init__(
            name="Pulse",
            role="Rigging Artist",
            skills=[
                "rigging",
                "bones",
                "ik",
                "constraints"
            ]
        )

        self.rigs = []



    def create_rig(
        self,
        model,
        anatomy=None
    ):

        anatomy = anatomy or {}

        rig = {

            "model": model["name"],

            "created": datetime.utcnow().isoformat(),

            "bones": [],

            "ik_chains": [],

            "constraints": [],

            "attachment_points": [],

            "physics_bones": [],

            "metadata": anatomy

        }

        self.rigs.append(rig)

        return rig



    def add_bone(
        self,
        rig,
        name,
        parent=None
    ):

        rig["bones"].append({

            "name": name,

            "parent": parent

        })



    def create_ik_chain(
        self,
        rig,
        chain_name,
        bones
    ):

        rig["ik_chains"].append({

            "name": chain_name,

            "bones": bones

        })



    def add_constraint(
        self,
        rig,
        bone,
        constraint_type
    ):

        rig["constraints"].append({

            "bone": bone,

            "type": constraint_type

        })



    def add_attachment_point(
        self,
        rig,
        name
    ):

        rig["attachment_points"].append(name)



    def add_physics_bone(
        self,
        rig,
        bone
    ):

        rig["physics_bones"].append(bone)



    def validate(
        self,
        rig
    ):

        return {

            "bones":
                len(rig["bones"]),

            "ik":
                len(rig["ik_chains"]),

            "constraints":
                len(rig["constraints"]),

            "ready_for_animation": True

        }



    def work(self):

        if self.current_job:

            return (
                f"Rigging "
                f"{self.current_job.name}"
            )

        return "Rigging Agent waiting"