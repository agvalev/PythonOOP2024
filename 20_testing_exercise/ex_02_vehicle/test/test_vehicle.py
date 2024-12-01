from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):
    Fuel = 3.5
    Horse_power = 100.

    def setUp(self):
        self.test_vehicle = Vehicle(self.Fuel, self.Horse_power)

    def test_init(self):
        self.assertEqual(self.Fuel, self.test_vehicle.fuel)
        self.assertEqual(self.Fuel, self.test_vehicle.capacity)
        self.assertEqual(self.Horse_power, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)
        self.assertIsInstance(self.test_vehicle.DEFAULT_FUEL_CONSUMPTION, float)

    def test_drive_success(self):
        self.test_vehicle.drive(2)
        self.assertEqual(1, self.test_vehicle.fuel)

    def test_drive_error(self):
        with self.assertRaises(Exception)as ex:
            self.test_vehicle.drive(5)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_success(self):
        self.test_vehicle.fuel = 1
        self.test_vehicle.refuel(1.2)
        self.assertEqual(2.2, self.test_vehicle.fuel)

    def test_refuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(9)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected = "The vehicle has 100.0 horse power with 3.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, self.test_vehicle.__str__())


if __name__ == "__main__":
    main()
