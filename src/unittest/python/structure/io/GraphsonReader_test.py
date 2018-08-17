# # Name: Debasish Kanhar
#
# import unittest
# from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
# from janusgraph_python.structure.io.GraphsonReader import JanusGraphSONReader
#
#
# class MockDeserializer(object):
#     def __init__(self):
#         pass
#
#     @classmethod
#     def objectify(cls, graphsonObj, reader):
#
#         return
#
#
# class TestGraphsonReader(unittest.TestCase):
#     GRAPHSON_PREFIX = "janusgraph"
#     GRAPHSON_BASE_TYPE = "MOCK"
#     GeoShape_GRAPHSON_TYPE = GraphSONUtil.formatType(GRAPHSON_PREFIX, GRAPHSON_BASE_TYPE)
#
#     def setUp(self):
#         self.readerClass = JanusGraphSONReader()
#         self.reader = None
#
#         pass
#
#     def test_mock_deserializer(self):
#         deserializer = MockDeserializer
#
#         self.readerClass.register_deserializer(self.GeoShape_GRAPHSON_TYPE, deserializer)
#         self.reader = self.readerClass.build()
#
#         self.reader.toObject()
#         return
