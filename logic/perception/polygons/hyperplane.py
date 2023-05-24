from .polygon import Polygon
import numpy as np

class Hyperplane(Polygon):
    def __init__(self, normal_vector: np.ndarray, offset: float) -> None:
        self.dim = normal_vector.size
        self.A = np.hstack([normal_vector,-normal_vector])
        self.b = np.array([offset, -offset])
