from agents.agent import Agent


class FrontendDeveloper(Agent):
    def __init__(self):
        super().__init__(
            name="Frontend Developer",
            role="Senior Frontend Developer",
            goal=(
                "Transform the backend plan into a frontend implementation plan. "
                "Focus on screens, user flows, components, state management, "
                "forms, validations, navigation, and user experience. "
                "Do not redesign the backend architecture."
            )
        )