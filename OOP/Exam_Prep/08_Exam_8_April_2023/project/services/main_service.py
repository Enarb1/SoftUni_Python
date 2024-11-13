from project.services.base_service import BaseService


class MainService(BaseService):
    SERVICE_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.SERVICE_CAPACITY)


    def details(self):
        return f"""{self.name} Main Service:
Robots: {self._get_robots()}"""