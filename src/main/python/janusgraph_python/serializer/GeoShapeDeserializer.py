# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.core.datatypes.Circle import Circle
import pprint


class GeoShapeDeserializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"
    VALUE_KEY = "@value"
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
        geometryDataValue = geometryData[cls.VALUE_KEY]

        val = iter(geometryDataValue)
        geometryDataValue = dict(zip(val, val))

        # print(10 * "A")
        # pprint.pprint(graphsonObj)
        # print(10 * "A")
        # pprint.pprint(geometryDataValue)
        # print(10 * "A")
        # print(type(geometryDataValue))
        # print(10 * "A")
        #
        # pprint.pprint(geometryDataValue)
        # print(10 * "A")

        if "coordinates" in geometryDataValue and isinstance(geometryDataValue["coordinates"][cls.VALUE_KEY], list):
            coordinates = geometryDataValue["coordinates"][cls.VALUE_KEY]
            shape = geometryDataValue["type"]
            radius = geometryDataValue["radius"][cls.VALUE_KEY]
            radiusUnits = geometryDataValue["properties"][cls.VALUE_KEY][1]

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

                    circle = cls.__deserialize_circle_from_coordinates(coordinates, radius)
                    # print(circle.toString())
                    return circle.toString()

                elif shape.lower() == "point":
                    point = cls.__deserialize_points_from_coordinates(coordinates)
                    # print(point.toString())
                    return point.toString()

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

        coordList = list(coordinates)
        coordList = [x[cls.VALUE_KEY] for x in coordList]
        radius = int(radius)

        circle = cls.__get_circle_from_coordinates(coordList, radius)

        return circle

    @classmethod
    def __get_circle_from_coordinates(cls, coordinates, radius):
        """

        Args:
            coordinates (list):
            radius (int):

        Returns:
            cr (Circle)
        """

        latitude = coordinates[0]
        longitude = coordinates[1]

        cr = Circle(latitude, longitude, radius)

        return cr
