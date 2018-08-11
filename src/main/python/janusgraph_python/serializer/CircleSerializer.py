# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from janusgraph_python.core.datatypes.Circle import Circle
from janusgraph_python.serializer.toGeoJSON import toGeoJSON


class CircleSerializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"
    GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)

    # def __init__(self):
    #     pass

    @classmethod
    def dictify(cls, circle, writer):
        """
        This is serializer method for Circle class.

        Args:
            circle (Circle):
            writer:

        Returns:

        """

        geometryJSON = toGeoJSON(circle).convert()

        # serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE,
        #                                          {"coordinates", [point.getLatitude(), point.getLongitude()]},
        #                                          cls.GRAPHSON_PREFIX)

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, geometryJSON, cls.GRAPHSON_PREFIX)
        print("Serialised JSON is being called.")
        print(serializedJSON)
        return serializedJSON

    @classmethod
    def objectify(cls, graphsonObj, reader):
        """
        This is deserializer method for Circle class.

        Args:
            graphsonObj (dict):
            reader:

        Returns:

        """

        if "coordinates" in graphsonObj:
            coordinates = graphsonObj["coordinates"]
            radius = graphsonObj["radius"]
            radiusUnits = graphsonObj["property"]["radius_units"]

            if radiusUnits:
                if radiusUnits.toLower() == "km":
                    radius = radius
                elif radiusUnits.toLower() == "m":
                    radius = 0.001 * radius
                else:
                    raise NotImplementedError("Current JanusGraph python serializers can only \
                                                understand Radius units in KM and Mts.")
                pass
            else:
                radius = radius
                pass

            return cls.__deserialize_points_from_coordinates(coordinates, radius)

        geometry = graphsonObj["geometry"]

        raise NotImplementedError("Deserialization of {} is not supported yet.".format(geometry["type"]))

    @classmethod
    def __deserialize_points_from_coordinates(cls, coordinates, radius):
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
