from datetime import datetime
import uuid


class AgentManager:
    """
    Controls all Caine worker agents.

    Responsibilities:

    - Register agents
    - Find capable agents
    - Assign jobs
    - Monitor workers
    """

    def __init__(self):

        self.id = str(uuid.uuid4())

        self.agents = []

        self.job_history = []

        self.created_at = datetime.utcnow()



    def register_agent(self, agent):

        """
        Adds an agent to Caine's workforce.
        """

        self.agents.append(agent)



    def remove_agent(self, agent):

        """
        Removes an agent.
        """

        if agent in self.agents:

            self.agents.remove(agent)



    def find_agent(self, job):

        """
        Finds the best agent for a job.

        Uses the job category and
        agent skills.
        """

        possible = []


        for agent in self.agents:

            if agent.status != "idle":

                continue


            if agent.has_skill(
                job.category
            ):

                possible.append(agent)



        if len(possible) == 0:

            return None


        return possible[0]



    def assign_job(self, job):

        """
        Automatically assigns
        a job to a suitable agent.
        """

        agent = self.find_agent(
            job
        )


        if agent is None:

            return False



        success = agent.assign_job(
            job
        )


        if success:

            self.job_history.append({

                "job": job.name,

                "agent": agent.name,

                "time":
                    datetime.utcnow().isoformat()

            })


        return success



    def get_idle_agents(self):

        """
        Returns available workers.
        """

        return [

            agent

            for agent in self.agents

            if agent.status == "idle"

        ]



    def get_active_agents(self):

        """
        Returns busy workers.
        """

        return [

            agent

            for agent in self.agents

            if agent.status == "working"

        ]



    def get_status(self):

        return {

            "agents":
                len(self.agents),

            "idle":
                len(self.get_idle_agents()),

            "working":
                len(self.get_active_agents())

        }