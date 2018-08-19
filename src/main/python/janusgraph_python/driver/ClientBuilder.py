"""
Copyright 2018 Debasish Kanhar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "Debasish Kanhar (https://github.com/debasishdebs)"
__credits__ = ["Florian Hockman", "Jason Plurad", "Dave Brown", "Marko Rodriguez"]
__license__ = "Apache-2.0"
__version__ = "0.0.1"
__email__ = ["d.kanhar@gmail.com", "dekanhar@in.ibm.com"]


from ..structure.io.GraphsonReader import JanusGraphSONReader
from ..structure.io.GraphsonWriter import JanusGraphSONWriter

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph


class JanusGraphClient(object):
    REMOTE_CONNECTION = None

    def __init__(self, version=3.0):
        self.graphsonVersion = version
        pass

    def build(self, url="loclahost", port="8182", graph="g"):

        URL = "ws://{}:{}/gremlin".format(url, port)

        graphson_reader = JanusGraphSONReader().build()
        graphson_writer = JanusGraphSONWriter().build()

        self.REMOTE_CONNECTION = DriverRemoteConnection(URL, graph, graphson_reader=graphson_reader,
                                                        graphson_writer=graphson_writer)

        return self

    def get_traversal(self):
        graph = Graph()
        g = graph.traversal().withRemote(self.REMOTE_CONNECTION)
        return g
