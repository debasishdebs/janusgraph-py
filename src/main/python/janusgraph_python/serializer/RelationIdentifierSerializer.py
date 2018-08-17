# Name: Debasish Kanhar

from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from janusgraph_python.core.datatypes.RelationIdentifier import RelationIdentifier


class RelationIdentifierSerializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "RelationIdentifier"

    @classmethod
    def dictify(cls, relationID, writer):
        """

        Args:
            relationID (RelationIdentifier):
            writer:

        Returns:

        """

        relationJSON = cls.__relationID_to_json(relationID)

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, relationJSON, cls.GRAPHSON_PREFIX)

        return serializedJSON

    @classmethod
    def __relationID_to_json(cls, relationID):
        """

        Args:
            relationID (RelationIdentifier):

        Returns:

        """

        relationIdDict = dict()

        relationIdDict["relationId"] = relationID.toString()

        return relationIdDict
