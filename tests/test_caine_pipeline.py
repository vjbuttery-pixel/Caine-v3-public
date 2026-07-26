import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from agents.director_agent import DirectorAgent
from agents.architect_agent import ArchitectAgent
from agents.model_agent import ModelAgent
from agents.rigging_agent import RiggingAgent
from agents.animation_agent import AnimationAgent
from agents.vfx_agent import VFXAgent
from agents.audio_agent import AudioAgent
from agents.programmer_agent import ProgrammerAgent
from agents.qa_agent import QAAgent

from engine.asset_registry import AssetRegistry
from engine.scene_builder import SceneBuilder
from engine.export_project import ProjectExporter


class TestProject:

    def __init__(self, name):

        self.name = name


def main():

    print("\n========== CAINE PIPELINE TEST ==========\n")

    project = TestProject(
        "Pipeline Test World"
    )

    print("Creating agents...")

    director = DirectorAgent()
    architect = ArchitectAgent()
    modeller = ModelAgent()
    rigger = RiggingAgent()
    animator = AnimationAgent()
    vfx = VFXAgent()
    audio = AudioAgent()
    programmer = ProgrammerAgent()
    qa = QAAgent()

    print("✓ Agents created")

    registry = AssetRegistry()

    scene_builder = SceneBuilder()

    exporter = ProjectExporter()

    print("✓ Core systems created")

    print("\nCreating Main Circus...")

    circus = scene_builder.create_scene(
        "Main Circus",
        "main_circus"
    )

    scene_builder.add_object(
        circus,
        "CentralTent",
        (0, 0, 0)
    )

    scene_builder.add_spawn_point(
        circus,
        "PlayerSpawn",
        (0, 0, 0)
    )

    print(scene_builder.validate(circus))

    print("\nRegistering assets...")

    asset = registry.register_asset(
        "Central Tent",
        "model",
        "assets/models/central_tent.fbx",
        "ModelAgent"
    )

    print(asset)

    print("\nExporting project...")

    result = exporter.export(
        project
    )

    print(result)

    print("\nRunning QA...")

    report = qa.create_report(
        project.name
    )

    qa.validate_asset(
        report,
        asset
    )

    qa.validate_system(
        report,
        circus
    )

    qa.validate_export(
        report,
        True
    )

    qa.finalise(
        report
    )

    print(
        qa.summary(report)
    )

    print("\n========== SUCCESS ==========")


if __name__ == "__main__":
    main()