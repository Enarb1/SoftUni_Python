import unittest

from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.auction_house_manager_app import AuctionHouseManagerApp
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class TestManagerMethod(unittest.TestCase):
    def setUp(self):
        self.manager = AuctionHouseManagerApp()

        self.museum1 = Museum(name="Louvre")
        self.museum1.available_money = 30_000.0
        self.museum1.available_space = 500

        self.museum2 = Museum(name="Metropolitan")
        self.museum2.available_money = 10_500.0
        self.museum2.available_space = 400

        self.private_collector1 = PrivateCollector(name="John Doe")
        self.private_collector1.available_money = 7_000.0
        self.private_collector1.available_space = 200

        self.private_collector2 = PrivateCollector(name="Jane Smith")
        self.private_collector2.available_money = 6_000.0
        self.private_collector2.available_space = 300

        self.ra1 = RenaissanceArtifact("Daphne", 10_000.0, 10)
        self.ca1 = ContemporaryArtifact("The Scream", 2_000.0, 100)
        self.ra2 = RenaissanceArtifact("Antique Vase", 1_400.0, 90)
        self.ca2 = ContemporaryArtifact("Golden Statue", 5_000.0, 20)
        self.ra3 = RenaissanceArtifact("Rome Vase", 2_400.0, 60)
        self.ca3 = ContemporaryArtifact("Z Statue", 3_000.0, 50)

        self.manager.artifacts.extend([self.ca1, self.ra2])

        self.museum1.purchased_artifacts.append(self.ra1)
        self.private_collector1.purchased_artifacts.append(self.ca2)

        self.manager.collectors.extend([self.museum1, self.museum2, self.private_collector1, self.private_collector2])

    def test_auction_report__one_collector_one_artifact(self):
        self.manager.artifacts = []
        self.manager.collectors = [self.museum1]
        self.museum1.purchased_artifacts = [self.ra1]

        result = self.manager.get_auction_report()
        expected_output = (
            """**Auction statistics**
Total number of sold artifacts: 1
Available artifacts for sale: 0
***
Collector name: Louvre; Money available: 30000.00; Space available: 500; Artifacts: Daphne"""
        )
        self.assertEqual(result.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()