from agents.agent import Agent
from config.agent_configs import PRODUCT_MANAGER


class ProductManager(Agent):
    def __init__(self):
        super().__init__(**PRODUCT_MANAGER)