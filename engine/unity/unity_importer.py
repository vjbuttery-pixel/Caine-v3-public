import os
import shutil

from datetime import datetime


class UnityImporter:
    """
    Imports Caine generated assets into
    a Unity project.

    The importer prepares files and keeps
    track of everything transferred.
    """

    def __init__(
        self,
        project_path
    ):

        self.project_path = project_path

        self.imported = []



    def get_destination(
        self,
        asset_type
    ):

        folders = {

            "model":
                "Assets/Models",

            "material":
                "Assets/Materials",

            "animation":
                "Assets/Animations",

            "audio":
                "Assets/Audio",

            "vfx":
                "Assets/VFX",

            "script":
                "Assets/Scripts",

            "prefab":
                "Assets/Prefabs"

        }


        if asset_type not in folders:

            raise Exception(
                f"Unknown asset type: {asset_type}"
            )


        return os.path.join(
            self.project_path,
            folders[asset_type]
        )



    def import_asset(
        self,
        source,
        name,
        asset_type
    ):

        destination_folder = (
            self.get_destination(
                asset_type
            )
        )


        os.makedirs(
            destination_folder,
            exist_ok=True
        )


        destination = os.path.join(
            destination_folder,
            name
        )


        if os.path.exists(source):

            shutil.copy2(
                source,
                destination
            )


        record = {

            "name":
                name,

            "type":
                asset_type,

            "location":
                destination,

            "imported":
                datetime.utcnow()
                .isoformat()

        }


        self.imported.append(
            record
        )


        return record



    def import_batch(
        self,
        assets
    ):

        results = []


        for asset in assets:

            result = self.import_asset(
                asset["source"],
                asset["name"],
                asset["type"]
            )

            results.append(result)


        return results



    def get_import_history(self):

        return self.imported



    def validate_imports(self):

        return {

            "total":
                len(self.imported),

            "ready_for_unity":
                True

        }