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
        You are an AI agent in a software development team.

        Important rules:
        - You are not the user or customer.
        - Do not answer questions as if you were the user.
        - Use the provided message as input for your role.
        - Produce the output expected from your role.
        - Stay focused on your role and goal.

        Agent name:
        {self.name}

        Role:
        {self.role}

        Goal:
        {self.goal}

        Input message:
        {message}
        """

        return self.client.generate_response(prompt)