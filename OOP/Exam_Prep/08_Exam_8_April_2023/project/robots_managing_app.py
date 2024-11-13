from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot



class RobotsManagingApp:

    VALID_SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    VALID_ROBOT_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    ROBOT_SERVICES = {
        "SecondaryService": "FemaleRobot",
        "MainService": "MaleRobot"
    }

    def __init__(self):
        self.robots: list = []
        self.services: list = []


    def add_service(self, service_type: str, name: str) -> str:
        try:
            service = self.VALID_SERVICE_TYPES[service_type](name)
        except KeyError:
            raise Exception("Invalid service type!")

        self.services.append(service)
        return f"{service_type} is successfully added."


    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        try:
            robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        except KeyError:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)
        return f"{robot_type} is successfully added."


    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self.__get_robot(robot_name)
        service = self.__get_service(service_name)

        if robot.__class__.__name__ != self.ROBOT_SERVICES[service.__class__.__name__]:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."


    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = self.__get_service(service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."


    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self.__get_service(service_name)
        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."


    def service_price(self, service_name: str):
        service = self.__get_service(service_name)
        total_price = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."


    def __str__(self):
        return '\n'.join(s.details() for s in self.services)


    def __get_robot(self, robot_name: str):
        robots = [r for r in self.robots if r.name == robot_name]
        return robots[0] if robots else None


    def __get_service(self, service_name: str):
        services = [ s for s in self.services if s.name == service_name]
        return services[0] if services else None
