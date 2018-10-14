# Name: Debasish Kanhar
# Emp ID: 05222V


from .SchemaBuilder import SchemaBuilder
from .Helpers import Helpers as helpers


class EdgeLabelBuilder(SchemaBuilder):
    def __init__(self, connection):
        super(EdgeLabelBuilder, self).__init__(connection)

        self.query += helpers.open_graph_management()

        self.label = None
        self.mult = None
        self.sign = None
        pass

    def makeEdgeLabel(self, label):
        self.label = label
        return self

    def multiplicity(self, mult):
        self.mult = mult
        return self

    def signature(self, property):
        self.sign = property
        return self

    def make(self):
        if self.label is None:
            raise AttributeError("makeVertexLabel() method needs called before make()")

        if self.mult is not None and self.sign is None:
            qq = "{} = mgmt.makeEdgeLabel('{}').multiplicity({}).make();".format(self.label, self.label,
                                                                                   self.mult)
        elif self.mult is None and self.sign is None:
            qq = "{} = mgmt.makeEdgeLabel('{}').make();".format(self.label, self.label)

        elif self.mult is None and self.sign is not None:
            qq = "{} = mgmt.makeEdgeLabel('{}').signature(mgmt.getPropertyKey('{}')).make();".format(
                                self.label, self.label, self.sign)
        else:
            qq = "{} = mgmt.makeEdgeLabel('{}').\
                    signature(mgmt.getPropertyKey('{}')).multiplicity({}).make();".format(self.label,self.label,
                                                                                                self.sign, self.mult)

        q = "if (mgmt.getEdgeLabel('"+self.label+"')) {" \
            "   "+self.label+" = mgmt.getEdgeLabel('"+self.label+"'); }" \
            "else {" \
            "   " + qq + " }\n"

        self.query += q

        self.query += helpers.close_graph_management()

        self.create(self.query)

        return self.label

