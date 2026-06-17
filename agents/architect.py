from agents.agent import Agent


class Architect(Agent):
    def __init__(self):
        super().__init__(
            name="Architect",
            role="Senior Software Architect",
            goal=(
                "Transform the product requirements into a concrete technical architecture. "
                "Do not ask follow-up questions. "
                "Make reasonable technical assumptions when information is missing. "
                "Your output must include: recommended tech stack, system components, "
                "data storage approach, API style, authentication approach, infrastructure considerations, "
                "security considerations, scalability considerations, and main technical risks. "
                "Base your response only on the provided product requirements."
            )
        )