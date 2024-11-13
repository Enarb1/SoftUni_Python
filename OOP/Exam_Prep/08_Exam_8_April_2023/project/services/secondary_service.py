from project.services.base_service import BaseService


class SecondaryService(BaseService):
    SERVICE_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.SERVICE_CAPACITY)


    def details(self):
        return f"""{self.name} Secondary Service:
Robots: {self._get_robots()}"""