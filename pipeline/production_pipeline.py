from datetime import datetime


class ProductionPipeline:
    """
    Coordinates every production agent.

    The pipeline moves a project through
    every stage until it is ready to be
    exported into a game engine.
    """

    def __init__(self):

        self.stages = [

            "Planning",

            "Architecture",

            "Model",

            "Rigging",

            "Animation",

            "VFX",

            "Audio",

            "Programming",

            "QA",

            "Export"

        ]

        self.completed = []

        self.started = datetime.utcnow()



    def next_stage(self):

        if len(self.completed) >= len(self.stages):

            return None

        return self.stages[len(self.completed)]



    def complete_stage(self):

        stage = self.next_stage()

        if stage is None:

            return None

        self.completed.append(stage)

        return stage



    def finished(self):

        return len(self.completed) == len(self.stages)



    def progress(self):

        return {

            "completed": len(self.completed),

            "total": len(self.stages),

            "current": self.next_stage(),

            "finished": self.finished()

        }