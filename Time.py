import Temperature

class Time:
    hours_in_day = 24
    days_in_year = 360
    current_hour = 0
    times_of_day = ""
    current_day = 0
    current_year = 0

    morning_begins = 0.0
    day_begins = 0.0
    evening_begins = 0.0
    night_begins = 0.0

    delta_times_of_day = 0.0
    delta_day = 0.0
    _observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notifyDayChanged(self, *args):
        for observer in self._observers:
            observer.notifyDayChanged(*args)

    def notifyTimesChanged(self, *args):
        for observer in self._observers:
            observer.notifyTimesChanged(*args)

    def __init__(self, set_hours_in_day = 24, set_days_in_year = 360):
        self.hours_in_day = set_hours_in_day
        self.days_in_year = set_days_in_year
        self.delta_times_of_day = self.hours_in_day/4
        self.updateTimingBegins()

    def updateTimingBegins(self):
        self.delta_day = -16 / self.days_in_year **2 * (self.current_day-self.days_in_year/2)**2 + 2
        self.morning_begins = self.delta_times_of_day - self.delta_day - self.delta_times_of_day / 2
        self.day_begins = self.morning_begins + self.delta_times_of_day
        self.evening_begins = self.day_begins + self.delta_times_of_day + self.delta_day
        self.night_begins = self.evening_begins + self.delta_times_of_day

    def getStepsInCentury(self):
        return self.getStepsInYear()*self.years_in_century

    def getStepsInYear(self):
        return self.hours_in_day*self.days_in_year

    def tick(self):
        self.current_hour = self.current_hour + 1
        if self.current_hour==self.hours_in_day:
            self.current_hour = 0
            self.current_day = self.current_day + 1
            self.notifyDayChanged(self.current_day, self.days_in_year)
            self.updateTimingBegins()

        if self.current_day==self.days_in_year:
            self.current_day = 0
            self.current_year = self.current_year + 1
        self.calculateTimesOfDay()

    def calculateTimesOfDay(self):
        if (self.current_hour<self.morning_begins):
            self.nightWorld()
        elif (self.current_hour<self.day_begins):
            self.morningWorld()
        elif (self.current_hour<self.evening_begins):
            self.dayWorld();
        elif (self.current_hour<self.night_begins):
            self.eveningWorld()
        else:
            self.nightWorld()
        self.notifyTimesChanged(self.times_of_day)

    def nightWorld(self):
        self.times_of_day="night"

    def morningWorld(self):
        self.times_of_day="morning"

    def dayWorld(self):
        self.times_of_day="day"

    def eveningWorld(self):
        self.times_of_day="evening"

