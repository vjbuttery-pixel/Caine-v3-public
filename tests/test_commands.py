import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from core.commands.command_queue import CommandQueue
from core.commands.command_factory import CommandFactory


def main():

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

            (0, 0, 0)

        )

    )

    while not queue.empty():

        command = queue.pop()

        print(command.to_dict())


if __name__ == "__main__":

    main()