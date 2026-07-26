import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from engine.unity.unity_scene_builder import UnitySceneBuilder



def run_test():

    print("\n--- SCENE BUILDER TEST ---")


    builder = UnitySceneBuilder(
        "test_project"
    )


    circus = builder.create_scene(
        "Main Circus",
        "main_circus"
    )


    builder.add_object(
        circus,
        "CircusTent.prefab",
        (0,0,0)
    )


    builder.add_spawn(
        circus,
        "Player",
        (5,0,5)
    )


    print(
        builder.validate(
            circus
        )
    )


    adventure = builder.create_scene(
        "Candy Kingdom",
        "adventure"
    )


    print(
        builder.validate(
            adventure
        )
    )


    print(
        "\nSCENE TEST COMPLETE"
    )



if __name__ == "__main__":

    run_test()