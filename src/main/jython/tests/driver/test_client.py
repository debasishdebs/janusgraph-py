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
import pytest

from gremlin_python.driver.client import Client
from gremlin_python.driver.request import RequestMessage
from gremlin_python.structure.graph import Graph
from gremlin_python.driver import serializer

__author__ = 'David M. Brown (davebshow@gmail.com)'


def test_connection(connection):
    g = Graph().traversal()
    t = g.V()
    message = RequestMessage('traversal', 'bytecode', {'gremlin': t.bytecode, 'aliases': {'g': 'gmodern'}})
    results_set = connection.write(message).result()
    future = results_set.all()
    results = future.result()
    assert len(results) == 6
    assert isinstance(results, list)


def test_client_simple_eval(client):
    assert client.submit('1 + 1').all().result()[0] == 2


def test_client_simple_eval_bindings(client):
    assert client.submit('x + x', {'x': 2}).all().result()[0] == 4


def test_client_eval_traversal(client):
    assert len(client.submit('g.V()').all().result()) == 6


def test_client_bytecode(client):
    g = Graph().traversal()
    t = g.V()
    message = RequestMessage('traversal', 'bytecode', {'gremlin': t.bytecode, 'aliases': {'g': 'gmodern'}})
    result_set = client.submit(message)
    assert len(result_set.all().result()) == 6


def test_iterate_result_set(client):
    g = Graph().traversal()
    t = g.V()
    message = RequestMessage('traversal', 'bytecode', {'gremlin': t.bytecode, 'aliases': {'g': 'gmodern'}})
    result_set = client.submit(message)
    results = []
    for result in result_set:
        results += result
    assert len(results) == 6


def test_client_async(client):
    g = Graph().traversal()
    t = g.V()
    message = RequestMessage('traversal', 'bytecode', {'gremlin': t.bytecode, 'aliases': {'g': 'gmodern'}})
    future = client.submitAsync(message)
    result_set = future.result()
    assert len(result_set.all().result()) == 6


def test_connection_share(client):
    # Overwrite fixture with pool_size=1 client
    client = Client('ws://localhost:45940/gremlin', 'gmodern', pool_size=1)
    g = Graph().traversal()
    t = g.V()
    message = RequestMessage('traversal', 'bytecode', {'gremlin': t.bytecode, 'aliases': {'g': 'gmodern'}})
    message2 = RequestMessage('traversal', 'bytecode', {'gremlin': t.bytecode, 'aliases': {'g': 'gmodern'}})
    future = client.submitAsync(message)
    future2 = client.submitAsync(message2)

    result_set2 = future2.result()
    assert len(result_set2.all().result()) == 6

    # This future has to finish for the second to yield result - pool_size=1
    assert future.done()
    result_set = future.result()
    assert len(result_set.all().result()) == 6


def test_multi_conn_pool(client):
    g = Graph().traversal()
    t = g.V()
    message = RequestMessage('traversal', 'bytecode', {'gremlin': t.bytecode, 'aliases': {'g': 'gmodern'}})
    message2 = RequestMessage('traversal', 'bytecode', {'gremlin': t.bytecode, 'aliases': {'g': 'gmodern'}})
    client = Client('ws://localhost:45940/gremlin', 'g', pool_size=1)
    future = client.submitAsync(message)
    future2 = client.submitAsync(message2)

    result_set2 = future2.result()
    assert len(result_set2.all().result()) == 6

    # with connection pool `future` may or may not be done here
    result_set = future.result()
    assert len(result_set.all().result()) == 6
