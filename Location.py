import random


class Location:
    def __init__(
        self,
        location_type,
        size,
        geography,
        population,
        government,
        history,
        function,
        accessibility,
        interactivity,
        aesthetic,
        name=None,
    ):
        self.name = name if name else self.generate_unique_location_name()
        self.location_type = (
            location_type
            if location_type
            else random.choice(
                [
                    "City",
                    "Town",
                    "Village",
                    "Forest",
                    "Mountain",
                    "Lake",
                    "River",
                    "Cave",
                ]
            )
        )
        self.size = size
        self.geography = geography
        self.population = population
        self.government = government
        self.history = history
        self.function = function
        self.accessibility = accessibility
        self.interactivity = interactivity
        self.aesthetic = aesthetic

    @staticmethod
    def generate_unique_location_name():
        potential_names = [
            "Oakvale",
            "Rivertown",
            "Windsong",
            "Brightwood",
            "Evergreen",
            "Stonehaven",
            "Silverlake",
            "Sunset Ridge",
            "Frostholm",
            "Moonshadow",
            "Emberfall",
            "Starglade",
        ]
        name = random.choice(potential_names)
        potential_names.remove(name)  # Remove the chosen name from potential_names
        return name
    
    def __str__(self):
        description = f"Location: {self.name}\n"
        description += f"Type: {self.location_type}\n"
        description += f"Size: {self.size}\n"
        description += f"Geography: {self.geography}\n"
        description += f"Population: {self.population}\n"
        description += f"Government: {self.government}\n"
        description += f"History: {self.history}\n"
        description += f"Function: {self.function}\n"
        description += f"Accessibility: {self.accessibility}\n"
        description += f"Interactivity: {self.interactivity}\n"
        description += f"Aesthetic: {self.aesthetic}\n"
        return description

