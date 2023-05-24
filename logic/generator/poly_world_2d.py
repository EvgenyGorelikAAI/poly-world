from .poly_world import PolyWorld
from logic.perception.polygons import Hyperplane, BoundingBox
from logic.agent import PerceptionAgent2D

import numpy as np


class PolyWorld2D(PolyWorld):
    def __init__(self, **parameters) -> None:
        super().__init__()
        self.object_parameters = parameters.get("object_parameters", {
            "num_objects" : 10,
            "size_range" : (2,10)
        }) 
        self.world_size = parameters.get("world_size", (100,100))
        self.agent_parameters = parameters.get("agent", {
            "num_layers": 10,
            "num_points_per_layer": 100, 
            "fov": np.pi,
            "tilt": 0.2
        })
        self.generate()

    def generate(self):
        self.agent = PerceptionAgent2D(**self.agent_parameters)
        self.perception = self.agent.perception

        self.objects = []

        for i in range(self.object_parameters["num_objects"]):
            self.objects.append(BoundingBox({
                "h":    1, 
                "w":    self.object_parameters["size_range"][1],
                "l":    self.object_parameters["size_range"][0], 
                "x":    np.random.rand() * self.world_size[0], 
                "y":    np.random.rand() * self.world_size[1], 
                "z":    0, 
                "roll": 0,
                "pitch":0,
                "yaw":  np.random.randn()
            }))
    
    def get_perception(self):
        return self.agent.get_perception(self.objects)

    def control_agent(self, action):
        return super().control_agent(action)

    def _PolyWorld__agent(self):
        return self.agent
    
    def _PolyWorld__perception(self):
        return self.perception