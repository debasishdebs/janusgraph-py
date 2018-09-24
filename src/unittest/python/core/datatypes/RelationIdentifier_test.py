# Copyright 2018 JanusGraph Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest
from janusgraph_python.core.datatypes.RelationIdentifier import RelationIdentifier


class TestRelationIdentifier(unittest.TestCase):
    def setUp(self):
        self.relationID = "74q-9n4-b2t-cr4"

        self.edgeID = RelationIdentifier(self.relationID)
        pass

    def test_relationID_equality(self):
        id1 = "74q-9n4-b2t-cr4"
        id2 = "74q-9n4-b2t-cr6"

        e1 = self.edgeID
        e2 = RelationIdentifier(id1)
        e3 = RelationIdentifier(id2)

        self.assertEqual(e1, e2)
        self.assertNotEqual(e1, e3)
        pass