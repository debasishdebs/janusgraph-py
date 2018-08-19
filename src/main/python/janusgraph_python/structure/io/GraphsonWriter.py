# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONWriter

from ...serializer.PointSerializer import PointSerializer
from ...serializer.CircleSerializer import CircleSerializer
from ...serializer.RelationIdentifierSerializer import RelationIdentifierSerializer
from ...core.datatypes.GeoShape import Point, Circle
from ...core.datatypes.RelationIdentifier import RelationIdentifier


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
            Point: PointSerializer,
            RelationIdentifier: RelationIdentifierSerializer
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
