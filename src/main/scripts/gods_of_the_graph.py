# Name: Debasish Kanhar
# Emp ID: 05222V

from janusgraph_python.structure.JanusGraph import JanusGraph


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
