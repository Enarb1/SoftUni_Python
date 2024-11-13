from unittest import TestCase, main
from project.tennis_player import TennisPlayer

class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Mira", 38, 100)
        self.player2 = TennisPlayer("Branko", 36, 150)

    def test_init(self):
        self.assertEqual("Mira",self.player.name)
        self.assertEqual(38, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)


    def test_name_with_less_than_3_symbols_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Mi"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))


    def test_age_with_age_less_than_18_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))


    def test_add_new_win_with_non_existing_tournament_expect_success(self):
        self.player.add_new_win("SofiaOpen")
        self.assertEqual(["SofiaOpen"], self.player.wins)

    def test_add_new_win_with_existing_tournament_expect_return_msg(self):
        self.player.wins = ["SofiaOpen"]
        result = self.player.add_new_win("SofiaOpen")

        self.assertEqual(
            "SofiaOpen has been already added to the list of wins!",
            result
        )


    def test_lt_method_with_less_points_than_other_player(self):
        result = self.player.__lt__(self.player2)
        self.assertEqual(
            "Branko is a top seeded player and he/she is better than Mira",
            result
        )


    def test_lt_method_with_more_points_than_other_player(self):
        self.player.points = 200
        result = self.player.__lt__(self.player2)

        self.assertEqual(
            'Mira is a better player than Branko',
            result
        )


    def test_str_method(self):
        self.player.wins = ["SofiaOpen", "BerlinOpen", "ParisOpen"]
        result = self.player.__str__()

        self.assertEqual("Tennis Player: Mira\n"
               "Age: 38\n"
               "Points: 100.0\n"
               "Tournaments won: SofiaOpen, BerlinOpen, ParisOpen",
                         result
                         )


if __name__ == '__main__':
    main()