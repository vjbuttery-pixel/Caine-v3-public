from datetime import datetime

from agents.base_agent import BaseAgent


class AudioAgent(BaseAgent):
    """
    Creates audio plans for worlds,
    characters and gameplay.

    The Audio Agent designs complete
    soundscapes instead of isolated
    audio clips.
    """

    def __init__(self):

        super().__init__(
            name="Harmony",
            role="Audio Designer",
            skills=[
                "music",
                "voice",
                "ambient_audio",
                "sound_effects"
            ]
        )

        self.soundscapes = []



    def create_soundscape(
        self,
        name,
        category
    ):

        soundscape = {

            "name": name,

            "category": category,

            "created": datetime.utcnow().isoformat(),

            "music": [],

            "ambient": [],

            "effects": [],

            "voices": [],

            "mix_settings": {

                "reverb": 0.0,

                "environment_size": "medium",

                "dynamic_range": "normal"

            }

        }

        self.soundscapes.append(soundscape)

        return soundscape



    def add_music(
        self,
        soundscape,
        description
    ):

        soundscape["music"].append(description)



    def add_ambient(
        self,
        soundscape,
        description
    ):

        soundscape["ambient"].append(description)



    def add_effect(
        self,
        soundscape,
        description
    ):

        soundscape["effects"].append(description)



    def add_voice(
        self,
        soundscape,
        character_name,
        voice_profile
    ):

        soundscape["voices"].append({

            "character": character_name,

            "profile": voice_profile

        })



    def set_mix(
        self,
        soundscape,
        reverb=0.0,
        environment_size="medium",
        dynamic_range="normal"
    ):

        soundscape["mix_settings"] = {

            "reverb": reverb,

            "environment_size": environment_size,

            "dynamic_range": dynamic_range

        }



    def validate(
        self,
        soundscape
    ):

        return {

            "music": len(soundscape["music"]),

            "ambient": len(soundscape["ambient"]),

            "effects": len(soundscape["effects"]),

            "voices": len(soundscape["voices"]),

            "ready": True

        }



    def work(self):

        if self.current_job:

            return (
                f"Creating audio for "
                f"{self.current_job.name}"
            )

        return "Audio Agent waiting"