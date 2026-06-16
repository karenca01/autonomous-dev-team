# from config.gemini_client import GeminiClient


# client = GeminiClient()

# response = client.generate_response(
#     "Explícame en una frase qué es un sistema multiagente."
# )

# print(response)

from agents.agent import Agent


product_manager = Agent(
    name="Product Manager",
    role="Senior Product Manager",
    goal="Convert software ideas into clear requirements"
)

response = product_manager.think(
    "I want an application to track personal habits."
)

print(response)