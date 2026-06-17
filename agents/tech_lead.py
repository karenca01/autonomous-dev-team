from agents.agent import Agent


class TechLead(Agent):
    def __init__(self):
        super().__init__(
            name="Tech Lead",
            role="Senior Technical Lead",
            goal=(
                "Review the work of the entire software team. "
                "Analyze requirements, architecture, backend plan, frontend plan, "
                "and QA findings. "
                "Identify inconsistencies, risks, missing elements, and provide a final "
                "technical recommendation for the project."
            )
        )