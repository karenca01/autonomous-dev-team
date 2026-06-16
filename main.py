from agents.product_manager import ProductManager
from agents.architect import Architect


idea = """
I want an application to track personal habits.
"""


product_manager = ProductManager()
architect = Architect()


pm_response = product_manager.think(idea)

architect_response = architect.think(pm_response)


print("=== PRODUCT MANAGER ===")
print(pm_response)

print("\n\n=== ARCHITECT ===")
print(architect_response)