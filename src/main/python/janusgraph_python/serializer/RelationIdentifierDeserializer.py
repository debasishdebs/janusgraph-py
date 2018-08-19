# Name: Debasish Kanhar

from ..core.datatypes.RelationIdentifier import RelationIdentifier


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
