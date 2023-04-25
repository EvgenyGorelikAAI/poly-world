import matplotlib.pyplot as plt
from logic.perception import RayPerception2D 
import numpy as np


if __name__=="__main__":
    lidar_sim = RayPerception2D(100, fov=np.pi*2)
    rays = lidar_sim.get_rays()

    ax = plt.axes()
    ax.scatter(rays[:,0], rays[:,1])
    ax.set_aspect('equal','box')
    plt.show()
    
    objects_in_scene = [{"w" : 2, "l" : 5, "x" : 5, "y" : 5, "yaw" : 0.2}]
    points = lidar_sim.get_hits(objects_in_scene)

    ax = plt.axes()
    ax.scatter(points[:,0], points[:,1])
    ax.set_aspect('equal','box')
    plt.show()