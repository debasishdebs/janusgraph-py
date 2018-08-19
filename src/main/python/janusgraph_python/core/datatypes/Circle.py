"""
Copyright 2018 Debasish Kanhar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "Debasish Kanhar (https://github.com/debasishdebs)"
__credits__ = ["Florian Hockman", "Jason Plurad", "Dave Brown", "Marko Rodriguez"]
__license__ = "Apache-2.0"
__version__ = "0.0.1"
__email__ = ["d.kanhar@gmail.com", "dekanhar@in.ibm.com"]


class Circle(object):
    def __init__(self, longitude, latitude, radiusInKM):
        """

        Args:
            latitude (float):
            longitude (float):
            radiusInKM (int):
        """
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radiusInKM

        status = self.__are_valid_coordinates()

        if status:
            pass
        else:
            raise ValueError("Invalid Coordinates/Radius passed. "
                             "Latitude needs to be b/w [-90, 90] and Longitude b/w [-180, 180] and Radius > 0")

        pass

    def getShape(self):
        """

        Returns:
            str
        """
        return "CIRCLE"

    def toString(self):
        return "CIRCLE(lat: {}, lon: {}, r: {})".format(self.getLatitude(), self.getLongitude(), self.getRadius())

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def getCoordinates(self):
        return [self.latitude, self.longitude]

    def getRadius(self):
        return self.radius

    def __are_valid_coordinates(self):
        if (-90 <= self.getLatitude() <= 90) and (-180 <= self.getLongitude() <= 180) and (self.getRadius() > 0):
            return True
        else:
            return False

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

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.toString()