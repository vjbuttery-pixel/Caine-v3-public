from datetime import datetime
import uuid


class Decision:
    """
    Result returned by the Governor.
    """

    APPROVED = "approved"

    REJECTED = "rejected"

    MODIFIED = "modified"




class Governor:
    """
    Controls whether actions and jobs
    should be allowed.

    The Governor does not create ideas.

    It protects the system from
    harmful, impossible or inefficient
    decisions.
    """

    def __init__(self):

        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()

        self.rules = []

        self.history = []



    def add_rule(self, rule):

        """
        Adds a decision rule.

        Future examples:

        - Do not destroy important history.
        - Do not overload resources.
        - Protect resident wellbeing.
        """

        self.rules.append(rule)



    def evaluate(self, action):

        """
        Checks whether an action
        should happen.

        Currently uses simple rules.

        Later this can become a reasoning system.
        """

        result = Decision.APPROVED

        reason = "No conflicts detected"



        for rule in self.rules:

            outcome = rule(action)


            if outcome:

                result = Decision.REJECTED

                reason = outcome

                break



        decision = {

            "action": action,

            "result": result,

            "reason": reason,

            "time": datetime.utcnow().isoformat()

        }


        self.history.append(decision)


        return decision



    def approve(self, action):

        """
        Shortcut for manually approving
        an action.
        """

        decision = {

            "action": action,

            "result": Decision.APPROVED,

            "reason": "Manually approved"

        }


        self.history.append(decision)

        return decision



    def reject(self, action, reason):

        """
        Shortcut for rejecting
        an action.
        """

        decision = {

            "action": action,

            "result": Decision.REJECTED,

            "reason": reason

        }


        self.history.append(decision)

        return decision



    def get_history(self):

        return self.history



    def status(self):

        return {

            "rules": len(self.rules),

            "decisions": len(self.history)

        }