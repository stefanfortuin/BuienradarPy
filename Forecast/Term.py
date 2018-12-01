class Term(object):
    def __init__(self, term):
        for key in term:
            object.__setattr__(self, key, term[key])
