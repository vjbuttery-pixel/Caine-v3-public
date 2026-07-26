from datetime import datetime

from agents.base_agent import BaseAgent


class AnimationAgent(BaseAgent):
    """
    Creates animation plans and motion
    definitions for characters and
    animated objects.

    The goal is to generate animation
    from intent rather than relying on
    a fixed animation library.
    """

    def __init__(self):

        super().__init__(
            name="Echo",
            role="Animation Artist",
            skills=[
                "animation",
                "motion",
                "facial_animation",
                "cinematics"
            ]
        )

        self.animation_sets = []



    def create_animation_set(
        self,
        rig,
        character_name
    ):

        animation_set = {

            "character": character_name,

            "rig": rig["model"],

            "created": datetime.utcnow().isoformat(),

            "animations": [],

            "facial": [],

            "transitions": [],

            "metadata": {}

        }

        self.animation_sets.append(
            animation_set
        )

        return animation_set



    def add_animation(
        self,
        animation_set,
        name,
        purpose,
        emotion="neutral"
    ):

        animation_set["animations"].append({

            "name": name,

            "purpose": purpose,

            "emotion": emotion

        })



    def add_facial_expression(
        self,
        animation_set,
        name
    ):

        animation_set["facial"].append(
            name
        )



    def add_transition(
        self,
        animation_set,
        start,
        end
    ):

        animation_set["transitions"].append({

            "from": start,

            "to": end

        })



    def build_motion_profile(
        self,
        personality=None,
        emotion="neutral",
        movement_style="natural"
    ):

        personality = personality or {}

        return {

            "emotion": emotion,

            "movement_style": movement_style,

            "personality": personality

        }



    def validate(
        self,
        animation_set
    ):

        return {

            "animations":
                len(animation_set["animations"]),

            "facial":
                len(animation_set["facial"]),

            "transitions":
                len(animation_set["transitions"]),

            "ready_for_runtime": True

        }



    def work(self):

        if self.current_job:

            return (
                f"Animating "
                f"{self.current_job.name}"
            )

        return "Animation Agent waiting"