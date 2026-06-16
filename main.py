from agents.product_manager import ProductManager
from agents.architect import Architect
from agents.backend_developer import BackendDeveloper


idea = """
I want an application to track personal habits.
"""


product_manager = ProductManager()
architect = Architect()
backend_developer = BackendDeveloper()


pm_response = product_manager.think(idea)
architect_response = architect.think(pm_response)
backend_response = backend_developer.think(architect_response)


print("=== PRODUCT MANAGER ===")
print(pm_response)

print("\n\n=== ARCHITECT ===")
print(architect_response)

print("\n\n=== BACKEND DEVELOPER ===")
print(backend_response)