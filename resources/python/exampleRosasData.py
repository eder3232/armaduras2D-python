verticesInstance = Vertices(["x", "y"])

verticesInstance.add(
    name="v1",
    coordinates={"x": 0, "y": 0},
    forces={"x": 0, "y": 0},
    displacements={"x": 0, "y": 0},
    isRestricted={"x": True, "y": True},
)
verticesInstance.add(
    name="v2",
    coordinates={"x": 3, "y": 0},
    forces={"x": 0, "y": 0},
    displacements={"x": 0, "y": 0},
    isRestricted={"x": True, "y": True},
)
verticesInstance.add(
    name="v3",
    coordinates={"x": 0, "y": 4},
    forces={"x": 4.8, "y": -6.4},
    displacements={"x": 0, "y": 0},
    isRestricted={"x": False, "y": False},
)
verticesInstance.add(
    name="v4",
    coordinates={"x": 3, "y": 4},
    forces={"x": 0, "y": -6},
    displacements={"x": 0, "y": 0},
    isRestricted={"x": False, "y": False},
)

dataVertices=verticesInstance.getData()
pprint.pprint(dataVertices)


edgesInstance = Edges(dataVertices)

edgesInstance.add(
    name="e1",
    vertexFrom="v1",
    vertexTo="v2",
    area=10 * 10**-4,
    elasticidad=2 * 10**7,
)
edgesInstance.add(
    name="e2",
    vertexFrom="v3",
    vertexTo="v4",
    area=10 * 10**-4,
    elasticidad=2 * 10**7,
)
edgesInstance.add(
    name="e3",
    vertexFrom="v1",
    vertexTo="v3",
    area=10 * 10**-4,
    elasticidad=2 * 10**7,
)
edgesInstance.add(
    name="e4",
    vertexFrom="v2",
    vertexTo="v4",
    area=10 * 10**-4,
    elasticidad=2 * 10**7,
)
edgesInstance.add(
    name="e5",
    vertexFrom="v1",
    vertexTo="v4",
    area=10 * 10**-4,
    elasticidad=2 * 10**7,
)
edgesInstance.add(
    name="e6",
    vertexFrom="v2",
    vertexTo="v3",
    area=10 * 10**-4,
    elasticidad=2 * 10**7,
)


dataEdgesFullData = edgesInstance.getData()
dataEdges = edgesInstance.getData()['edges']

pprint.pprint(dataEdges)