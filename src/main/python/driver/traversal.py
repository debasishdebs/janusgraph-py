# Name: Debasish Kanhar
# Emp ID: 05222V


from gremlin_python.process.traversal import Traversal


class JanusGraphTraversal(Traversal):
    def __init__(self, graph, traversal_strategies, bytecode):
        self.graph = graph
        self.traversal_strategies = traversal_strategies
        self.bytecode = bytecode
        self.side_effects = JanusGraphTraversalSideEffects()
        self.traversers = None
        self.last_traverser = None
        super(JanusGraphTraversal, self).__init__(self.graph, self.traversal_strategies, self.bytecode)
        pass


class JanusGraphTraversalSideEffects(object):
    def keys(self):
        return set()
    def get(self, key):
        raise KeyError(key)
    def __getitem__(self, key):
        return self.get(key)
    def __repr__(self):
        return "sideEffects[size:" + str(len(self.keys())) + "]"
