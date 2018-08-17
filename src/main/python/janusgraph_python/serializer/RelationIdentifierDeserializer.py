# Name: Debasish Kanhar

from janusgraph_python.core.datatypes.RelationIdentifier import RelationIdentifier


class RelationIdentifierDeserializer(object):

    @classmethod
    def objectify(cls, graphsonObj, reader):
        """

        Args:
            graphsonObj (dict):
            reader:

        Returns:

        """

        relationID = str(graphsonObj["relationId"])

        relationID = RelationIdentifier(relationID)

        return relationID
