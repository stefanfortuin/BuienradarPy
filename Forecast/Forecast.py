from Forecast.Weatherreport import Weatherreport
from Forecast.Term import Term
from Forecast.FivedayForecast import FivedayForecast

class Forecast(object):
    """Weather forecast for shortterm, longterm, fiveday forecast and a small weatherreport"""
    def __init__(self, forecast):
        self.Weatherreport = Weatherreport(forecast['weatherreport'])
        self.Shortterm = Term(forecast['shortterm'])
        self.Longterm = Term(forecast['longterm'])
        # self.__fivedayforecast = FivedayForecast(forecast['fivedayforecast'])
        self.Fivedayforecast = FivedayForecast(forecast['fivedayforecast'])

    # Room for other functions


