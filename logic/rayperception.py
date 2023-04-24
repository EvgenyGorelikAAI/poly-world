import numpy as np
from scipy.spatial import ConvexHull
from logic.bbox_calculation import bbox_corners
from logic.hit_point_calculation import calc_hit
from logic.utils import spherical2cartesian
import matplotlib.pyplot as plt

class RayPerception():
    def __init__(self, num_layers, num_points_per_layer, fov=np.pi, tilt=-np.pi/8) -> None:
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

    def get_lidar_points(self, objects_in_scene: list):
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
    
if __name__=="__main__":
    lidar_sim = RayPerception(32, 100, fov=np.pi/2, tilt=np.pi/4)
    rays = lidar_sim.get_rays()

    ax = plt.axes(projection='3d')
    ax.scatter3D(rays[:,0], rays[:,1], rays[:,2], s=2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_proj_type('ortho')
    ax.set_aspect('equal','box')
    ax.view_init(45, 45, 0)
    plt.tight_layout()
    plt.show()

    objects_in_scene = [{"h" : 1, "w" : 2, "l" : 5, "x" : 10, "y" : 0, "z" : 0, "yaw" : np.pi/4}]
    points = lidar_sim.get_lidar_points(objects_in_scene)

    ax = plt.axes(projection='3d')
    ax.scatter3D(points[:,0], points[:,1], points[:,2], s=2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_proj_type('ortho')
    ax.set_aspect('equal','box')
    ax.view_init(45, 45, 0)
    plt.tight_layout()