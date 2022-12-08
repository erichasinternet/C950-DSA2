# Created by: Eric Lawson
# Student ID: 001009860
# The time complexity of this entire program is O(n^2)
import csv
import datetime
import trucks
from builtins import ValueError
from hashtable import HashMap
from packages import Package

with open("data/address.csv", mode="r+", encoding="utf-8-sig") as address_csv:
    # Read the address data from the address.csv file
    address_data = csv.reader(address_csv)
    # Convert the address data to a list
    address_data = list(address_data)

with open("data/distance.csv", mode="r+", encoding="utf-8-sig") as distance_csv:
    # Read the distance data from the distance.csv file
    distance_data = csv.reader(distance_csv)
    # Convert the distance data to a list
    distance_data = list(distance_data)

# Initialize an empty list to hold the package data
package_array = []

with open("data/packages.csv", mode="r", encoding="utf-8-sig") as packages_csv:
    # Read the package data from the packages.csv file
    package_data = csv.reader(packages_csv)
    # Convert the package data to a list
    package_array = list(package_data)

# This function parses the package data and inserts it into a hash map.
# The time complexity of this function is O(n)
def get_package_data(csv, hash_map):
    # Iterate over each package in the package data list
    for package in package_array:
        # Parse the data for each package
        package_id = int(package[0])
        package_address = package[1]
        package_city = package[2]
        package_state = package[3]
        package_area_code = package[4]
        package_time_limit = package[5]
        package_weight = package[6]
        package_status = "at the hub"

        # Create a Package object with the parsed data
        package_object = Package(
            package_id,
            package_address,
            package_city,
            package_state,
            package_area_code,
            package_time_limit,
            package_weight,
            package_status,
        )

        # Insert the Package object into the hash map
        hash_map.insert(package_id, package_object)


# This function calculates the distance between two locations.
# The time complexity of this function is O(1)
def trip_distance(x_value, y_value):
    # Check if the distance from x_value to y_value is defined
    trip_distance = distance_data[x_value][y_value]

    # If the distance is not defined, check if the distance from
    # y_value to x_value is defined
    if not trip_distance:
        trip_distance = distance_data[y_value][x_value]

    # Convert the distance string to a float and return it
    return float(trip_distance)


# The time complexity of this function is O(n)
def get_address(address):
    # Loop through all rows in the address data
    for row in address_data:
        # Check if the address is in the current row
        if address in row[2]:
            # Return the first column (index 0) of the current row as an integer
            return int(row[0])


# Define the WGU address
wgu_address = "4001 South 700 East"

# Create the first truck
truck_1 = trucks.Truck(
    wgu_address,  # Set the address
    16,  # Set the maximum packages that the truck can carry
    datetime.timedelta(hours=8),  # Set the time required to load the truck
    None,  # Set the current location of the truck
    0.0,  # Set the current mileage of the truck
    [
        1,
        13,
        14,
        15,
        16,
        20,
        29,
        30,
        31,
        34,
        37,
        40,
    ],  # Set the packages to be delivered by the truck
    18,  # Set the speed of the truck in mph
)

# Create the second truck
truck_2 = trucks.Truck(
    wgu_address,  # Set the address
    16,  # Set the maximum packages that the truck can carry
    datetime.timedelta(hours=10, minutes=20),  # Set the time required to load the truck
    None,  # Set the current location of the truck
    0.0,  # Set the current mileage of the truck
    [
        3,
        6,
        12,
        17,
        18,
        19,
        21,
        22,
        23,
        24,
        26,
        27,
        35,
        36,
        38,
        39,
    ],  # Set the packages to be delivered by the truck
    18,  # Set the speed of the truck in mph
)

# Create the third truck
truck_3 = trucks.Truck(
    wgu_address,  # Set the address
    16,  # Set the maximum packages that the truck can carry
    datetime.timedelta(hours=9, minutes=5),  # Set the time required to load the truck
    None,  # Set the current location of the truck
    0.0,  # Set the current mileage of the truck
    [
        2,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        25,
        28,
        32,
        33,
    ],  # Set the packages to be delivered by the truck
    18,  # Set the speed of the truck in mph
)

# Create a new hash map
hash_map = HashMap()

# Get the package data from the specified file and store it in the hash map
get_package_data("data/packages.csv", hash_map)

# The time complexity of this function is O(n^2), because it
# iterates over all packages in the truck and then calls the trip_distance function on each package
def deliver(trucks):
    # Create a list of undelivered packages
    undelivered = [hash_map.get(package_id) for package_id in trucks.packages]
    # Clear the list of packages in the truck
    trucks.packages.clear()

    # Continue delivering packages until the list of undelivered packages is empty
    while undelivered:
        # Find the next package to deliver, which is the one closest to the truck's current address
        next_package = min(
            undelivered,
            key=lambda p: trip_distance(
                get_address(trucks.address), get_address(p.address)
            ),
        )
        # Add the package to the list of packages in the truck
        trucks.packages.append(next_package.package_id)
        # Remove the package from the list of undelivered packages
        undelivered.remove(next_package)

        # Calculate the distance and time to the next package
        distance = trip_distance(
            get_address(trucks.address), get_address(next_package.address)
        )
        time = datetime.timedelta(hours=distance / 18)

        # Update the truck's mileage, address, and time
        trucks.mileage += distance
        trucks.address = next_package.address
        trucks.time += time

        # Update the delivery time and departure time of the package
        next_package.deliver_time = trucks.time
        next_package.depart_time = trucks.depart_time


# Deliver packages with truck 1
deliver(truck_1)

# Deliver packages with truck 2
deliver(truck_2)

# Set the departure time of truck 3 to the minimum of the delivery times of truck 1 and truck 2
truck_3.depart_time = min(truck_1.time, truck_2.time)

# Deliver packages with truck 3
deliver(truck_3)

# Time complexity: O(n) average case
# Time complexity: O(n^2) worst case
class Main:
    # Define a string to display when the user inputs an invalid value
    invalid_input = "Error! Invalid input, exiting the program..."

    # Display the program banner
    print(
        r"""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
████████╗ ██████╗                                             
╚══██╔══╝██╔═══██╗                                            
   ██║   ██║   ██║                                            
   ██║   ██║   ██║                                            
   ██║   ╚██████╔╝                                            
   ╚═╝    ╚═════╝                                             
██╗    ██╗ ██████╗ ██╗   ██╗██████╗ ███████╗██╗               
██║    ██║██╔════╝ ██║   ██║██╔══██╗██╔════╝██║               
██║ █╗ ██║██║  ███╗██║   ██║██████╔╝███████╗██║               
██║███╗██║██║   ██║██║   ██║██╔═══╝ ╚════██║╚═╝               
╚███╔███╔╝╚██████╔╝╚██████╔╝██║     ███████║██╗               
 ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚═╝                                                                                                                                                                                                    
    """
    )

    # Calculate the total route distance
    total_distance = truck_1.mileage + truck_2.mileage + truck_3.mileage

    # Display the total route distance
    print("The total route distance is:", total_distance, "miles")

    # Ask the user to type "start" to begin
    text = input("Type `start` to begin.\n")

    # If the user didn't type "start", print the error message and exit the program
    if text != "start":
        print(invalid_input)
        exit()

    # Ask the user to input the time for the report in the format: HOURS:MINUTES:SECONDS
    time_input = input(
        "Please provide a time for the report in the following format: HOURS:MINUTES:SECONDS\n"
    )

    # Try to split the time input into hours, minutes, and seconds and convert it to a timedelta object
    try:
        (hours, minutes, seconds) = time_input.split(":")
        datetime = datetime.timedelta(
            hours=int(hours), minutes=int(minutes), seconds=int(seconds)
        )
    # If the user didn't provide the time in the correct format, print the error message and exit the program
    except ValueError:
        print(invalid_input)
        exit()

    # Ask the user if they want to generate a report for all packages or just an individual package
    package_type_input = input(
        "Type `all` to generate a report for all the packages.\nType `one` to generate a report for an individual package.\n"
    )

    # Set the initial package ID range to iterate over
    package_id_range = range(1, 41)

    # If the user wants to generate a report for an individual package:
    if package_type_input == "one":
        # Ask the user to provide the package id
        solo_input = input("Please enter the package_id\n")
        package_id_range = [int(solo_input)]

    # Try to look up the packages and update their statuses
    try:
        for packageID in package_id_range:
            package = hash_map.get(packageID)
            package.update_status(datetime)
            print(str(package))
    # If there is an error, print the error message and exit the program
    except ValueError:
        print(invalid_input)
        exit()
