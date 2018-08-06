# Name: Debasish Kanhar
# Emp ID: 05222V


from gremlin_python.process.traversal import P
from gremlin_python import statics


class JanusGraphP(P):
    def __init__(self, operator, value, other=None):
        self.operator = operator
        self.value = value
        self.other = other

        super(JanusGraphP, self).__init__(self.operator, self.value, self.other)

        pass

    @staticmethod
    def textContains(*args):
        JanusGraphP("textContains", *args)


def textContains(*args):
    return JanusGraphP.textContains(*args)
statics.add_static('textContains', textContains)
