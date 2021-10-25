import Time
import Temperature
import Screen

class World:

    def __init__(self, set_hours_in_day = 24, set_days_in_year = 360):
        self.screen = Screen.Screen()
        self.time = Time.Time(set_hours_in_day, set_days_in_year)
        self.temperature = Temperature.Temperature()
        self.time.attach(self.temperature)
        self.screen.attach(self.time)
        self.screen.attach(self.temperature)
        self.screen.attach(self.time)

    def tick(self):
        self.time.tick()

    def render(self, clock):
        self.screen.render(clock)
