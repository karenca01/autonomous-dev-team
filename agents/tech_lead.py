from agents.agent import Agent
from config.agent_configs import TECH_LEAD


class TechLead(Agent):
    def __init__(self):
        super().__init__(**TECH_LEAD)