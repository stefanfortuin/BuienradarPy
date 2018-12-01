class Weatherreport(object):
    def __init__(self, weatherreport):
        for key in weatherreport:
            object.__setattr__(self, key, weatherreport[key])
    
    