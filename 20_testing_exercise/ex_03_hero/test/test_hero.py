from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    username = "Test hero"
    level = 5
    health = 39.5
    damage = 15.3

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attribute_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_enemy_hero_with_same_name_raises_exception(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_not_enough(self):
        self.hero.health = 0
        enemy = Hero("Enemy", self.level, 100, self.damage)

        with self.assertRaises(ValueError) as er:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(er.exception))

        self.hero.health = -1

        with self.assertRaises(ValueError) as er2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(er2.exception))

    def test_enemy_health_not_enough(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)

        with self.assertRaises(ValueError) as er:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(er.exception))

        enemy.health = -1
        with self.assertRaises(ValueError) as er2:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(er2.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        result = self.hero.battle(enemy)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(-37.0, self.hero.health)
        self.assertEqual(15.3, self.hero.damage)
        self.assertEqual("Draw", result)

    def test_hero_win(self):
        enemy = Hero("Enemy", 1, 1, 1)
        result = self.hero.battle(enemy)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(43.5, self.hero.health)
        self.assertEqual(20.3, self.hero.damage)
        self.assertEqual("You win", result)

    def test_hero_lose(self):
        enemy = Hero("Enemy", 100, 100, 100)
        result = self.hero.battle(enemy)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(-9960.5, self.hero.health)
        self.assertEqual(15.3, self.hero.damage)
        self.assertEqual("You lose", result)

        self.assertEqual(101, enemy.level)
        self.assertEqual(28.5, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
                   f"Health: {self.health}\n" \
                   f"Damage: {self.damage}\n"
        self.assertEqual(expected, self.hero.__str__())


if __name__ == "__main__":
    main()
