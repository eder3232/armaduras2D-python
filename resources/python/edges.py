class Edges:
    def __init__(self, vertices) -> None:
        self.data = {}
        self.vertices = vertices
        self.verticesData = vertices["data"]

    def add(self, name, vertexFrom, vertexTo, area, elasticidad):
        # validaciones
        # verificamos si el name ya existe:
        if name in self.data:
            raise Exception(
                "El nodo ya existe! los nodos deben tener un nombtre único."
            )
        # verificamos si el nombre del vertice que viene es valido
        if not (vertexFrom in self.verticesData):
            raise Exception(
                "El nombre del vertice del que viene, es incorrecto! verifica si este existe en los vertices."
            )
        # verificamos si el nombre del vertice al que va es valido
        if not (vertexTo in self.verticesData):
            raise Exception(
                "El nombre del vertice al que va, es incorrecto! verifica si este existe en los vertices."
            )

        fromX = self.verticesData[vertexFrom]["coordinates"]["x"]
        fromY = self.verticesData[vertexFrom]["coordinates"]["y"]

        toY = self.verticesData[vertexTo]["coordinates"]["y"]
        toX = self.verticesData[vertexTo]["coordinates"]["x"]

        longitud = ((toX - fromX) ** 2 + (toY - fromY) ** 2) ** 0.5
        rigidez = elasticidad * area / longitud

        cos = (toX - fromX) / longitud
        sin = (toY - fromY) / longitud

        fromDOFx = self.verticesData[vertexFrom]["DOF"]["x"]
        fromDOFy = self.verticesData[vertexFrom]["DOF"]["y"]
        toDOFx = self.verticesData[vertexTo]["DOF"]["x"]
        toDOFy = self.verticesData[vertexTo]["DOF"]["y"]

        tableDOF = [
            fromDOFx,
            fromDOFy,
            toDOFx,
            toDOFy,
        ]

        self.data[name] = {
            "name": name,
            "area": area,
            "elasticidad": elasticidad,
            "longitud": longitud,
            "rigidez": rigidez,
            "cos": cos,
            "sin": sin,
            "tableDOF": tableDOF,
        }

    def getData(self):
        return {"edges": self.data, "vertices": self.vertices}



