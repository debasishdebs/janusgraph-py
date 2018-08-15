# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from janusgraph_python.core.datatypes.Circle import Circle
from janusgraph_python.utils.toGeoJSON import toGeoJSON


class CircleSerializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"
    GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)

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

        return serializedJSON
