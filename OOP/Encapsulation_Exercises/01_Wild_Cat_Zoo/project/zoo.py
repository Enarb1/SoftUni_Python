from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price:
            if self.__animal_capacity > len(self.animals):
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough space for animal"
        return "Not enough budget"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        money_needed = sum([s.salary for s in self.workers])

        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        money_needed_for_animals = sum([m.money_for_care for m in self.animals])

        if money_needed_for_animals <= self.__budget:
            self.__budget -= money_needed_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"

        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"

        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self) -> str:
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"

        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"

        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += f"{vet}\n"

        return result[:-1]


