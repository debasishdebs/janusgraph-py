# Name: Debasish Kanhar

from gremlin_python.process.traversal import P


class GeoIntersect(object):
    def __init__(self):
        pass

    def toString(self):
        return "geoIntersect"

    def geoIntersect(self, value):
        print("I'm inside correct method signatured of geoIntersect")
        return P(self.toString(), value)
