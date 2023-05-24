from logic import PerceptionAgent2D
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    agent = PerceptionAgent2D(100,2*np.pi)
    bbox_list = [
        {"h": 2., "w": 2., "l": 5., "x": 5.},
        {"h": 2., "w": 2., "l": 5., "x": -5.},
        {"h": 2., "w": 2., "l": 5., "y": 3.},
        {"h": 2., "w": 2., "l": 5., "y": -3.},
    ]  
    points = agent.get_perception(bbox_list)

    ax = plt.axes()
    ax.scatter(points[:,0], points[:,1])
    ax.set_aspect('equal','box')
    plt.waitforbuttonpress(1)
    plt.cla()

    agent.rotate(np.pi/8.)
    points = agent.get_perception(bbox_list)

    ax.scatter(points[:,0], points[:,1])
    ax.set_aspect('equal','box')

    agent.move(np.array([1,0],dtype=float))
    points = agent.get_perception(bbox_list)
    plt.waitforbuttonpress(1)
    plt.cla()

    ax.scatter(points[:,0], points[:,1])
    ax.set_aspect('equal','box')
    plt.waitforbuttonpress(1)
    plt.cla()
