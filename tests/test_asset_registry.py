import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from engine.asset_registry import AssetRegistry



def run_test():

    print("\n--- ASSET REGISTRY TEST ---")


    registry = AssetRegistry()


    castle = registry.register_asset(
        "Flying Candy Castle",
        "model",
        "Assets/Models/Castle.fbx",
        "ModelAgent"
    )


    print(
        castle
    )


    found = registry.find_asset(
        "Flying Candy Castle"
    )


    print(
        "Found:"
    )

    print(
        found
    )


    registry.add_dependency(
        castle["id"],
        "MagicMaterial"
    )


    print(
        registry.summary()
    )


    print(
        "\nASSET TEST COMPLETE"
    )



if __name__ == "__main__":

    run_test()