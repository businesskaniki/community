from Time import Time  # Assuming Time class is defined in Time.py
import random
from Person import Person
from Location import Location
# Define the world
class World:
    def __init__(self):
        self.people = []
        self.locations = []
        self.time_manager = Time()  # Create an instance of the Time class

    def add_person(self, person):
        self.people.append(person)

    def add_location(self, location):
        self.locations.append(location)  # Add the location object to the locations list

    def populate(self, num_people):
        for _ in range(num_people):
            age = random.randint(18, 80)
            gender = random.choice(["male", "female"])
            social_class = random.choice(["low", "middle", "high"])
            person = Person(age=age, gender=gender, social_class=social_class)
            self.add_person(person)

    def __str__(self):
        result = "People in the world:\n"
        for person in self.people:
            result += str(person) + "\n"
        result += "\nLocations in the world:\n"
        for location in self.locations:
            result += str(location) + "\n"
        return result

    def advance_time(self, minutes):
        self.time_manager.advance_time(minutes)

# Example usage:
world = World()

# Create and add locations to the world
location1 = Location(
    location_type="City",
    size="Large",
    geography="Urban",
    population=1000000,
    government="City Council",
    history="Founded in 1800",
    function="Commercial and cultural center",
    accessibility="Accessible by road and public transportation",
    interactivity="Numerous shops, restaurants, and attractions",
    aesthetic="Skyscrapers and city skyline"
)
world.add_location(location1)

location2 = Location(
    location_type="Forest",
    size="Medium",
    geography="Wooded area",
    population=5000,
    government="None",
    history="Ancient forest",
    function="Natural habitat and recreation",
    accessibility="Trails and footpaths",
    interactivity="Wildlife observation and hiking",
    aesthetic="Tall trees and lush vegetation"
)
world.add_location(location2)

# Populate the world with people
world.populate(3)

# Print information about the world

# Advance time in the world by 1 minute
world.advance_time(1)
print(world)

