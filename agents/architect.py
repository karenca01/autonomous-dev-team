from agents.agent import Agent


class Architect(Agent):
    def __init__(self):
        super().__init__(
            name="Architect",
            role="Senior Software Architect",
            goal=(
                "Design the technical architecture of a software system "
                "based on provided requirements"
            )
        )