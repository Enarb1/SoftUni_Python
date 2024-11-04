from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore
from project.stores.base_store import BaseStore
from project.products.base_product import BaseProduct



class FactoryManager:

    VALID_PRODUCT_TYPES = {
        "Chair": Chair,
        "HobbyHorse": HobbyHorse,
    }

    VALID_STORE_TYPES =  {
        "FurnitureStore": FurnitureStore,
        "ToyStore": ToyStore,
    }

    VALID_SUB_TYPES = {
        "FurnitureStore": "Furniture",
        "ToyStore": "Toys"
    }


    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list = []
        self.stores: list = []

    @staticmethod
    def decrease_store_capacity(store: BaseStore, products_count: int):
        store.capacity -= products_count

    @staticmethod
    def calculate_income(*products: BaseProduct):
        return sum(p.price for p in products)

    @staticmethod
    def stock_store_products(store: BaseStore, *products: BaseProduct):
        for p in products:
            store.products.append(p)


    def produce_item(self, product_type: str, model: str, price: float) -> str:
        try:
            product = self.VALID_PRODUCT_TYPES[product_type](model, price)
        except KeyError:
            raise Exception("Invalid product type!")

        self.products.append(product)

        return f"A product of sub-type {product.sub_type} was produced."


    def register_new_store(self, store_type: str, name: str, location: str):
        try:
            store = self.VALID_STORE_TYPES[store_type](name, location)
        except KeyError:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(store)

        return f"A new {store_type} was successfully registered."


    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        valid_type = store.store_type
        valid_subtype = self.VALID_SUB_TYPES.get(valid_type)
        products_for_purchase = [p for p in products if p.sub_type == valid_subtype]

        if len(products_for_purchase) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        if not products_for_purchase:
            return "Products do not match in type. Nothing sold."

        self.remove_products(*products_for_purchase)
        self.stock_store_products(store, *products_for_purchase)
        self.decrease_store_capacity(store, len(products_for_purchase))
        self.income += self.calculate_income(*products_for_purchase)

        return f"Store {store.name} successfully purchased {len(products_for_purchase)} items."


    def remove_products(self, *products: BaseProduct):
         for p in products:
             self.products.remove(p)


    def unregister_store(self, store_name: str):
        try:
            store =  next(filter(lambda s: s.name == store_name, self.stores))
        except StopIteration:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."


    def discount_products(self, product_model: str):
        products_for_discount = list(filter(lambda p: p.model == product_model, self.products))

        for product in products_for_discount:
            product.discount()

        return f"Discount applied to {len(products_for_discount)} products with model: {product_model}"


    def request_store_stats(self, store_name: str):
        try:
            store = next(filter(lambda s: s.name == store_name, self.stores))
        except StopIteration:
            return "There is no store registered under this name!"

        return store.store_stats()


    def statistics(self):
        return (f"Factory: {self.name}\n"
                f"Income: {self.income:.2f}\n"
                f"***Products Statistics***\n"
                f"Unsold Products: {len(self.products)}. Total net price: {self.get_unsold_products_value():.2f}\n"
                + self.get_products_message() +
                f"\n***Partner Stores: {len(self.stores)}***\n"
                + "\n".join(self.get_sorted_stores())
                )


    def get_unsold_products_value(self):
        return sum([p.price for p in self.products])

    def get_product_count(self, model):
        return len([p for p in self.products if p.model == model])

    def get_unique_models(self):
        return sorted({p.model for p in self.products})

    def get_products_message(self):
        product_details = [
            f"{model}: {self.get_product_count(model)}" for model in sorted(self.get_unique_models())
        ]

        return "\n".join(product_details)

    def get_sorted_stores(self):
        stores_to_sort = [s.name for s in self.stores]

        return  sorted(stores_to_sort)


