# Name: Debasish Kanhar


class Point(object):
    def __init__(self, latitude, longitude):
        """

        Args:
            latitude (long):
            longitude (long):
        """
        self.latitude = latitude
        self.longitude = longitude
        pass

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def __eq__(self, other):
        """

        Args:
            other (Point):

        Returns:

        """

        if other is None:
            return False
        else:
            if (other.getLatitude()).__eq__(self.getLatitude()) and (other.getLongitude()).__eq__(self.getLongitude()):
                return True
            else:
                return False

    def __hash__(self):
        return (self.getLatitude().__hash__()*397) ^ (self.getLongitude().__hash__())
