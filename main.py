from config.gemini_client import GeminiClient


client = GeminiClient()

response = client.generate_response(
    "Explícame en una frase qué es un sistema multiagente."
)

print(response)