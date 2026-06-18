from strands import Agent
from strands.models.gemini import GeminiModel

from config.agent_configs import PRODUCT_MANAGER, ARCHITECT


class StrandsDevTeam:
    def __init__(self):
        self.model = GeminiModel(model_id="gemini-2.5-flash")

        self.product_manager = self._build_agent(PRODUCT_MANAGER)
        self.architect = self._build_agent(ARCHITECT)

    def _build_agent(self, config):
        system_prompt = f"""
You are an AI agent in a software development team.

Agent name:
{config["name"]}

Role:
{config["role"]}

Goal:
{config["goal"]}

Important rules:
- Stay focused on your role.
- Do not act as the user.
- Use the input as context.
- Produce the output expected from your role.
"""

        return Agent(
            model=self.model,
            system_prompt=system_prompt
        )

    def run(self, idea):
        print("\nRunning Product Manager...")
        pm_response = str(self.product_manager(idea))
        print("Product Manager completed")

        print("\nRunning Architect...")
        architect_response = str(self.architect(pm_response))
        print("Architect completed")

        return {
            "product_manager": pm_response,
            "architect": architect_response,
        }