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
