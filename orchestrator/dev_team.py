from agents.product_manager import ProductManager
from agents.architect import Architect
from agents.backend_developer import BackendDeveloper
from agents.frontend_developer import FrontendDeveloper
from agents.qa_tester import QATester
from agents.tech_lead import TechLead
import time


class DevTeam:
    def __init__(self):
        self.product_manager = ProductManager()
        self.architect = Architect()
        self.backend_developer = BackendDeveloper()
        self.frontend_developer = FrontendDeveloper()
        self.qa_tester = QATester()
        self.tech_lead = TechLead()

    def run(self, idea):
        total_start = time.perf_counter()

        print("\nStarting Product Manager")
        start = time.perf_counter()
        pm_response = self.product_manager.think(idea)
        print(f"Product Manager section completed ({time.perf_counter() - start:.2f}s)")

        print("\nStarting Architect")
        start = time.perf_counter()
        architect_response = self.architect.think(pm_response)
        print(f"Architect section completed ({time.perf_counter() - start:.2f}s)")

        print("\nStarting Backend Developer")
        start = time.perf_counter()
        backend_response = self.backend_developer.think(architect_response)
        print(f"Backend Developer section completed ({time.perf_counter() - start:.2f}s)")

        print("\nStarting Frontend Developer")
        start = time.perf_counter()
        frontend_response = self.frontend_developer.think(backend_response)
        print(f"Frontend Developer section completed ({time.perf_counter() - start:.2f}s)")

        print("\nStarting QA Tester")
        start = time.perf_counter()
        qa_response = self.qa_tester.think(frontend_response)
        print(f"QA Tester section completed ({time.perf_counter() - start:.2f}s)")

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

        print("\nStarting Tech Lead")
        start = time.perf_counter()
        tech_lead_response = self.tech_lead.think(tech_lead_input)
        print(f"Tech Lead section completed ({time.perf_counter() - start:.2f}s)")

        print(f"\nTotal workflow time: {time.perf_counter() - total_start:.2f}s")

        return {
            "product_manager": pm_response,
            "architect": architect_response,
            "backend_developer": backend_response,
            "frontend_developer": frontend_response,
            "qa_tester": qa_response,
            "tech_lead": tech_lead_response,
        }