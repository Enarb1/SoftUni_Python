from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:

    VALID_ARTIFACT_TYPE = {
        "RenaissanceArtifact": RenaissanceArtifact,
        "ContemporaryArtifact": ContemporaryArtifact
    }

    VALID_COLLECTOR_TYPE = {
        "Museum": Museum,
        "PrivateCollector": PrivateCollector
    }

    def __init__(self):
        self.artifacts: list = []
        self.collectors: list = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.VALID_ARTIFACT_TYPE.keys():
            raise ValueError("Unknown artifact type!")
        if self.__get_artifact_by_name(artifact_name) is not None:
            raise ValueError(f"{artifact_name} has been already registered!")
        artifact = self.VALID_ARTIFACT_TYPE[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(artifact)
        return f"{artifact.name} is successfully added to the auction as {artifact.__class__.__name__}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.VALID_COLLECTOR_TYPE.keys():
            raise ValueError("Unknown collector type!")
        if self.__get_collector_by_name(collector_name) is not None:
            raise ValueError(f"{collector_name} has been already registered!")
        collector = self.VALID_COLLECTOR_TYPE[collector_type](collector_name)
        self.collectors.append(collector)
        return f"{collector.name} is successfully registered as a {collector.__class__.__name__}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = self.__get_collector_by_name(collector_name)
        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        artifact = self.__get_artifact_by_name(artifact_name)
        if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
        if collector.can_purchase(artifact.price, artifact.space_required):
            collector.purchased_artifacts.append(artifact)
            collector.available_money -= artifact.price
            collector.available_space -= artifact.space_required
            self.artifacts.remove(artifact)
            return f"{collector.name} purchased {artifact.name} for a price of {artifact.price:.2f}."
        return "Purchase is impossible."

    def remove_artifact(self, artifact_name: str):
        artifact = self.__get_artifact_by_name(artifact_name)
        if artifact is None:
            return "No such artifact."
        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        count = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                count += 1
        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        result = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {self.__get_sold_artifacts()}",
            f"Available artifacts for sale: {len(self.artifacts)}",
            "***"
        ]
        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts),c.name))
        if self.collectors:
            for collector in sorted_collectors:
                result.append(str(collector))
        return "\n".join(result)

    def __get_collector_by_name(self, name):
        return next((c for c in self.collectors if c.name == name), None)

    def __get_artifact_by_name(self, name):
        return next((a for a in self.artifacts if a.name == name), None)

    def __get_sold_artifacts(self):
        return sum(len(c.purchased_artifacts) for c in self.collectors)
