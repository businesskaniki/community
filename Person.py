import random


class Person:
    def __init__(
        self,
        age=0,
        name=None,
        gender=None,
        occupation=None,
        religion=None,
        education=None,
        hobbies=None,
        social_class=None,
        health=100,
        relationship_status="Not married",
        goals=None,
        location=None,
    ):
        self.age = age
        self.gender = gender if gender else random.choice(["male", "female"])
        self.social_class = social_class if social_class else random.choice(["low","high","middle"])
        self.name = name if name else self.generate_name(self.gender)
        self.occupation = occupation if occupation else self.generate_occupation()
        self.religion = (
            religion
            if religion
            else random.choice(
                ["Christianity", "Islam", "Hinduism", "Buddhism", "Judaism"]
            )
        )
        self.education = (
            education if education else self.generate_education(self.social_class)
        )
        self.hobbies = (
            hobbies
            if hobbies
            else random.choice(["Reading", "Sports", "Music", "Cooking", "Traveling"])
        )
        self.health = health
        self.relationship_status = relationship_status
        self.goals = goals
        self.location = location


    def generate_name(self, gender):
        # Define lists of male and female names
        male_names = [
            "James",
            "John",
            "Robert",
            "Michael",
            "William",
            "David",
            "Richard",
            "Joseph",
            "Charles",
            "Thomas",
            "Daniel",
            "Matthew",
            "Anthony",
            "Mark",
            "Paul",
            "Steven",
            "Andrew",
            "Kenneth",
            "Joshua",
            "Kevin",
        ]
        female_names = [
            "Mary",
            "Patricia",
            "Jennifer",
            "Linda",
            "Elizabeth",
            "Barbara",
            "Susan",
            "Jessica",
            "Sarah",
            "Karen",
            "Nancy",
            "Lisa",
            "Margaret",
            "Betty",
            "Dorothy",
            "Sandra",
            "Ashley",
            "Kimberly",
            "Emily",
            "Donna",
        ]

        if gender == "male":
            return random.choice(male_names)
        elif gender == "female":
            return random.choice(female_names)

    def generate_occupation(self):
        male_occupations = [
            "Engineer",
            "Doctor",
            "Pilot",
            "Software Developer",
            "Electrician",
        ]
        female_occupations = [
            "Nurse",
            "Teacher",
            "Graphic Designer",
            "Social Worker",
            "Chef",
        ]

        if self.gender == "male":
            return random.choice(male_occupations)
        elif self.gender == "female":
            return random.choice(female_occupations)


    def generate_education(self, social_class):
    # Define education levels for each social class with their respective probabilities
        education_levels = {
            "low": [("Primary School", 0.5), ("Secondary School", 0.3), ("No Formal Education", 0.2)],
            "middle": [("High School Diploma", 0.4), ("Associate Degree", 0.3), ("Bachelor's Degree", 0.2), ("Master's Degree", 0.05), ("PhD", 0.05)],
            "high": [("Bachelor's Degree", 0.3), ("Master's Degree", 0.4), ("PhD", 0.2), ("Professional Degree", 0.1)]
        }

        # Adjust probabilities based on social class
        if social_class == "low":
            # Lower social class individuals have a higher chance of having lower education levels
            return self.select_education_level(education_levels["low"])
        elif social_class == "middle":
            # Middle social class individuals have a more balanced distribution of education levels
            return self.select_education_level(education_levels["middle"])
        elif social_class == "high":
            # Higher social class individuals have a higher chance of having higher education levels
            return self.select_education_level(education_levels["high"])

    def select_education_level(self, education_levels):
        # Randomly select an education level based on the defined probabilities
        education_level = random.choices([level[0] for level in education_levels], [level[1] for level in education_levels])[0]
        return education_level

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Occupation: {self.occupation}, Religion: {self.religion}, Education: {self.education}, Hobbies: {self.hobbies}, Social Class: {self.social_class}, Health: {self.health}, Relationship Status: {self.relationship_status}, Goals: {self.goals}, Location: {self.location}"


# Example usage:
person1 = Person(age=30)
person2 = Person()
print(person2)
