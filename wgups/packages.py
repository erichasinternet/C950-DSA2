class Package:
    # This method is called when an instance of the `Package` class is created.
    def __init__(
        self, package_id, address, city, state, area_code, time_limit, weight, status
    ):
        # Initialize the instance's attributes with the provided values.
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.area_code = area_code
        self.time_limit = time_limit
        self.weight = weight
        self.status = status
        self.depart_time = ""
        self.deliver_time = ""

    # This method is called when a string representation of the instance is needed,
    def __str__(self):
        # Return a string that contains the values of the instance's attributes.
        return f"{self.package_id}, {self.address}, {self.city}, {self.state}, {self.area_code}, {self.time_limit}, {self.weight}, {self.deliver_time}, {self.status}"

    # This method updates the status attribute of the instance based on the provided `datetime`.
    # The time complexity of this method is O(1) because it performs a constant number of operations.
    def update_status(self, datetime):
        # Update the status attribute based on the value of `datetime`.
        if self.deliver_time < datetime:
            self.status = "delivered"
        elif self.depart_time > datetime:
            self.status = "en route"
        else:
            self.status = "at the hub"
