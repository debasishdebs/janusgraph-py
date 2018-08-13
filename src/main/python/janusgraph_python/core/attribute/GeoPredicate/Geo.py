# Name: Debasish Kanhar

from .GeoContains import GeoContains
from .GeoWithin import GeoWithin


class Geo(object):
    def __init__(self):
        pass
    contains = GeoContains()
    within = GeoWithin()

    @staticmethod
    def geoContains(value):
        return Geo.contains.geoContains(value)

    @staticmethod
    def geoWithin(value):
        return Geo.within.geoWithin(value)
