from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location,FurnitureStore.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return self.__class__.__name__

    def store_stats(self) -> str:

        return (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                f"{self.get_estimated_profit()}\n"
                f"**Furniture for sale:"
                f"\n{self.get_products_message()}")

    def get_products_message(self) -> str:
        product_details = [
            f"{model}: {self.get_product_count(model)}pcs, average price: {self.get_average_price(model):.2f}"
            for model in sorted(self.get_unique_models())
        ]

        return "\n".join(product_details)

    def get_product_count(self, model) -> int:
        return  len([p for p in self.products if p.model == model])

    def get_average_price(self, model) -> float:
        count = self.get_product_count(model)
        total_price = sum(p.price for p in self.products if p.model == model)

        return  total_price / count if count > 0 else 0

    def get_unique_models(self):
        return sorted({p.model for p in self.products})
