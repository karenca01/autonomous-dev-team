from agents.agent import Agent
from config.agent_configs import FRONTEND_DEVELOPER


class FrontendDeveloper(Agent):
    def __init__(self):
        super().__init__(**FRONTEND_DEVELOPER)