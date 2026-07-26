from datetime import datetime
import uuid


class Scheduler:
    """
    Controls the order in which Caine's work happens.

    It does not create ideas.

    It organizes existing goals,
    projects and jobs.
    """

    def __init__(self):

        self.id = str(uuid.uuid4())

        self.goals = []

        self.active_jobs = []

        self.completed_jobs = []

        self.running = True

        self.created_at = datetime.utcnow()



    def add_goal(self, goal):

        """
        Adds a goal for scheduling.
        """

        self.goals.append(goal)



    def collect_available_jobs(self):

        """
        Searches all active projects
        for jobs that can begin.
        """

        jobs = []


        for goal in self.goals:

            for project in goal.projects:

                available = project.get_active_jobs()

                jobs.extend(available)


        return jobs



    def prioritize_jobs(self, jobs):

        """
        Sorts jobs by importance.

        Higher priority jobs happen first.
        """

        return sorted(
            jobs,
            key=lambda job: job.priority.value,
            reverse=True
        )



    def choose_next_job(self):

        """
        Finds the next best job.
        """

        available = self.collect_available_jobs()


        if len(available) == 0:

            return None


        ordered = self.prioritize_jobs(
            available
        )


        return ordered[0]



    def start_job(self, job, agent=None):

        """
        Starts a selected job.
        """

        if agent is None:

            agent = "unknown"


        success = job.start(agent)


        if success:

            self.active_jobs.append(job)


        return success



    def complete_job(self, job, result=None):

        """
        Finishes a job and records it.
        """

        job.complete(result)


        if job in self.active_jobs:

            self.active_jobs.remove(job)


        self.completed_jobs.append(job)



    def get_status(self):

        """
        Returns scheduler information.
        """

        return {

            "goals": len(self.goals),

            "active_jobs": len(
                self.active_jobs
            ),

            "completed_jobs": len(
                self.completed_jobs
            )

        }



    def tick(self):

        """
        Main scheduler update.

        Called repeatedly by Caine's runtime.
        """

        if not self.running:

            return None


        job = self.choose_next_job()


        if job:

            return job


        return None