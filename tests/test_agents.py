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



def run_test():

    print("\n--- AGENT SYSTEM TEST ---")


    agents = [

        DirectorAgent(),

        ArchitectAgent(),

        ModelAgent(),

        RiggingAgent(),

        AnimationAgent(),

        VFXAgent(),

        AudioAgent(),

        ProgrammerAgent(),

        QAAgent()

    ]


    for agent in agents:

        print(
            "\nTesting:",
            agent.name
        )


        print(
            "Role:",
            agent.role
        )


        print(
            "Skills:",
            agent.skills
        )


        print(
            "Status:",
            agent.work()
        )


    print(
        "\nALL AGENTS LOADED SUCCESSFULLY"
    )



if __name__ == "__main__":

    run_test()