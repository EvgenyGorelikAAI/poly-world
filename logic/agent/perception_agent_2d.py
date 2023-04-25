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
        self.position = np.zeros(3)
        self.rotation = np.zeros(3)

    def move(self, vector: np.ndarray):
        assert vector.shape == (3,), "Wrong input shape"
        self.position += vector

    def set_position(self, vector: np.ndarray):
        assert vector.shape == (3,), "Wrong input shape"
        self.position = vector.astype(np.float64)
    
    def rotate(self, vector: np.ndarray):
        assert vector.shape == (3,), "Wrong input shape"
        self.rotation += vector

    def set_rotation(self, vector: np.ndarray):
        assert vector.shape == (3,), "Wrong input shape"
        self.rotation = vector.astype(np.float64)
    
    def get_perception(self, object_list: list):
        '''
            transpose all objects in the list to the view of the agent
        '''
        bbox_list = list()
        reference_system = np.concatenate([self.position, self.rotation])
        for o in object_list:
            bbox_list.append(bbox2reference(array_from_dict(o), reference_system))
        return self.perception.get_hits(bbox_list)