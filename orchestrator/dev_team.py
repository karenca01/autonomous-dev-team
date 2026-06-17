from agents.product_manager import ProductManager
from agents.architect import Architect
from agents.backend_developer import BackendDeveloper
from agents.frontend_developer import FrontendDeveloper
from agents.qa_tester import QATester
from agents.tech_lead import TechLead


class DevTeam:
    def __init__(self):
        self.product_manager = ProductManager()
        self.architect = Architect()
        self.backend_developer = BackendDeveloper()
        self.frontend_developer = FrontendDeveloper()
        self.qa_tester = QATester()
        self.tech_lead = TechLead()

    def run(self, idea):
        pm_response = self.product_manager.think(idea)
        architect_response = self.architect.think(pm_response)
        backend_response = self.backend_developer.think(architect_response)
        frontend_response = self.frontend_developer.think(backend_response)
        qa_response = self.qa_tester.think(frontend_response)

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

        tech_lead_response = self.tech_lead.think(tech_lead_input)

        return {
            "product_manager": pm_response,
            "architect": architect_response,
            "backend_developer": backend_response,
            "frontend_developer": frontend_response,
            "qa_tester": qa_response,
            "tech_lead": tech_lead_response,
        }