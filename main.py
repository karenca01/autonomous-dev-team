from agents.product_manager import ProductManager
from agents.architect import Architect
from agents.backend_developer import BackendDeveloper
from agents.frontend_developer import FrontendDeveloper
from agents.qa_tester import QATester
from agents.tech_lead import TechLead


idea = """
I want an application to track personal habits.
"""


product_manager = ProductManager()
architect = Architect()
backend_developer = BackendDeveloper()
frontend_developer = FrontendDeveloper()
qa_tester = QATester()
tech_lead = TechLead()


pm_response = product_manager.think(idea)
architect_response = architect.think(pm_response)
backend_response = backend_developer.think(architect_response)
frontend_response = frontend_developer.think(backend_response)
qa_response = qa_tester.think(frontend_response)

# contexto distinto porque tiene que analizar distintos elementos
tech_lead_input = f"""
=== REQUIREMENTS ===
{pm_response}

=== ARCHITECTURE ===
{architect_response}

=== BACKEND ===
{backend_response}

=== FRONTEND ===
{frontend_response}

=== QA FINDINGS ===
{qa_response}
"""

tech_lead_response = tech_lead.think(
    tech_lead_input
)


print("=== PRODUCT MANAGER ===")
print(pm_response)

print("\n\n=== ARCHITECT ===")
print(architect_response)

print("\n\n=== BACKEND DEVELOPER ===")
print(backend_response)

print("\n\n=== FRONTEND DEVELOPER ===")
print(frontend_response)

print("\n\n=== QA TESTER ===")
print(qa_response)

print("\n\n=== TECH LEAD ===")
print(tech_lead_response)