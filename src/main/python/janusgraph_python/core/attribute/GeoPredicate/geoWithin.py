# Name: Debasish Kanhar

from gremlin_python.process.traversal import P


class GeoWithin(object):
    def __init__(self):
        pass

    def toString(self):
        return "geoWithin"

    def geoWithin(self, value):
        print("I'm inside correct method signature of geoWithin")
        print(value)

        withinP = P(self.toString(), value)
        print(withinP)

        return withinP
