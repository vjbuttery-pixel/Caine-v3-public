from core.commands.command import Command


class CommandFactory:
    """
    Creates standard command objects.
    """

    @staticmethod
    def spawn_prefab(
        prefab,
        position,
        rotation=(0, 0, 0)
    ):

        return Command(

            command_type="SpawnPrefab",

            payload={

                "prefab": prefab,

                "position": position,

                "rotation": rotation

            },

            priority=8

        )

    @staticmethod
    def create_scene(
        name,
        scene_type
    ):

        return Command(

            command_type="CreateScene",

            payload={

                "name": name,

                "scene_type": scene_type

            },

            priority=10

        )

    @staticmethod
    def destroy_object(
        object_name
    ):

        return Command(

            command_type="DestroyObject",

            payload={

                "name": object_name

            },

            priority=6

        )