from dotenv import load_dotenv
from strands import Agent
from strands.models.gemini import GeminiModel
from config.agent_configs import PRODUCT_MANAGER


load_dotenv()

model = GeminiModel(
    model_id="gemini-2.5-flash"
)

system_prompt = f"""
You are an AI agent in a software development team.

Agent name:
{PRODUCT_MANAGER["name"]}

Role:
{PRODUCT_MANAGER["role"]}

Goal:
{PRODUCT_MANAGER["goal"]}

Important rules:
- Stay focused on your role and goal.
- Do not answer as the user.
- Produce the output expected from your role.
"""

product_manager = Agent(
    model=model,
    system_prompt=system_prompt
)

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

response = product_manager(idea)

print(response)