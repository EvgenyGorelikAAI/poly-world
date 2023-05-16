import numpy as np
from logic.perception import RayPerception2D
from .perception_agent import PerceptionAgent
from .utils import (
    bbox2reference,
    array_from_dict
)

class PerceptionAgent2D(PerceptionAgent):
    def __init__(self, num_layers=1, num_points_per_layer=1, fov=np.pi, tilt=-np.pi/8) -> None:
        super().__init__()
        self.perception = RayPerception2D(num_rays=100, fov=np.pi)
        self.position = np.zeros(2)
        self.rotation = 0.

    def move(self, vector: np.ndarray):
        assert vector.shape == (2,), "Wrong input shape"
        self.position += vector

    def set_position(self, vector: np.ndarray):
        assert vector.shape == (2,), "Wrong input shape"
        self.position = vector.astype(np.float64)
    
    def rotate(self, shift: float):
        self.rotation += shift

    def set_rotation(self, shift: float):
        self.rotation = float(shift)
    
    def get_perception(self, object_list: list):
        '''
            transpose all objects in the list to the view of the agent
        '''
        bbox_list = list()
        for o in object_list:
            bbox_list.append({
                    "x": o.get("x", 0) - self.position[0],
                    "y": o.get("y", 0) - self.position[1],
                    "w": o.get("w", 0),
                    "l": o.get("l", 0),
                    "yaw": o.get("yaw", 0) - self.rotation
            })
        return self.perception.get_hits(bbox_list)