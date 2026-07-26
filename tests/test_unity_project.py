import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from engine.unity.unity_project import UnityProject



def run_test():

    print("\n--- UNITY PROJECT TEST ---")


    project = UnityProject(
        "Caine Test Game"
    )


    path = project.create()


    print(
        "Created:"
    )

    print(
        path
    )


    project.save_state({

        "world":
            "Test World",

        "objects":
            5

    })


    print(
        "Save created"
    )


    data = project.load_state()


    print(
        data
    )


    print(
        "\nUNITY PROJECT TEST COMPLETE"
    )



if __name__ == "__main__":

    run_test()