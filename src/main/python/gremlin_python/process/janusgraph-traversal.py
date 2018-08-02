from .traversal import P


class JanusGraphP(P):
    def __init__(self, operator, value, other=None):
        P.__init__(operator, value, other)
        # super(JanusGraphP, self).__init__(operator, value, other)

        self.operator = operator
        self.value = value
        self.other = other

        pass

    @staticmethod
    def textContains(*args):
        return P("textContains", *args)
