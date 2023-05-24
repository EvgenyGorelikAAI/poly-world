from logic import PerceptionAgent3D
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    agent = PerceptionAgent3D(32,100,np.pi,-np.pi/8)
    bbox_list = [
        {"h": 2., "w": 2., "l": 5., "x": 5.},
        {"h": 2., "w": 2., "l": 5., "x": -5.},
        {"h": 2., "w": 2., "l": 5., "y": 3.},
        {"h": 2., "w": 2., "l": 5., "y": -3.},
    ]  
    points = agent.get_perception(bbox_list)

    ax = plt.axes(projection='3d')
    ax.scatter3D(points[:,0], points[:,1], points[:,2], s=2)
    ax.scatter3D(0, 0, 0, s=5, marker="x")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_proj_type('ortho')
    ax.set_aspect('equal','box')
    ax.view_init(45, 45, 0)
    plt.tight_layout()
    plt.waitforbuttonpress(1)
    plt.cla()

    agent.rotate(np.array([0,0,np.pi/8.]))
    points = agent.get_perception(bbox_list)

    ax.scatter3D(points[:,0], points[:,1], points[:,2], s=2)
    ax.scatter3D(0, 0, 0, s=5, marker="x")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_proj_type('ortho')
    ax.set_aspect('equal','box')
    ax.view_init(45, 45, 0)
    plt.tight_layout()
    plt.waitforbuttonpress(1)
    plt.cla()

    agent.move(np.array([1,0,0],dtype=float))
    points = agent.get_perception(bbox_list)

    ax = plt.axes(projection='3d')
    ax.scatter3D(points[:,0], points[:,1], points[:,2], s=2)
    ax.scatter3D(0, 0, 0, s=5, marker="x")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_proj_type('ortho')
    ax.set_aspect('equal','box')
    ax.view_init(45, 45, 0)
    plt.tight_layout()
    plt.waitforbuttonpress(1)
    plt.cla()