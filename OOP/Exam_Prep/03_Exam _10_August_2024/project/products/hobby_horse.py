from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    DISCOUNT = 0.20
    def __init__(self, model: str, price: float):
        super().__init__(model, price, "Wood/Plastic", "Toys")

    def discount(self):
        self.price -= self.price * self.DISCOUNT