# Name: Debasish Kanhar

from gremlin_python.process.traversal import P


class GeoDisjoint(object):
    def __init__(self):
        pass

    def toString(self):
        return "geoDisjoint"

    def geoDisjoint(self, value):
        print("I'm inside correct method signatured of geoDisjoint")
        return P(self.toString(), value)
