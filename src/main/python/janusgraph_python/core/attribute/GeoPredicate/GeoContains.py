# Name: Debasish Kanhar

from gremlin_python.process.traversal import P


class GeoContains(object):
    def __init__(self):
        pass

    def toString(self):
        """

        Returns:

        """
        return "geoContains"

    def geoContains(self, value):
        """

        Args:
            value:

        Returns:

        """
        continsP = P(self.toString(), value)
        return continsP
