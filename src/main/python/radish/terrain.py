'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''

from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver import serializer
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from radish import before, after, world

outV = __.outV
label = __.label
inV = __.inV
project = __.project
tail = __.tail


@before.all
def prepare_static_traversal_source(features, marker):
    # as the various traversal sources for testing do not change their data, there is no need to re-create remotes
    # and client side lookup data over and over. it can be created once for all tests and be reused.
    cache = {}
    for graph_name in (("modern", "gmodern"), ("classic", "gclassic"), ("crew", "gcrew"), ("grateful", "ggrateful"), ("sink", "gsink")):
        cache[graph_name[0]] = {}
        remote = __create_remote(graph_name[1])
        cache[graph_name[0]]["remote_conn"] = __create_remote(graph_name[1])
        cache[graph_name[0]]["lookup_v"] = __create_lookup_v(remote)
        cache[graph_name[0]]["lookup_e"] = __create_lookup_e(remote)

    # store the cache on the global context so that remotes can be shutdown cleanly at the end of the tests
    world.cache = cache

    # iterate each feature and apply the cached remotes/lookups to each scenario context so that they are
    # accessible to the feature steps for test logic
    for feature in features:
        for scenario in feature.all_scenarios:
            scenario.context.remote_conn = {}
            scenario.context.lookup_v = {}
            scenario.context.lookup_e = {}

            for graph_name in ("modern", "classic", "crew", "grateful", "sink"):
                scenario.context.remote_conn[graph_name] = cache[graph_name]["remote_conn"]
                scenario.context.lookup_v[graph_name] = cache[graph_name]["lookup_v"]
                scenario.context.lookup_e[graph_name] = cache[graph_name]["lookup_e"]

            # setup the "empty" lookups as needed
            scenario.context.lookup_v["empty"] = {}
            scenario.context.lookup_e["empty"] = {}


@before.each_scenario
def prepare_traversal_source(scenario):
    # some tests create data - create a fresh remote to the empty graph and clear that graph prior to each test
    if not("graphson" in world.config.user_data):
        raise ValueError('test configuration requires setting of --user-data="graphson=*" to one of [v2,v3]')

    if world.config.user_data["graphson"] == "v3":
        s = serializer.GraphSONSerializersV3d0()
    elif world.config.user_data["graphson"] == "v2":
        s = serializer.GraphSONSerializersV2d0()
    else:
        raise ValueError('serializer set with --user-data="graphson=v2" must be one of [v2,v3]')

    remote = DriverRemoteConnection('ws://localhost:45940/gremlin', "ggraph", message_serializer=s)
    scenario.context.remote_conn["empty"] = remote
    g = Graph().traversal().withRemote(remote)
    g.V().drop().iterate()


@after.each_scenario
def close_traversal_source(scenario):
    scenario.context.remote_conn["empty"].close()


@after.all
def close_static_traversal_source(features, marker):
    for key, value in world.cache.iteritems():
        value["remote_conn"].close()


def __create_remote(server_graph_name):
    return DriverRemoteConnection('ws://localhost:45940/gremlin', server_graph_name, message_serializer=serializer.GraphSONSerializersV3d0())


def __create_lookup_v(remote):
    g = Graph().traversal().withRemote(remote)

    # hold a map of name/vertex for use in asserting results
    return g.V().group().by('name').by(tail()).next()


def __create_lookup_e(remote):
    g = Graph().traversal().withRemote(remote)

    # hold a map of the "name"/edge for use in asserting results - "name" in this context is in the form of
    # outgoingV-label->incomingV
    return g.E().group(). \
        by(lambda: ("it.outVertex().value('name') + '-' + it.label() + '->' + it.inVertex().value('name')", "gremlin-groovy")). \
        by(tail()).next()
