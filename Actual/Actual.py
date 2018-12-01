class Actual(object):
    """Actual weatherdata from weatherstation around the Netherlands"""
    def __init__(self, actual):
        for key in actual:
            object.__setattr__(self, key, actual[key])
