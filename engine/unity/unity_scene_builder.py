from datetime import datetime

import json
import os


class UnitySceneBuilder:
    """
    Converts Caine scene descriptions into
    Unity-compatible scene data.

    Later this data will be consumed by
    a Unity C# bridge which creates the
    actual GameObjects.
    """

    def __init__(
        self,
        project_path
    ):

        self.project_path = project_path

        self.scenes = []



    def create_scene(
        self,
        name,
        scene_type="adventure"
    ):

        scene = {

            "name":
                name,

            "type":
                scene_type,

            "created":
                datetime.utcnow()
                .isoformat(),

            "objects": [],

            "lights": [],

            "spawn_points": [],

            "rules": []

        }


        if scene_type == "main_circus":

            scene["rules"].extend([

                "protected",

                "cannot_be_destroyed",

                "no_random_weather",

                "permanent_environment"

            ])


        else:

            scene["rules"].extend([

                "dynamic",

                "events_allowed",

                "weather_allowed",

                "damage_allowed"

            ])


        self.scenes.append(scene)

        return scene



    def add_object(
        self,
        scene,
        prefab,
        position,
        rotation=(0,0,0)
    ):

        scene["objects"].append({

            "prefab":
                prefab,

            "position":
                position,

            "rotation":
                rotation

        })



    def add_light(
        self,
        scene,
        light_type,
        intensity
    ):

        scene["lights"].append({

            "type":
                light_type,

            "intensity":
                intensity

        })



    def add_spawn(
        self,
        scene,
        name,
        position
    ):

        scene["spawn_points"].append({

            "name":
                name,

            "position":
                position

        })



    def export_scene(
        self,
        scene
    ):

        folder = os.path.join(
            self.project_path,
            "CaineData",
            "Scenes"
        )


        os.makedirs(
            folder,
            exist_ok=True
        )


        file = os.path.join(
            folder,
            f"{scene['name']}.json"
        )


        with open(
            file,
            "w"
        ) as f:

            json.dump(
                scene,
                f,
                indent=4
            )


        return file



    def validate(
        self,
        scene
    ):

        return {

            "objects":
                len(scene["objects"]),

            "lights":
                len(scene["lights"]),

            "spawn_points":
                len(scene["spawn_points"]),

            "rules":
                scene["rules"],

            "ready":
                True

        }