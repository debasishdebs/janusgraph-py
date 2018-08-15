# Name: Debasish Kanhar


class Point(object):
    def __init__(self, longitude, latitude):
        """

        Args:
            latitude (float):
            longitude (float):
        """
        self.latitude = latitude
        self.longitude = longitude

        status = self.__are_valid_coordinates()

        if status:
            pass
        else:
            raise ValueError("Invalid Coordinates passed. "
                             "Latitude needs to be b/w [-90, 90] and Longitude b/w [-180, 180]")
        pass

    def getShape(self):
        """

        Returns:
            str
        """

        return "POINT"

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def getCoordinates(self):
        return [self.latitude, self.longitude]

    def __are_valid_coordinates(self):
        if (-90 <= self.getLatitude() <= 90) and (-180 <= self.getLongitude() <= 180):
            return True
        else:
            return False

    def __eq__(self, other):
        """

        Args:
            other (Point):

        Returns:

        """

        if other is None:
            return False
        else:
            if (other.getLatitude()).__eq__(self.getLatitude()) and \
                    (other.getLongitude()).__eq__(self.getLongitude()):
                return True
            else:
                return False

    def __str__(self):
        return self.toString()

    def __ne__(self, other):
        return not self.__eq__(other)

    def toString(self):
        point = "POINT(lat: {}, lon: {})".format(self.getLatitude(), self.getLongitude())
        return point
