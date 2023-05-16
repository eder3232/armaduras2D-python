import numpy as np


class Vertices:
    def __init__(
        self,
        axis=None,
    ):
        if axis is None:
            self.axis = ["x", "y"]
        else:
            self.axis = axis
        self.data = {}

    def add(self, name, coordinates, forces, displacements, isRestricted):
        # validaciones
        # verificar si el name ya existe
        if name in self.data:
            raise Exception("El nodo ya existe! los nodos deben tener un nombtre único.")

        # verificar si los grados de libertad restringidos no
        #  tengan una fuerza aplicada
        for a in self.axis:
            if isRestricted[a] and forces[a] != 0:
                raise Exception(
                    f"El vertice {name} tiene el eje {a} restringido, por lo tanto, no puede tener una fuerza aplicada."
                )
            elif not (isRestricted[a]) and displacements[a] != 0:
                raise Exception(
                    f"El vertice {name} tiene el eje {a} no restringido, por lo tanto, no puede tener un desplazamiento."
                )
        self.data[name] = {
            'coordinates':coordinates,
            'forces':forces,
            'displacements':displacements,
            'isRestricted':isRestricted,
        }
    


eder = Vertices(["x", "y"])

eder.add(
    name="v1",
    coordinates={"x": 0, "y": 0},
    forces={"x": 0, "y": 0},
    displacements={"x": 0, "y": 0},
    isRestricted={"x": False, "y": False},
)

eder.add(
    name="v2",
    coordinates={"x": 3, "y": 0},
    forces={"x": 0, "y": 0},
    displacements={"x": 0, "y": 0},
    isRestricted={"x": False, "y": False},
)

print(eder.__dict__)
