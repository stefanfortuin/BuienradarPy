from Buienradar import Buienradar
buienradar = Buienradar()


print(buienradar.Forecast.Fivedayforecast.Day_one.day)
print(buienradar.Forecast.Fivedayforecast.Day_three.maxtemperature)
print(buienradar.Forecast.Shortterm.forecast)
print(buienradar.Forecast.Longterm.forecast)
print(buienradar.Actual.sunrise)
print(buienradar.Actual.sunset)

stationarnhem = buienradar.Actual.station_by_name("arnhem")
for key, value in stationarnhem.__dict__.items():
    print(key, value)

    
print(buienradar.Actual.station_by_name("arnhem"))
print(buienradar.Actual.station_by_id(6330))