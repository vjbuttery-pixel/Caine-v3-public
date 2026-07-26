import json
import os



class KnowledgeMemory:
    """
    Saves and loads Caine's learned knowledge.

    This allows knowledge to survive
    after the program closes.
    """



    def __init__(
        self,
        graph,
        file_path="knowledge/memory.json"
    ):

        self.graph = graph

        self.file_path = file_path



    def save(self):

        folder = os.path.dirname(
            self.file_path
        )


        if folder:

            os.makedirs(
                folder,
                exist_ok=True
            )



        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(

                self.graph.describe(),

                file,

                indent=4

            )



    def load(self):

        if not os.path.exists(
            self.file_path
        ):

            return False



        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:


            data = json.load(
                file
            )


        self.graph.concepts = data.get(
            "concepts",
            {}
        )


        self.graph.relationships = data.get(
            "relationships",
            []
        )


        return True