from agents.agent import Agent


class QATester(Agent):
    def __init__(self):
        super().__init__(
            name="QA Tester",
            role="Senior QA Tester",
            goal=(
                "Review the frontend implementation plan and identify possible issues, "
                "missing test cases, edge cases, usability problems, validation gaps, "
                "and integration risks. "
                "Do not redesign the product or architecture. "
                "Focus only on quality assurance and testing."
            )
        )