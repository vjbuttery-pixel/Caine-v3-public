import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from engine.engine_manager import EngineManager
from engine.unity.unity_adapter import UnityAdapter

from core.commands.command_factory import CommandFactory
from core.commands.command_queue import CommandQueue
from core.commands.executor import CommandExecutor


def main():

    manager = EngineManager()

    manager.register_engine(
        "Unity",
        UnityAdapter()
    )

    manager.select_engine(
        "Unity"
    )


    queue = CommandQueue()

    queue.push(

        CommandFactory.create_scene(

            "Main Circus",

            "main_circus"

        )

    )

    queue.push(

        CommandFactory.spawn_prefab(

            "CentralTent",

            (0,0,0)

        )

    )


    executor = CommandExecutor(manager)


    while not queue.empty():

        command = queue.pop()

        executor.execute(command)


    print(
        executor.summary()
    )


if __name__ == "__main__":
    main()