import random

class Temperature:
    local_temperature = 0
    global_temperature = 0
    maximal_delta = 20
    half_maximal_delta = maximal_delta / 2

    def notifyTimesChanged(self, *argv):
        self.updateLocalTemperature(*argv)

    def notifyDayChanged(self, *argv):
        self.calculateGlobalTemperature(*argv)

    def __init__(self, set_maximal_delta = 20):
        self.maximal_delta = set_maximal_delta
        self.half_maxmial_delta = self.maximal_delta / 2
        self.global_temperature = -self.half_maximal_delta
        self.setupLocalTemperature()

    def calculateGlobalTemperature(self, current_day, days_in_year):
        if current_day < days_in_year / 2:
            self.calculateGlobalTemperatureSpring(current_day, days_in_year)
        else:
            self.calculateGlobalTemperatureAutumn(current_day, days_in_year)
        self.setupLocalTemperature()

    def calculateGlobalTemperatureSpring(self, current_day, days_in_year):
        print(current_day/ days_in_year*2*self.maximal_delta-self.half_maximal_delta)
        self.global_temperature = current_day / days_in_year * 2 * self.maximal_delta - self.half_maximal_delta

    def calculateGlobalTemperatureAutumn(self, current_day, days_in_year):
        self.global_temperature = self.half_maximal_delta - current_day * 2 / days_in_year * self.maximal_delta

    def setupLocalTemperature(self):
        self.local_temperature = self.global_temperature + random.randrange(1, self.maximal_delta) - self.half_maximal_delta

    def updateLocalTemperature(self, times):
        if times=="night":
            self.local_temperature = self.local_temperature - 1
        elif times=="day":
            self.local_temperature = self.local_temperature + 2
        elif times=="morning":
            self.local_temperature = self.local_temperature + 0.5
        else:
            self.local_temperature = self.local_temperature - 0.5

    def getTemperature(self):
        return self.local_temperature
