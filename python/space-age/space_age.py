from datetime import timedelta


class SpaceAge:
    PLANETS = {'on_mercury': 0.2408467, 'on_venus': 0.61519726, 'on_earth': 1.0, 'on_mars': 1.8808158,'on_jupiter': 11.862615, 'on_saturn': 29.447498, 'on_uranus': 84.016846, 'on_neptune': 164.79132}

    def __init__(self, seconds):
        self.seconds = seconds
        for planet in self.PLANETS:
            setattr(self,planet,self.the_caller(planet))
        pass
    def the_caller(self,planet):
        func=self.the_planet(self.PLANETS[planet])
        return lambda planet=planet:func
        pass
    def the_planet(self, one_year):
        self.one_year = one_year*365.25
        year = timedelta(days=self.one_year)
        years = timedelta(seconds=self.seconds)/year
        return round(years,2)