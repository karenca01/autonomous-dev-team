from strands import Agent
from strands.models.gemini import GeminiModel
from strands_tools import file_read

from config.agent_configs import PRODUCT_MANAGER, ARCHITECT

from tools.shared_memory_tools import save_agent_output, read_agent_output


class StrandsDevTeam:
    def __init__(self):
        self.model = GeminiModel(model_id="gemini-2.5-flash")

        self.product_manager = self._build_agent(PRODUCT_MANAGER)
        
        # self.architect = self._build_agent(ARCHITECT)
        self.architect = self._build_agent(
            ARCHITECT,
            tools=[file_read]
        )

    def _build_agent(self, config, tools=None):
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
            system_prompt=system_prompt,
            tools=tools or []
        )

    def run(self, idea):
        print("\nRunning Product Manager...")
        pm_response = str(self.product_manager(idea))
        save_agent_output("Product Manager", pm_response)
        print("Product Manager completed and SAVED to memory")

        print("\nArchitect READING Product Manager output from memory...")

        print("\nRunning Architect...")
        architect_prompt = """
        Read the file memory/product_manager.md using your available file reading tool.
        Then create the technical architecture based on that content.
        """

        architect_response = str(self.architect(architect_prompt))
        save_agent_output("Architect", architect_response)
        print("Architect completed and SAVED to memory")

        return {
            "product_manager": pm_response,
            "architect": architect_response,
        }