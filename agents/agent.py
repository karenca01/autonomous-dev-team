from config.gemini_client import GeminiClient


class Agent:
    def __init__(
        self,
        name,
        role,
        goal,
        model="gemini-2.5-flash"
    ):
        self.name = name
        self.role = role
        self.goal = goal
        self.model = model

        self.client = GeminiClient(model)

    def think(self, message):
        prompt = f"""
        Role:
        {self.role}

        Goal:
        {self.goal}

        Message:
        {message}
        """

        return self.client.generate_response(prompt)