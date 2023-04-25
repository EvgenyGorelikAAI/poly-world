from .rayperception import RayPerception
import numpy as np
from scipy.spatial import ConvexHull
from .hit_point_calculation import calc_hit
import matplotlib.pyplot as plt

def rotation_matrix_2d(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

def bbox2d_corners(params: dict):
    '''
        input:
            - params: parameter dict
    '''
    w = params.get("w", 0)
    l = params.get("l", 0)
    x = params.get("x", 0)
    y = params.get("y", 0)
    theta = params.get("theta", 0)
    corners = np.array([[x-l/2, x-l/2, x+l/2, x+l/2],
                        [y-w/2, y+w/2, y-w/2, y+w/2]])
    corners = rotation_matrix_2d(theta) @ corners
    return corners

class RayPerception2D(RayPerception):
    def __init__(self, num_rays=10, fov=np.pi) -> None:
        super().__init__()
        self.num_rays = num_rays
        self.fov = fov

    def get_hits(self, object_list: list):
        rays = self.get_rays()
        hits = list()
        for obj in object_list:
            bb_corners = bbox2d_corners(obj).T
            hull = ConvexHull(bb_corners)
            for ray in rays:
                hit = calc_hit(ray, hull)
                if not np.isinf(np.max(hit)):
                    hits.append(hit)
        hits_array = np.array(hits)
        return hits_array

    def get_rays(self):
        unit_vector = np.array([1,0])
        rays = np.array([rotation_matrix_2d(r) @unit_vector for r in np.linspace(-self.fov/2, self.fov/2, self.num_rays)])
        return rays
