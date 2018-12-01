import json
import requests
from urllib.request import urlopen
from Forecast.Forecast import Forecast
from Actual.Actual import Actual

class Buienradar:
    def __init__(self):
        self.get_json_data()
    
    def get_json_data(self):
        
        url = 'https://api.buienradar.nl/data/public/2.0/jsonfeed'
        response = urlopen(url)
        data = response.read()

        encoding = response.info().get_content_charset()
        html = data.decode(encoding)
        json_data = json.loads(html)
        self.set_json_data(json_data)

    def set_json_data(self, json):
        forecast_data = json['forecast']
        actual_data = json['actual']
        self.Forecast = Forecast(forecast_data)
        self.Actual = Actual(actual_data)