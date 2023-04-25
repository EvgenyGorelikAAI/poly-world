import numpy as np
from scipy.spatial import ConvexHull
from .hit_point_calculation import calc_hit
from .utils import spherical2cartesian, bbox_corners

class RayPerception3D():
    def __init__(self, num_layers, num_points_per_layer, fov=np.pi, tilt=-np.pi/8) -> None:
        super().__init__()
        self.num_layers = num_layers
        self.num_points_per_layer = num_points_per_layer
        self.fov = fov
        self.tilt = tilt
        
    def get_rays(self):
        azimuths = np.linspace(-np.pi, np.pi, self.num_points_per_layer)
        rays = np.zeros((0,3))
        for e in np.linspace(-np.pi + self.tilt, -np.pi + self.tilt + self.fov, self.num_layers):
            rays = np.concatenate([rays,spherical2cartesian(np.ones(len(azimuths)), azimuths, e*np.ones(len(azimuths)))])
        return rays

    def get_hits(self, objects_in_scene: list):
        '''
            assume ray starts in (0,0,0)
        '''
        rays = self.get_rays()
        hits = list()
        for obj in objects_in_scene:
            bb_corners = bbox_corners(obj).T
            hull = ConvexHull(bb_corners)
            for ray in rays:
                hit = calc_hit(ray, hull)
                if not np.isinf(np.max(hit)):
                    hits.append(hit)
        hits_array = np.array(hits)
        return hits_array
