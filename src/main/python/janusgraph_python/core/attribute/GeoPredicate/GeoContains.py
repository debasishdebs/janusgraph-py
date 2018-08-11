# Name: Debasish Kanhar

from gremlin_python.process.traversal import P


class GeoContains(object):
    def __init__(self):
        pass

    def toString(self):
        return "geoContains"

    def geoContains(self, value):
        print("I'm inside correct method signatured of geoContains")
        return P(self.toString(), value)
