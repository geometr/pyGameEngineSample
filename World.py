import Time
import Temperature

class World:
    def __init__(self, set_hours_in_day = 24, set_days_in_year = 360):
        self.time = Time.Time(set_hours_in_day, set_days_in_year)
        self.temperature = Temperature.Temperature()
        self.time.attach(self.temperature)
    def tick(self):
        self.time.tick()


