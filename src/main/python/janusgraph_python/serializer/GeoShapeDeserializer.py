# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.core.datatypes.Circle import Circle


class GeoShapeDeserializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"
    GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)

    @classmethod
    def objectify(cls, graphsonObj, reader):
        """

        Args:
            graphsonObj (dict):
            reader:

        Returns:

        """

        geometryData = graphsonObj["geometry"]

        if "coordinates" in geometryData and isinstance(geometryData["coordinates"], list):
            coordinates = geometryData["coordinates"]
            shape = geometryData["type"]
            radius = geometryData["radius"]
            radiusUnits = geometryData["property"]["radius_units"]

            if len(coordinates) >= 2:
                if shape.lower() == "circle":
                    if radiusUnits:
                        if radiusUnits.lower() == "km":
                            radius = radius
                        elif radiusUnits.lower() == "m":
                            radius = 0.001 * radius
                        else:
                            raise NotImplementedError("Current JanusGraph python serializers can only \
                                                        understand Radius units in KM and Mts.")
                        pass
                    else:
                        radius = radius
                        pass

                    return cls.__deserialize_circle_from_coordinates(coordinates, radius)

                elif shape.lower() == "point":
                    return cls.__deserialize_points_from_coordinates(coordinates)

                else:
                    raise NotImplementedError("Currently implemented De-serialization \
                                                    for Geometry shapes CIRCLE and POINT.")

            else:
                raise AttributeError("Invalid GeoShape parameters passed.")

        else:
            raise AttributeError("Invalid GeoShape parameters passed.")

    @classmethod
    def __deserialize_points_from_coordinates(cls, coordinates):
        """

        Args:
            coordinates (object):

        Returns:
            point (Point)
        """

        coordList = type(list)(coordinates)
        coordList = [type(float)(x) for x in coordList]

        point = cls.__get_point_from_coordinates(coordList)

        return point

    @classmethod
    def __get_point_from_coordinates(cls, coordinates):
        """

        Args:
            coordinates (list):

        Returns:
            pt (Point)
        """

        latitude = coordinates[0]
        longitude = coordinates[1]

        pt = Point(latitude, longitude)

        return pt

    @classmethod
    def __deserialize_circle_from_coordinates(cls, coordinates, radius):
        """

        Args:
            coordinates (object):

        Returns:
            circle (Circle)
        """

        coordList = type(list)(coordinates)
        coordList = [type(float)(x) for x in coordList]
        radius = type(float)(radius)

        circle = cls.__get_circle_from_coordinates(coordList, radius)

        return circle

    @classmethod
    def __get_circle_from_coordinates(cls, coordinates, radius):
        """

        Args:
            coordinates (list):

        Returns:
            cr (Circle)
        """

        latitude = coordinates[0]
        longitude = coordinates[1]

        cr = Circle(latitude, longitude, radius)

        return cr
