from datetime import datetime
import uuid


class CognitiveCore:
    """
    The central coordinator for Caine's reasoning systems.

    It connects:

    - Blackboard
    - Goals
    - Scheduler
    - Governor
    - Event Bus

    It does not directly create assets.

    It decides what should happen next.
    """

    def __init__(
        self,
        blackboard,
        scheduler,
        governor,
        event_bus
    ):

        self.id = str(uuid.uuid4())

        self.blackboard = blackboard

        self.scheduler = scheduler

        self.governor = governor

        self.event_bus = event_bus


        self.running = True

        self.created_at = datetime.utcnow()


        self.thought_history = []



    def observe(self):

        """
        Reads current world information.

        Future expansion:

        - Sensors
        - Player actions
        - Resident behaviour
        - World events
        """

        return self.blackboard.get_all()



    def think(self):

        """
        Main reasoning cycle.

        Called repeatedly by Caine's runtime.
        """

        if not self.running:

            return None


        situation = self.observe()


        thought = {

            "time": datetime.utcnow().isoformat(),

            "situation": situation

        }


        self.thought_history.append(
            thought
        )


        return self.decide()



    def decide(self):

        """
        Chooses the next action.

        Currently:

        Scheduler finds work.
        Governor approves it.

        Later:

        Caine reasoning model
        will influence decisions.
        """

        job = self.scheduler.tick()


        if job is None:

            return None



        decision = self.governor.evaluate(
            job.name
        )


        if decision["result"] == "approved":

            return job



        return None



    def execute_cycle(self):

        """
        Runs one complete thinking cycle.
        """

        job = self.think()


        if job:

            self.event_bus.emit(
                "job_selected",
                {
                    "job": job.name
                }
            )


        return job



    def stop(self):

        self.running = False



    def start(self):

        self.running = True



    def get_thought_history(self):

        return self.thought_history