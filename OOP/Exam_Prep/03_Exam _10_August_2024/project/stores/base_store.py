from abc import ABC, abstractmethod


class BaseStore(ABC):
    ESTIMATED_PROFIT_PERCENT = 0.10

    def __init__(self,name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")

        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value) != 3 or " " in value:
            raise ValueError("Store location must be 3 chars long!")

        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")

        self.__capacity = value

    @property
    @abstractmethod
    def store_type(self):
        ...

    @abstractmethod
    def store_stats(self):
        ...

    @abstractmethod
    def get_products_message(self) -> str:
        ...

    @abstractmethod
    def get_product_count(self, model) -> int:
        ...

    @abstractmethod
    def get_average_price(self, model) -> float:
        ...

    @abstractmethod
    def get_unique_models(self):
        ...


    def get_estimated_profit(self) -> str:
        products_value = sum(p.price for p in self.products)
        estimated_profit = products_value * self. ESTIMATED_PROFIT_PERCENT

        return f"Estimated future profit for {len(self.products)} products is {estimated_profit:.2f}"
