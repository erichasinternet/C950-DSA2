class Truck:
    # This method is called when an instance of the `Truck` class is created.
    def __init__(self, address, capacity, depart_time, load, mileage, packages, speed):
        self.address = address
        self.capacity = capacity
        self.depart_time = depart_time
        self.load = load
        self.mileage = mileage
        self.packages = packages
        self.speed = speed
        self.time = depart_time

    # This method is called when a string representation of the instance is needed.
    def __str__(self):
        # Return a string that contains the values of the instance's attributes.
        return f"{self.address}, {self.capacity}, {self.depart_time}, {self.load}, {self.mileage}, {self.packages}, {self.speed}"
