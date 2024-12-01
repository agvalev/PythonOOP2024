from project.mammal import Mammal

from unittest import TestCase, main


class MammalTest(TestCase):

    def setUp(self):
        self.mammal = Mammal("Test", "Test type", "test sound")

    def test_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Test type", self.mammal.type)
        self.assertEqual("test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        expected = f"Test makes test sound"
        self.assertEqual(expected, result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        self.assertEqual(f"Test is of type Test type", self.mammal.info())


if __name__ == "__main__":
    main()
