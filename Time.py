import time

class Time:
    def __init__(self):
        self.current_time = 0  # Current time in minutes
        self.day_length = 12 * 60  # Length of day in minutes (12 hours)
        self.night_length = 12 * 60  # Length of night in minutes (12 hours)
        self.season = "Spring"  # Initial season
        self.year_length = 10  # Length of a year in real-time minutes

    def advance_time(self, minutes):
        self.current_time += minutes
        if self.current_time >= self.year_length:
            self.current_time %= self.year_length
            self.change_season()

    def change_season(self):
        seasons = ["Spring", "Summer", "Autumn", "Winter"]
        current_season_index = seasons.index(self.season)
        new_season_index = (current_season_index + 1) % len(seasons)
        self.season = seasons[new_season_index]

    def is_daytime(self):
        return 0 <= self.current_time < self.day_length

    def is_nighttime(self):
        return self.day_length <= self.current_time < self.day_length + self.night_length

    def get_lighting_intensity(self):
        # Calculate lighting intensity based on the current time
        if self.is_daytime():
            return 1.0  # Full daylight intensity
        elif self.is_nighttime():
            return 0.0  # Complete darkness
        else:
            # Twilight transitions
            twilight_start = self.day_length - 30  # 30 minutes before sunset
            twilight_end = self.day_length + 30  # 30 minutes after sunrise

            if twilight_start <= self.current_time < self.day_length:
                return 1.0 - ((self.current_time - twilight_start) / 30.0)  # Dimming during sunset
            elif self.day_length + self.night_length <= self.current_time < twilight_end:
                return (self.current_time - (self.day_length + self.night_length)) / 30.0  # Brightening during sunrise
            else:
                return 1.0  # Full daylight intensity

    def display_time(self):
        hours = self.current_time // 60
        minutes = self.current_time % 60
        return f"{hours:02d}:{minutes:02d}"
    def __str__(self):
        return f"Current Time: {self.display_time()}, Season: {self.season}, Lighting Intensity: {self.get_lighting_intensity():.2f}"


# Example usage:
time_manager = Time()

# Simulate real-time passage and display conditions every minute
for _ in range(10):
    time.sleep(60)  # Wait for 1 minute of real time
    time_manager.advance_time(1)  # Advance time by 1 minute
    print("Current time:", time_manager.display_time())
    print("Season:", time_manager.season)
    print("Lighting intensity:", time_manager.get_lighting_intensity())
    if time_manager.is_daytime():
        print("It's daytime.")
    elif time_manager.is_nighttime():
        print("It's nighttime.")
    print("-------------------")
