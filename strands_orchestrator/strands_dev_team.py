from strands import Agent
from strands.models.gemini import GeminiModel
from strands_tools import file_read, file_write

from config.agent_configs import PRODUCT_MANAGER, ARCHITECT

from tools.shared_memory_tools import save_agent_output


class StrandsDevTeam:
    def __init__(self):
        self.model = GeminiModel(model_id="gemini-2.5-flash")

        self.product_manager = self._build_agent(
            PRODUCT_MANAGER,
            tools=[file_write]
        )
        
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
        pm_prompt = f"""
        Create the product requirements document for this idea:

        {idea}

        After generating the document, use your file writing tool to save it at:
        memory/product_manager.md

        The file content must be the full product requirements document.
        """

        pm_response = str(self.product_manager(pm_prompt))

        architect_prompt = """
        Read the file memory/product_manager.md using your available file reading tool.
        Then create the technical architecture based on that content.
        """

        architect_response = str(self.architect(architect_prompt))
        save_agent_output("Architect", architect_response)

        return {
            "product_manager": pm_response,
            "architect": architect_response,
        }