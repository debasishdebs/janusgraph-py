# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from ..core.datatypes.GeoShape import Point
from ..utils.toGeoJSON import toGeoJSON


class PointSerializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"

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

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, geometryJSON, cls.GRAPHSON_PREFIX)

        return serializedJSON
