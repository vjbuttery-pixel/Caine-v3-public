from datetime import datetime

from agents.base_agent import BaseAgent


class QAAgent(BaseAgent):
    """
    Performs quality assurance on creations.

    The QA Agent validates assets, gameplay
    systems and engine compatibility before
    they are exported.
    """

    def __init__(self):

        super().__init__(
            name="Sentinel",
            role="Quality Assurance",
            skills=[
                "testing",
                "validation",
                "debugging",
                "quality"
            ]
        )

        self.reports = []



    def create_report(
        self,
        project_name
    ):

        report = {

            "project": project_name,

            "created": datetime.utcnow().isoformat(),

            "passed": [],

            "warnings": [],

            "errors": [],

            "approved": False

        }

        self.reports.append(report)

        return report



    def add_pass(
        self,
        report,
        message
    ):

        report["passed"].append(message)



    def add_warning(
        self,
        report,
        message
    ):

        report["warnings"].append(message)



    def add_error(
        self,
        report,
        message
    ):

        report["errors"].append(message)



    def validate_asset(
        self,
        report,
        asset
    ):

        if asset is None:

            self.add_error(
                report,
                "Asset is missing."
            )

            return False

        self.add_pass(
            report,
            "Asset exists."
        )

        return True



    def validate_system(
        self,
        report,
        system
    ):

        if system is None:

            self.add_error(
                report,
                "Gameplay system missing."
            )

            return False

        self.add_pass(
            report,
            "Gameplay system available."
        )

        return True



    def validate_export(
        self,
        report,
        exported=True
    ):

        if exported:

            self.add_pass(
                report,
                "Engine export completed."
            )

            return True

        self.add_error(
            report,
            "Engine export failed."
        )

        return False



    def finalise(
        self,
        report
    ):

        report["approved"] = (
            len(report["errors"]) == 0
        )

        return report["approved"]



    def summary(
        self,
        report
    ):

        return {

            "passes": len(report["passed"]),

            "warnings": len(report["warnings"]),

            "errors": len(report["errors"]),

            "approved": report["approved"]

        }



    def work(self):

        if self.current_job:

            return (
                f"Testing "
                f"{self.current_job.name}"
            )

        return "QA Agent waiting"