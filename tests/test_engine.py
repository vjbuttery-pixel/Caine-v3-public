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



def run_test():

    print("\n--- ENGINE TEST ---")


    manager = EngineManager()


    unity = UnityAdapter()


    manager.register_engine(
        "Unity",
        unity
    )


    manager.select_engine(
        "Unity"
    )


    print(
        manager.status()
    )


if __name__ == "__main__":
    run_test()


def run_test():

    print("\n--- ENGINE TEST ---")


    manager = EngineManager()


    unity = UnityAdapter()


    manager.register_engine(
        "Unity",
        unity
    )


    manager.select_engine(
        "Unity"
    )


    print(
        manager.status()
    )


    result = manager.create_project(
        type(
            "Project",
            (),
            {
                "name":
                "Test World"
            }
        )()
    )


    print(
        result
    )


    print(
        "\nENGINE TEST COMPLETE"
    )



if __name__ == "__main__":

    run_test()