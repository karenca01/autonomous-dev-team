from agents.agent import Agent
from config.agent_configs import BACKEND_DEVELOPER


class BackendDeveloper(Agent):
    def __init__(self):
        super().__init__(**BACKEND_DEVELOPER)