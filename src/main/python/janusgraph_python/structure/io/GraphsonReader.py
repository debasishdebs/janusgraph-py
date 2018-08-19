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


from gremlin_python.structure.io.graphsonV3d0 import GraphSONReader
from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil

from ...serializer.RelationIdentifierDeserializer import RelationIdentifierDeserializer
from ...serializer.GeoShapeDeserializer import GeoShapeDeserializer


class JanusGraphSONReader(object):
    GRAPHSON_PREFIX = "janusgraph"
    GEO_GRAPHSON_BASE_TYPE = "Geoshape"
    RELATIONID_BASE_TYPE = "RelationIdentifier"
    GeoShape_GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GEO_GRAPHSON_BASE_TYPE)
    RelationID_GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, RELATIONID_BASE_TYPE)

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
            self.GeoShape_GRAPHSON_TYPE: GeoShapeDeserializer,
            self.RelationID_GRAPHSON_TYPE: RelationIdentifierDeserializer
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
