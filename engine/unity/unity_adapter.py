from engine.engine_adapter import EngineAdapter

from datetime import datetime


class UnityAdapter(EngineAdapter):
    """
    Unity implementation of Caine's
    engine communication layer.

    This will eventually communicate with
    Unity through generated files, the Unity
    Editor API, or a local bridge tool.
    """

    def __init__(self):

        self.connected = False

        self.project = None

        self.imported_assets = []



    def initialise(self):

        self.connected = True

        return {
            "engine": "Unity",
            "version": "Unity 6",
            "connected": True
        }



    def create_project(
        self,
        project
    ):

        self.project = project

        return {

            "project":
                project.name,

            "created":
                datetime.utcnow()
                .isoformat(),

            "engine":
                "Unity"

        }



    def import_model(
        self,
        model
    ):

        asset = {

            "type":
                "model",

            "name":
                model["name"]

        }


        self.imported_assets.append(asset)


        return asset



    def import_material(
        self,
        material
    ):

        asset = {

            "type":
                "material",

            "name":
                material

        }


        self.imported_assets.append(asset)


        return asset



    def import_animation(
        self,
        animation
    ):

        asset = {

            "type":
                "animation",

            "name":
                animation

        }


        self.imported_assets.append(asset)


        return asset



    def import_audio(
        self,
        audio
    ):

        asset = {

            "type":
                "audio",

            "name":
                audio

        }


        self.imported_assets.append(asset)


        return asset



    def import_vfx(
        self,
        effect
    ):

        asset = {

            "type":
                "vfx",

            "name":
                effect

        }


        self.imported_assets.append(asset)


        return asset



    def create_scene(
        self,
        scene
    ):

        return {

            "scene":
                scene["name"],

            "objects":
                len(scene["objects"])

        }



    def save_project(self):

        return {

            "saved":
                True,

            "time":
                datetime.utcnow()
                .isoformat()

        }



    def build(self):

        return {

            "build":
                "successful",

            "engine":
                "Unity"

        }



    def play(self):

        return {

            "running":
                True,

            "engine":
                "Unity"

        }