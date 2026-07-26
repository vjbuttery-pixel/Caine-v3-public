from datetime import datetime


class SceneBuilder:
    """
    Converts Caine world designs into
    engine-independent scene data.

    The result can later be converted
    into Unity scenes, Godot scenes,
    or Unreal levels.
    """

    def __init__(self):

        self.scenes = []



    def create_scene(
        self,
        name,
        zone_type="adventure"
    ):

        scene = {

            "name": name,

            "zone_type": zone_type,

            "created":
                datetime.utcnow().isoformat(),

            "objects": [],

            "spawn_points": [],

            "lighting": {},

            "environment": {},

            "rules": []

        }


        if zone_type == "main_circus":

            scene["rules"].extend([

                "Protected zone",

                "No destructive events",

                "Permanent structures",

                "Safe resident area"

            ])


        else:

            scene["rules"].extend([

                "Dynamic environment",

                "Events allowed",

                "Temporary structures possible"

            ])


        self.scenes.append(scene)

        return scene



    def add_object(
        self,
        scene,
        asset,
        position,
        rotation=(0,0,0)
    ):

        scene["objects"].append({

            "asset": asset,

            "position": position,

            "rotation": rotation

        })



    def add_spawn_point(
        self,
        scene,
        name,
        position
    ):

        scene["spawn_points"].append({

            "name": name,

            "position": position

        })



    def set_lighting(
        self,
        scene,
        lighting_data
    ):

        scene["lighting"] = lighting_data



    def set_environment(
        self,
        scene,
        environment_data
    ):

        scene["environment"] = environment_data



    def validate(
        self,
        scene
    ):

        return {

            "objects":
                len(scene["objects"]),

            "spawn_points":
                len(scene["spawn_points"]),

            "zone":
                scene["zone_type"],

            "rules":
                scene["rules"],

            "ready":
                True

        }