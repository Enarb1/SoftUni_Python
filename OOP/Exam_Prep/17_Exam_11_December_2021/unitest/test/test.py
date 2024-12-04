from unittest import TestCase, main
from project.team import Team

class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Branko")
        self.other_team = Team("Adit")

    def test_init(self):
        self.assertEqual("Branko", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Br1nk0"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member(self):
        result = self.team.add_member(Branko=18, Mira=20)

        self.assertEqual({"Branko": 18, "Mira": 20}, self.team.members)
        self.assertEqual("Successfully added: Branko, Mira", result)

    def test_add_member_with_duplicate_member(self):
        self.team.members = {"Branko": 18}
        self.team.add_member(Branko=20)

        self.assertEqual({"Branko": 18}, self.team.members)

    def test_remove_members(self):
        self.team.members = {"Branko": 18, "Mira": 20}
        result = self.team.remove_member("Branko")

        self.assertEqual({"Mira": 20}, self.team.members)
        self.assertEqual("Member Branko removed", result)

    def test_remove_member_with_invalid_name(self):
        self.team.members = {"Branko": 18, "Mira": 20}
        result = self.team.remove_member("Adit")

        self.assertEqual({"Branko": 18, "Mira": 20}, self.team.members)
        self.assertEqual("Member with name Adit does not exist", result)

    def test_gt_with_bigger_len(self):
        self.team.add_member(Branko=18, Mira=20)
        self.other_team.add_member(Adit=15)

        self.assertTrue(self.team > self.other_team)

    def test_gt_with_smaller_len(self):
        self.team.add_member(Branko=18)
        self.other_team.add_member(Adit=15, Mira=20)

        self.assertFalse(self.team > self.other_team)

    def test_gt_with_equal_len(self):
        self.team.add_member(Branko=18)
        self.other_team.add_member(Mira=20)

        self.assertFalse(self.team > self.other_team)

    def test_len_method(self):
        self.team.add_member(Branko=18, Mira=20)
        self.assertEqual(2, len(self.team))

    def test_gt_with_len_team_members_true(self):
        self.team.add_member(Branko=18, Mira=20)
        self.other_team.add_member(Adit=15)
        result = self.team > self.other_team

        self.assertEqual(True, result)
        self.assertTrue(len(self.team.members) > len(self.other_team.members))

    def test_gt_with_len_team_members_false(self):
        self.team.add_member(Branko=18)
        self.other_team.add_member(Adit=15, Mira=20)
        result = self.team > self.other_team

        self.assertEqual(False, result)
        self.assertTrue(len(self.team.members) <= len(self.other_team.members))

    def test_add_method(self):
        self.team.add_member(Branko=18, Mira=20)
        self.other_team.add_member(Adit=15)

        new_team = self.team + self.other_team
        self.assertEqual("BrankoAdit", new_team.name)

        expected_members = {
            "Branko": 18,
            "Mira": 20,
            "Adit": 15
        }
        self.assertEqual(expected_members, new_team.members)

        self.assertEqual("Branko", self.team.name)
        self.assertEqual({"Branko": 18, "Mira": 20}, self.team.members)
        self.assertEqual("Adit", self.other_team.name)
        self.assertEqual({"Adit": 15}, self.other_team.members)

    def test_str_method(self):
        self.team.add_member(Branko=20, Mira=20, Adit=15)
        expected = ("Team name: Branko\n"
                    "Member: Branko - 20-years old\n"
                    "Member: Mira - 20-years old\n"
                    "Member: Adit - 15-years old")

        self.assertEqual(expected, str(self.team))

    def test_sorting(self):
        self.team.add_member(Zane=20, Branko=20, Mira=25)
        expected = ("Team name: Branko\n"
                    "Member: Mira - 25-years old\n"
                    "Member: Branko - 20-years old\n"
                    "Member: Zane - 20-years old")

        self.assertEqual(expected, str(self.team))


if __name__ == '__main__':
    main()