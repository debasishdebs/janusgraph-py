# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONReader
from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from janusgraph_python.serializer.GeoShapeDeserializer import GeoShapeDeserializer


class JanusGraphSONReader(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "Geoshape"
    GeoShape_GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)

    deserializers = dict()

    def __init__(self):
        self.reader = None
        pass

    def __register_default_deserializers(self):
        janusDeSerializers = self.__build_deserializers()

        self.deserializers.update(janusDeSerializers)

    def __build_deserializers(self):
        # Currently the default de-serializers registered.

        janusDeSerializers = {
            self.GeoShape_GRAPHSON_TYPE: GeoShapeDeserializer
        }

        return janusDeSerializers

    def build(self):
        self.__register_default_deserializers()
        self.reader = GraphSONReader(self.deserializers)
        return self.reader

    def register_deserializer(self, typeClass, serializer):
        """

        Args:
            typeClass (type):
            serializer:

        Returns:

        """

        self.deserializers[typeClass] = serializer
