# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONWriter
from janusgraph_python.serializer.PointSerializer import PointSerializer
from janusgraph_python.serializer.CircleSerializer import CircleSerializer
from janusgraph_python.core.datatypes.Point import Point
from janusgraph_python.core.datatypes.Circle import Circle


class JanusGraphSONWriter(object):
    serializers = dict()

    def __init__(self):
        self.writer = None
        pass

    def __register_default_serializers(self):
        janusSerializers = self.__build_serializers()

        self.serializers.update(janusSerializers)

    def __build_serializers(self):
        # Currently the default serializers registered.

        janusSerializers = {
            Circle: CircleSerializer,
            Point: PointSerializer
        }

        return janusSerializers

    def build(self):
        self.__register_default_serializers()
        self.writer = GraphSONWriter(self.serializers)
        return self.writer

    def register_serializer(self, typeClass, serializer):
        """

        Args:
            typeClass (type):
            serializer:

        Returns:

        """

        self.serializers[typeClass] = serializer
