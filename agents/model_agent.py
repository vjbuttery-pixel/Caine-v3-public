from datetime import datetime

from agents.base_agent import BaseAgent


class ModelAgent(BaseAgent):
    """
    Creates 3D model specifications.

    The Model Agent does not currently
    generate meshes directly.

    It produces a complete modelling plan
    that can later be converted into
    Blender, Unity, Unreal or Godot assets.
    """

    def __init__(self):

        super().__init__(
            name="Forge",
            role="3D Model Artist",
            skills=[
                "model",
                "mesh",
                "geometry",
                "materials"
            ]
        )

        self.models = []



    def create_model(
        self,
        asset_name,
        asset_type,
        concept_data=None
    ):

        concept_data = concept_data or {}

        model = {

            "name": asset_name,

            "type": asset_type,

            "created": datetime.utcnow().isoformat(),

            "components": [],

            "materials": [],

            "lods": [],

            "collision": True,

            "uv_mapped": False,

            "optimised": False,

            "metadata": concept_data

        }

        self.models.append(model)

        return model



    def add_component(
        self,
        model,
        component_name,
        description=""
    ):

        model["components"].append({

            "name": component_name,

            "description": description

        })



    def add_material(
        self,
        model,
        material_name
    ):

        if material_name not in model["materials"]:

            model["materials"].append(
                material_name
            )



    def generate_lods(
        self,
        model
    ):

        model["lods"] = [

            "LOD0",

            "LOD1",

            "LOD2"

        ]



    def optimise(
        self,
        model
    ):

        model["optimised"] = True



    def unwrap_uvs(
        self,
        model
    ):

        model["uv_mapped"] = True



    def validate(
        self,
        model
    ):

        return {

            "components":
                len(model["components"]),

            "materials":
                len(model["materials"]),

            "lods":
                len(model["lods"]),

            "ready_for_rigging":
                True

        }



    def work(self):

        if self.current_job:

            return (
                f"Building model for "
                f"{self.current_job.name}"
            )

        return "Model Agent waiting for assignment"