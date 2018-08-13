# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.utils.toGeoJSON import toGeoJSON


class PointSerializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"
    GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)

    # def __init__(self, longitude, latitude):
    #     self.longitude = longitude
    #     self.latitude = latitude
    #     pass

    @classmethod
    def objectify(cls, graphsonObj, reader):
        """
        This is deserializer method for Point class.

        Args:
            graphsonObj (dict):
            reader:

        Returns:

        """

        if "coordinates" in graphsonObj:
            coordinates = graphsonObj["coordinates"]
            return cls.__deserialize_points_from_coordinates(coordinates)

        geometry = graphsonObj["geometry"]

        raise NotImplementedError("Deserialization of {} is not supported yet.".format(geometry["type"]))

    @classmethod
    def dictify(cls, point, writer):
        """
        This is serializer method for Point class.

        Args:
            point (Point):
            writer:

        Returns:

        """

        geometryJSON = toGeoJSON(point).convert()

        # serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE,
        #                                          {"coordinates", [point.getLatitude(), point.getLongitude()]},
        #                                          cls.GRAPHSON_PREFIX)

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, geometryJSON, cls.GRAPHSON_PREFIX)
        # print("Serialized json on point being called ")
        # print(serializedJSON)
        return serializedJSON

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
