from agents.agent import Agent


class ProductManager(Agent):
    def __init__(self):
        super().__init__(
            name="Product Manager",
            role="Senior Product Manager",
            goal="Convert software ideas into clear requirements"
        )