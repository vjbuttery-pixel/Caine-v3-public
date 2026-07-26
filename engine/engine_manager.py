from datetime import datetime


class EngineManager:
    """
    Controls connections between Caine
    and supported game engines.
    """

    def __init__(self):

        self.adapters = {}

        self.active_engine = None

        self.connected = False

        self.history = []



    def register_engine(
        self,
        name,
        adapter
    ):
        """
        Adds an engine adapter.
        """

        self.adapters[name] = adapter



    def select_engine(
        self,
        name
    ):
        """
        Selects the engine Caine will use.
        """

        if name not in self.adapters:

            raise Exception(
                f"Engine {name} not registered"
            )


        self.active_engine = (
            self.adapters[name]
        )


        self.active_engine.initialise()


        self.connected = True


        self.history.append({

            "engine": name,

            "time":
                datetime.utcnow().isoformat(),

            "event":
                "Engine selected"

        })


        return True



    def get_engine(self):

        return self.active_engine



    def create_project(
        self,
        project
    ):

        if not self.connected:

            raise Exception(
                "No engine connected"
            )


        return self.active_engine.create_project(
            project
        )



    def import_creation(
        self,
        creation
    ):

        """
        Sends generated content
        to the selected engine.
        """

        if not self.connected:

            raise Exception(
                "No engine connected"
            )


        results = {}


        if "models" in creation:

            results["models"] = [

                self.active_engine.import_model(
                    model
                )

                for model in creation["models"]

            ]


        if "materials" in creation:

            results["materials"] = [

                self.active_engine.import_material(
                    material
                )

                for material in creation["materials"]

            ]


        if "animations" in creation:

            results["animations"] = [

                self.active_engine.import_animation(
                    animation
                )

                for animation in creation["animations"]

            ]


        if "audio" in creation:

            results["audio"] = [

                self.active_engine.import_audio(
                    audio
                )

                for audio in creation["audio"]

            ]


        if "vfx" in creation:

            results["vfx"] = [

                self.active_engine.import_vfx(
                    effect
                )

                for effect in creation["vfx"]

            ]


        return results



    def build_game(self):

        if not self.connected:

            raise Exception(
                "No engine connected"
            )


        return self.active_engine.build()



    def run_game(self):

        if not self.connected:

            raise Exception(
                "No engine connected"
            )


        return self.active_engine.play()



    def status(self):

        return {

            "connected":
                self.connected,

            "active_engine":
                type(
                    self.active_engine
                ).__name__
                if self.active_engine
                else None,

            "available_engines":
                list(
                    self.adapters.keys()
                )

        }