import re

class Actual(object):
    """Actual weatherdata from weatherstation around the Netherlands"""
    def __init__(self, actual):
        self.stations = []
        for key in actual:
            if key == 'stationmeasurements':
                for station in actual[key]:
                    self.stations.append(Station(station))
            else:
                object.__setattr__(self, key, actual[key])

    def station_by_name(self, name):
        """get the data from a station by name, e.i. "Arnhem" """
        for station in self.stations:
            if name.lower() in station.stationname.lower():
                return station

        print(str.format("Could not find station with name '{0}'", name))

    def station_by_id(self, id):
        """get the data from a station by id, e.i. 6370 corresponds to Eindhoven"""
        for station in self.stations:
            if id == station.stationid:
                return station

        print(str.format("Could not find station with '{0}'",str(id)))


class Station(object):
    def __init__(self, station):
        for key in station:
            if key == 'dayhistory':
                object.__setattr__(self, 'dayhistory' , Dayhistory(station[key]))
            else:
                object.__setattr__(self, key, station[key])

    

class Dayhistory(object):
    def __init__(self, history):
        for key in history:
            object.__setattr__(self, key, history[key])