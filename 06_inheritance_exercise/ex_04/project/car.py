from project.vehicle import Vehicle


class Car(Vehicle):
    pass


c = Car(10, 10)
print(c.DEFAULT_FUEL_CONSUMPTION)

