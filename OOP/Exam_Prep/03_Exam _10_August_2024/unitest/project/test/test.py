from unittest import TestCase, main
from project.soccer_player import SoccerPlayer

class TestSoccerPlayer(TestCase):
    VALID_TEAMS = ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]

    def setUp(self):
        self.player = SoccerPlayer(
            "Tony Kross",
            30,
            10,
            "Real Madrid"
        )

    def test_init(self):
        self.assertEqual("Tony Kross", self.player.name)
        self.assertEqual(30, self.player.age)
        self.assertEqual(10, self.player.goals)
        self.assertEqual("Real Madrid", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_name_length_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Kros"

        self.assertEqual("Name should be more than 5 symbols!", str(ve.exception))

    def test_age_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 7

        self.assertEqual("Players must be at least 16 years of age!", str(ve.exception))

    def test_goals_value_if_below_zero_expect_zero(self):
        self.player.goals = -1
        self.assertEqual(0, self.player.goals,)

    def test_if_team_in_valid_teams_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.player.team = "Liverpool"

        self.assertEqual(
            f"Team must be one of the following: {', '.join(self.VALID_TEAMS)}!",
            str(ve.exception)
        )

    def test_change_team_with_invalid_team_expect_invalid_msg(self):
        result = self.player.change_team("Liverpool")

        self.assertEqual("Invalid team name!", result)

    def test_change_team_with_a_valid_team_expect_changed_team(self):
        result = self.player.change_team("PSG")

        self.assertEqual("PSG", self.player.team)
        self.assertEqual("Team successfully changed!", result)

    def test_add_new_achievement_with_new_achievement_expect_updated_dict_and_success_msg(self):
        result = self.player.add_new_achievement("League")

        self.assertEqual({"League": 1}, self.player.achievements)
        self.assertEqual(
            "League has been successfully added to the achievements collection!",
            result
        )

    def test_add_new_achievement_with_existing_achievement_expect_updated_dict_and_success_msg(self):
        self.player.achievements = {"League": 1}
        result = self.player.add_new_achievement("League")

        self.assertEqual({"League": 2}, self.player.achievements)
        self.assertEqual(
            "League has been successfully added to the achievements collection!",
            result
        )

    def test_compare_goals(self):
        player_more_goals = SoccerPlayer("Mira Mira", 30, 15, "PSG")
        player_less_goals = SoccerPlayer("Berbatov", 30, 3, "PSG")

        result = self.player.__lt__(player_more_goals)
        self.assertEqual(
            "Mira Mira is a top goal scorer! S/he scored more than Tony Kross.",
            result
        )

        result = self.player.__lt__(player_less_goals)
        self.assertEqual(
            "Tony Kross is a better goal scorer than Berbatov.",
            result
        )


if __name__ == '__main__':
    main()
