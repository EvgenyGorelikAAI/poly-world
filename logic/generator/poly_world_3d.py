from logic.perception.polygons import Hyperplane, Polygon
from logic.agent import PerceptionAgent3D
from .poly_world import PolyWorld

import numpy as np


class PolyWorld3D(PolyWorld):
    def __init__(self) -> None:
        super().__init__()

    def generate(self):
        self.floor = Hyperplane(np.array(0,0,1), 0)