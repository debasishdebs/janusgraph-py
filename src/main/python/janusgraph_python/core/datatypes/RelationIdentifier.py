# Name: Debasish Kanhar


class RelationIdentifier(object):
    def __init__(self, relationID):
        self.relationID = relationID
        pass

    def __eq__(self, other):
        """

        Args:
            other (RelationIdentifier):

        Returns:

        """
        if other is None:
            return False
        else:
            if self.relationID == other.relationID:
                return True
            else:
                return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.toString()

    def toDict(self):
        edgeID = dict()
        edgeID["janusgraph:RelationIdentifier"] = self.toString()
        return edgeID

    def toString(self):
        return str(self.relationID)

    def getID(self):
        return self.toString()
