# Name: Debasish Kanhar


class Circle(object):
    def __init__(self, latitude, longitude, radiusInKM):
        """

        Args:
            latitude (float):
            longitude (float):
            radiusInKM (int):
        """
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radiusInKM
        pass

    def getShape(self):
        """

        Returns:
            str
        """
        return "CIRCLE"

    def toString(self):
        return "Geoshape.circle"

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def getCoordinates(self):
        return [self.latitude, self.longitude]

    def getRadius(self):
        return self.radius

    def __eq__(self, other):
        """

        Args:
            other (Circle):

        Returns:

        """

        if other is None:
            return False
        else:
            if (other.getLatitude()).__eq__(self.getLatitude()) and \
                    (other.getLongitude()).__eq__(self.getLongitude()) and \
                    (other.getRadius()).__eq__(self.getRadius()):
                return True
            else:
                return False
