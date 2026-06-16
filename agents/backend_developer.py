from agents.agent import Agent


class BackendDeveloper(Agent):
    def __init__(self):
        super().__init__(
            name="Backend Developer",
            role="Senior Backend Developer",
            goal=(
                "Transform the software architecture into a practical backend plan. "
                "Do not redesign the entire system. "
                "Focus only on backend responsibilities: API endpoints, data models, "
                "business logic, authentication if needed, validations, and error handling. "
                "Base your response on the architecture provided."
            )
        )