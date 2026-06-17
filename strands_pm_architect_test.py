from dotenv import load_dotenv
from strands import Agent
from strands.models.gemini import GeminiModel

from config.agent_configs import (
    PRODUCT_MANAGER,
    ARCHITECT
)

load_dotenv()

model = GeminiModel(
    model_id="gemini-2.5-flash"
)


def build_agent(config):
    return Agent(
        model=model,
        system_prompt=f"""
You are an AI agent in a software development team.

Agent name:
{config["name"]}

Role:
{config["role"]}

Goal:
{config["goal"]}

Important rules:
- Stay focused on your role.
- Produce the output expected from your role.
- Do not act as the user.
"""
    )


product_manager = build_agent(PRODUCT_MANAGER)

architect = build_agent(ARCHITECT)

idea = """
I want a platform for students.

Students can:
- upload assignments
- receive grades

Teachers can:
- create courses
- review assignments

Administrators can:
- manage users
"""

print("\nRunning Product Manager...\n")

pm_response = str(product_manager(idea))

print("Product Manager completed")

print("\nRunning Architect...\n")

architect_response = str(
    architect(pm_response)
)

print("Architect completed")

print("\n===================")
print("ARCHITECT RESPONSE")
print("===================\n")

print(architect_response)