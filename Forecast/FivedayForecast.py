class FivedayForecast(object):
    def __init__(self, fivedayforecast):
        self.Day_one = Day(fivedayforecast[0])
        self.Day_two = Day(fivedayforecast[1])
        self.Day_three = Day(fivedayforecast[2])
        self.Day_four = Day(fivedayforecast[3])
        self.Day_five = Day(fivedayforecast[4])
        

class Day(object):
    def __init__(self, day):
        for key in day:
            object.__setattr__(self, key, day[key])