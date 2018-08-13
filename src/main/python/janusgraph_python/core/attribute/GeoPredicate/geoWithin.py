# Name: Debasish Kanhar

from gremlin_python.process.traversal import P


class GeoWithin(object):
    def __init__(self):
        pass

    def toString(self):
        return "geoWithin"

    def geoWithin(self, value):

        withinP = P(self.toString(), value)

        return withinP
