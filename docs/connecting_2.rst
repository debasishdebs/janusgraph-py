==========================
Connecting to JanusGraph
==========================

The library defines a Structure class named JanusGraph running in
Gremlin Server mode.

For information about Gremlin Server, refer to `JanusGraph docs
<https://docs.janusgraph.org/latest/server.html>`_.

==================
JanusGraph Client
==================

The JanusGraph client provided as part of JanusGraph-Python is used to open either **traversal()** object
or a **management()** object which means the corresponding thing as in JVM JanusGraph clients.

===============================
Initializing JanusGraph Client
===============================

The client provided to connect to JanusGraph expects that the JanusGraph is already running in Gremlin Server
mode. The client provided registers all the default Serializers and Deserializers required to support the features as
part of this release.

The Serializers and Deserializers registered as part of JanusGraph Python's default registry would be
GeoShape (Point & Circle), RelationIdentifier. If new data types / object specific to JanusGraph are added in future
release, the same needs to be added to Client registry.

The JanusGraph object provides a *connect()* method to connect to a a running instance of JanusGraph in Gremlin
Server mode. The API interface is as follows:

.. code-block::python

    from janusgraph_python.structure.JanusGraph import JanusGraph

    # Create a JanusGraph object, and connect to running instance of JanusGraph Server
    graph = JanusGraph().connect(url="0.0.0.0", port="8182", graph="g")


==============================
Opening Traversal for Queries
==============================

The client provided with JanusGraph provides 2 APIs to open either Traversal connection or Management connection
either depending on requirements like either Querying data or Schema management.

Data can be queries using GLVs as follows:

.. code-block::python

    from janusgraph_python.structure.JanusGraph import JanusGraph

    # Create a JanusGraph object, and connect to running instance of JanusGraph Server
    graph = JanusGraph().connect(url="0.0.0.0", port="8182", graph="g")

    # Create Traversal
    g = graph.traversal()

    g.V().count().next()
    ==> 0


=========================================
Opening Management for Schema Management
=========================================

