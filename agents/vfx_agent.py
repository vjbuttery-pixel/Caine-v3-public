from datetime import datetime

from agents.base_agent import BaseAgent


class VFXAgent(BaseAgent):
    """
    Creates visual effects for the world.

    Responsible for:

    - particles
    - weather
    - magic
    - lighting
    - environmental effects
    - destruction effects
    - portals
    """

    def __init__(self):

        super().__init__(
            name="Spark",
            role="VFX Artist",
            skills=[
                "vfx",
                "particles",
                "weather",
                "lighting",
                "magic"
            ]
        )

        self.effects = []



    def create_effect(
        self,
        name,
        effect_type,
        target=None
    ):

        effect = {

            "name": name,

            "type": effect_type,

            "target": target,

            "created": datetime.utcnow().isoformat(),

            "emitters": [],

            "lights": [],

            "materials": [],

            "audio_sync": False

        }

        self.effects.append(effect)

        return effect



    def add_emitter(
        self,
        effect,
        emitter_type,
        count=1
    ):

        effect["emitters"].append({

            "type": emitter_type,

            "count": count

        })



    def add_light(
        self,
        effect,
        colour,
        intensity
    ):

        effect["lights"].append({

            "colour": colour,

            "intensity": intensity

        })



    def add_material(
        self,
        effect,
        material
    ):

        effect["materials"].append(material)



    def enable_audio_sync(
        self,
        effect
    ):

        effect["audio_sync"] = True



    def validate(
        self,
        effect
    ):

        return {

            "emitters": len(effect["emitters"]),

            "lights": len(effect["lights"]),

            "materials": len(effect["materials"]),

            "ready": True

        }



    def work(self):

        if self.current_job:

            return (
                f"Creating VFX for "
                f"{self.current_job.name}"
            )

        return "VFX Agent waiting"