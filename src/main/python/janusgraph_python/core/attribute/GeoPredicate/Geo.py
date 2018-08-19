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
        """

        Args:
            value :

        Returns:

        """
        return Geo.contains.geoContains(value)

    @staticmethod
    def geoWithin(value):
        """

        Args:
            value:

        Returns:

        """
        return Geo.within.geoWithin(value)
