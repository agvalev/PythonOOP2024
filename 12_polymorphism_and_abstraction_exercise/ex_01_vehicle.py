from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9  # air conditioner

    def drive(self, distance) -> None:
        fuel_needed = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6  # air conditioner
    FUEL_COEFFICIENT = 0.95

    def drive(self, distance) -> None:
        fuel_needed = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel) -> None:
        self.fuel_quantity += fuel * self.FUEL_COEFFICIENT


# ! Test Code
# -----------------------------------------------
# First Test


car = Car(20, 5)

car.drive(3)

print(car.fuel_quantity)

car.refuel(10)

print(car.fuel_quantity)

# ---------------------------------------------
# Second Test

truck = Truck(100, 15)

truck.drive(5)

print(truck.fuel_quantity)

truck.refuel(50)

print(truck.fuel_quantity)
