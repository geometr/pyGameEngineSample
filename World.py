import Time
import Temperature
import Screen
import Region

class World:

    def __init__(self, set_hours_in_day = 24, set_days_in_year = 360):
        self.screen = Screen.Screen()
        self.time = Time.Time(set_hours_in_day, set_days_in_year)
        self.temperature = Temperature.Temperature()
        self.time.attach(self.temperature)
        self.regions = set()
        for x,y,biom,min_biom in (          (400,0,2,1),
                                                (600,100,3,1),
                                                    (800,200,4,2),
                                        (200,100,2,0),
                                            (400,200,2,0),
                                                (600,300,4,2),
                                    (0,200,1,0),
                                        (200,300,2,0),
                                            (400,400,4,2)):
            self.regions.add(self.createRegion(x,y,biom,min_biom))
        self.screen.attach(self.temperature)
        self.screen.attach(self.time)
    def createRegion(self,x,y,biom,min_biom):
        region = Region.Region(x,y,biom,min_biom)
        self.time.attach(region)
        self.screen.attach(region)
        return region

    def tick(self):
        self.time.tick()

    def render(self, clock):
        self.screen.render(clock)
