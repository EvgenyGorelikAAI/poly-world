from logic import RayPerception3D
import numpy as np
import matplotlib.pyplot as plt

    
if __name__=="__main__":
    lidar_sim = RayPerception3D(32, 100, fov=np.pi/2, tilt=np.pi/4)
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
    points = lidar_sim.get_hits(objects_in_scene)

    ax = plt.axes(projection='3d')
    ax.scatter3D(points[:,0], points[:,1], points[:,2], s=2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_proj_type('ortho')
    ax.set_aspect('equal','box')
    ax.view_init(45, 45, 0)
    plt.tight_layout()
    plt.show()