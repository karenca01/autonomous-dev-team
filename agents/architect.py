from agents.agent import Agent
from config.agent_configs import ARCHITECT


class Architect(Agent):
    def __init__(self):
        super().__init__(**ARCHITECT)