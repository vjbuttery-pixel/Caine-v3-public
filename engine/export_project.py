import os
import json

from datetime import datetime


class ProjectExporter:
    """
    Creates and manages exported Caine projects.

    This does not directly communicate with
    the game engine.

    It prepares everything required for
    engine import.
    """

    def __init__(
        self,
        base_directory="projects"
    ):

        self.base_directory = (
            base_directory
        )

        self.exports = []



    def create_project_folder(
        self,
        project_name
    ):

        safe_name = (
            project_name
            .replace(" ", "_")
            .lower()
        )


        path = os.path.join(
            self.base_directory,
            safe_name
        )


        folders = [

            "assets",

            "models",

            "materials",

            "animations",

            "audio",

            "vfx",

            "scripts",

            "scenes",

            "metadata"

        ]


        os.makedirs(
            path,
            exist_ok=True
        )


        for folder in folders:

            os.makedirs(
                os.path.join(
                    path,
                    folder
                ),
                exist_ok=True
            )


        return path



    def create_metadata(
        self,
        project,
        path
    ):

        metadata = {

            "name":
                project.name,

            "created":
                datetime.utcnow()
                .isoformat(),

            "status":
                "generated",

            "engine_ready":
                False

        }


        file = os.path.join(
            path,
            "metadata",
            "project.json"
        )


        with open(
            file,
            "w"
        ) as f:

            json.dump(
                metadata,
                f,
                indent=4
            )


        return metadata



    def register_export(
        self,
        project_name,
        path
    ):

        export = {

            "project":
                project_name,

            "location":
                path,

            "time":
                datetime.utcnow()
                .isoformat()

        }


        self.exports.append(
            export
        )


        return export



    def export(
        self,
        project
    ):

        path = (
            self.create_project_folder(
                project.name
            )
        )


        metadata = (
            self.create_metadata(
                project,
                path
            )
        )


        self.register_export(
            project.name,
            path
        )


        return {

            "path":
                path,

            "metadata":
                metadata

        }