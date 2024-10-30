from unittest import TestCase, main
from project.hero import Hero

class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Branko", 1, 100, 100)
        self.enemy = Hero("Adit", 1, 50, 50)

    def test_init(self):
        self.assertEqual("Branko", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_if_enemy_is_with_the_same_username(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_hero_health_is_less_than_or_zero(self):
        expected_result = "Your health is lower than or equal to 0. You need to rest"
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_result, str(ve.exception))

    def test_if_enemy_health_is_less_than_or_zero(self):
        expected_result = f"You cannot fight Adit. He needs to rest"
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_result, str(ve.exception))

    def test_battle_if_draw_and_if_both_heroes_health_decreases(self):
        self.hero.health = 50
        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(0, self.hero.health)

    def test_battle_if_hero_wins_and_updates_level_health_and_damage(self):
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)


    def test_battle_if_enemy_wins_and_if_it_updates_enemy_damage_health_level(self):
        self.hero, self.enemy = self.enemy, self.hero
        expected_level = self.enemy.level + 1
        expected_health = self.enemy.health - self.hero.damage + 5
        expected_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_str_method_return_message(self):
        expected_result = f"Hero Branko: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 100\n"

        self.assertEqual(expected_result, str(self.hero))


if __name__ == '__main__':
    main()