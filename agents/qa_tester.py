from agents.agent import Agent
from config.agent_configs import QA_TESTER


class QATester(Agent):
    def __init__(self):
        super().__init__(**QA_TESTER)