from datetime import datetime


class CommandExecutor:
    """
    Executes queued commands using the
    currently selected engine.

    This is the final step between
    Caine's thinking and the game engine.
    """

    def __init__(self, engine_manager):

        self.engine_manager = engine_manager

        self.completed = []

        self.failed = []



    def execute(self, command):

        engine = self.engine_manager.get_engine()

        if engine is None:

            command.fail()

            self.failed.append(command)

            return False


        try:

            command_type = command.command_type

            payload = command.payload


            if command_type == "CreateScene":

                engine.create_scene({

                    "name": payload["name"],

                    "objects": [],

                    "type": payload["scene_type"]

                })


            elif command_type == "SpawnPrefab":

                # Temporary implementation.
                # Later this becomes a Unity Bridge command.
                print(
                    f"Spawning prefab: "
                    f"{payload['prefab']}"
                )


            elif command_type == "DestroyObject":

                print(
                    f"Destroying: "
                    f"{payload['name']}"
                )


            else:

                raise Exception(
                    f"Unknown command: {command_type}"
                )


            command.complete()

            self.completed.append(command)

            return True


        except Exception as e:

            print(e)

            command.fail()

            self.failed.append(command)

            return False



    def summary(self):

        return {

            "completed":
                len(self.completed),

            "failed":
                len(self.failed),

            "time":
                datetime.utcnow().isoformat()

        }