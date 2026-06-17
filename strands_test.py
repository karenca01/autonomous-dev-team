import os
from dotenv import load_dotenv
from strands import Agent
from strands.models.gemini import GeminiModel


load_dotenv()

model = GeminiModel(
    model_id="gemini-2.5-flash",
)

agent = Agent(
    model=model,
    system_prompt="You are a helpful software architect."
)

response = agent("Explain in one sentence what a multi-agent system is.")

print(response)