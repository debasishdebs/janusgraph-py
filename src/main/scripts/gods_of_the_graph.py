# Name: Debasish Kanhar
# Emp ID: 05222V

from janusgraph_python.structure.JanusGraph import JanusGraph
from janusgraph_python.core.datatypes.GeoShape import GeoShape


if __name__ == '__main__':
    graph = JanusGraph().connect(url="13.71.86.240", port="8182", bindings="g", graph="graph")

    # Create Schema
    management = graph.openManagement()

    nameBuilder = management.propertyKeyBuilder()
    name = nameBuilder.makePropertyKey("name").dataType("String").make()
    print("Build prop name")
    nameIndexBuilder = management.buildCompositeIndex("name", "Vertex")
    nameIdx = nameIndexBuilder.addKey("name").unique().make()
    print("Build index name")

    ageBuilder = management.propertyKeyBuilder()
    age = ageBuilder.makePropertyKey("age").dataType("Integer").make()
    print("Build prop age")
    ageIdxBuilder = management.buildMixedIndex("vertices", "Vertex")
    ageIdx = ageIdxBuilder.addKey("age").make("search")
    print("Build idx age")

    time = management.propertyKeyBuilder().makePropertyKey("time").dataType("Integer").make()
    print("Buld prop time")
    reason = management.propertyKeyBuilder().makePropertyKey("reason").dataType("String").make()
    print("Build prop reason")
    place = management.propertyKeyBuilder().makePropertyKey("place").dataType("Geoshape").make()
    print("Build prop place")

    edgeIdBuilder = management.buildMixedIndex("edges", "Edge")
    edgeIdBuilder.addKey("reason").make("search")
    print("Build idx reason")

    father = management.edgeLabelBuilder().makeEdgeLabel("father").multiplicity("MANY2ONE").make()
    print("Build edge father")
    mother = management.edgeLabelBuilder().makeEdgeLabel("mother").multiplicity("MANY2ONE").make()
    print("Build edge mother")
    battled = management.edgeLabelBuilder().makeEdgeLabel("battled").signature("time").make()
    print("Build edge battled")
    lives = management.edgeLabelBuilder().makeEdgeLabel("lives").signature("reason").make()
    print("Build edge lives")
    pet = management.edgeLabelBuilder().makeEdgeLabel("pet").make()
    print("Build edge pet")
    
    battledIdxBuilder = management.buildVertexCentricIndex("battlesByTime")
    battledIdx = battledIdxBuilder.addEdge("battled").direction("BOTH").order("decr").on(["time"]).make()
    print("Build edge idx battles")

    titan = management.vertexLabelBuilder().makeVertexLabel("titan").make()
    print("Build vertex titan")
    location = management.vertexLabelBuilder().makeVertexLabel("location").make()
    print("Build vertex location")
    god = management.vertexLabelBuilder().makeVertexLabel("god").make()
    print("Build vertex god")
    demigod = management.vertexLabelBuilder().makeVertexLabel("demigod").make()
    print("Build vertex demigod")
    human = management.vertexLabelBuilder().makeVertexLabel("human").make()
    print("Build vertex human")
    monster = management.vertexLabelBuilder().makeVertexLabel("monster").make()
    print("Build vertex monster")

    graph.commit()
    # Once committed, we can't use any of graph's methods and hence can't use traversal.
    # We will need to create another JanusGraph object before continuing.

    graph = JanusGraph().connect(url="13.71.86.240", port="8182", bindings="g", graph="graph")

    # Adding Data now
    g = graph.traversal()
    print("Adding vertices")
    # Vertices
    saturn = g.addV("titan").property("name", "saturn").property("age", 10000).next()
    sky = g.addV("location").property("name", "sky").next()
    sea = g.addV("location").property("name", "sea").next()
    jupiter = g.addV("god").property("name", "jupiter").property("age", 5000).next()
    neptune = g.addV("god").property("name", "neptune").property("age", 4500).next()
    hercules = g.addV("demigod").property("name", "hercules").property("age", 30).next()
    alcmene = g.addV("human").property("name", "alcmene").property("age", 45).next()
    pluto = g.addV("god").property("name", "pluto").property("age", 4000).next()
    nemean = g.addV("monster").property("name", "nemean").next()
    hydra = g.addV("monster").property("name", "hydra").next()
    cerberus = g.addV("monster").property("name", "cerberus").next()
    tartarus = g.addV("location").property("name", "tartarus").next()
    print("Vertices added successfully")

    print("Adding Edges")
    # Edges
    g.V(jupiter).as_("from").V(saturn).addE("father").from_("from").next()
    # or
    # g.V(saturn).as_("to").V(jupiter).addE("father").to("to").next()
    g.V(jupiter).as_("from").V(sky).addE("lives").property("reason", "loves fresh breezes").from_("from").next()
    g.V(jupiter).as_("from").V(neptune).addE("brother").from_("from").next()
    g.V(jupiter).as_("from").V(pluto).addE("brother").from_("from").next()

    g.V(neptune).as_("from").V(sea).addE("lives").property("reason", "loves waves").from_("from").next()
    g.V(neptune).as_("from").V(jupiter).addE("brother").from_("from").next()
    g.V(neptune).as_("from").V(pluto).addE("brother").from_("from").next()

    g.V(hercules).as_("from").V(jupiter).addE("father").from_("from").next()
    g.V(alcmene).as_("from").V(hercules).addE("mother").from_("from").next()
    pt1 = GeoShape.Point(38.1, 23.7)
    g.V(hercules).as_("from").V(nemean).addE("battled").property("time", 1).property("place", pt1).next()
    pt1 = GeoShape.Point(37.7, 23.9)
    g.V(hercules).as_("from").V(hydra).addE("battled").property("time", 2).property("place", pt1).next()
    pt1 = GeoShape.Point(39, 22)
    g.V(hercules).as_("from").V(cerberus).addE("battled").property("time", 12).property("place", pt1).next()

    g.V(pluto).as_("from").V(jupiter).addE("brother").from_("from").next()
    g.V(pluto).as_("from").V(neptune).addE("brother").from_("from").next()
    g.V(pluto).as_("from").V(tartarus).addE("lives").property("reason", "no fear of death").from_("from").next()
    g.V(pluto).as_("from").V(cerberus).addE("pet").from_("from").next()

    g.V(cerberus).as_("from").V(tartarus).addE("lives").from_("from").next()

    print("Added Edges")

    graph.commit()

    graph = JanusGraph().connect(url="13.71.86.240", port="8182", bindings="g", graph="graph")
    g = graph.traversal()

    print("Counts")
    print("Vertex: ", g.V().count().next())
    print("Edge: ", g.E().count().next())
