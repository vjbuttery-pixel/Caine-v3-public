class CapabilityPlanner:
    """
    Converts understood ideas into required creation capabilities.

    Caine does not choose generators here.
    Caine only decides what abilities are needed.
    """


    def plan(self, idea_data):

        plan = {

            "object": idea_data.get(
                "core_object"
            ),

            "required_capabilities": [],

            "visual_requirements": {

                "shape": [],

                "materials": [],

                "effects": []

            },

            "environment_requirements": []

        }



        core = idea_data.get(
            "core_object"
        )

        modifiers = idea_data.get(
            "modifiers",
            []
        )

        environments = idea_data.get(
            "environment",
            []
        )



        # -------------------------
        # Core object capabilities
        # -------------------------

        if core == "castle":

            plan["required_capabilities"].extend(
                [
                    "large_structure",
                    "fantasy_architecture",
                    "interior_spaces"
                ]
            )


            plan["visual_requirements"]["shape"].extend(
                [
                    "towers",
                    "walls",
                    "gate"
                ]
            )


            plan["visual_requirements"]["materials"].extend(
                [
                    "stone",
                    "metal",
                    "glass"
                ]
            )



        if core == "forest":

            plan["required_capabilities"].extend(
                [
                    "vegetation_generation",
                    "terrain_generation"
                ]
            )



        # -------------------------
        # Modifier capabilities
        # -------------------------

        for modifier in modifiers:


            if modifier == "flying":

                plan["required_capabilities"].append(
                    "floating_structure"
                )

                plan["visual_requirements"]["effects"].append(
                    "levitation_visuals"
                )



            if modifier == "magical":

                plan["required_capabilities"].append(
                    "magic_system"
                )

                plan["visual_requirements"]["effects"].extend(
                    [
                        "glowing_materials",
                        "magic_particles"
                    ]
                )



            if modifier == "ancient":

                plan["visual_requirements"]["materials"].append(
                    "weathered_surfaces"
                )



        # -------------------------
        # Environment
        # -------------------------

        for environment in environments:


            if environment == "forest":

                plan["environment_requirements"].append(
                    "forest_biome"
                )


            if environment == "ocean":

                plan["environment_requirements"].append(
                    "water_generation"
                )


        return plan