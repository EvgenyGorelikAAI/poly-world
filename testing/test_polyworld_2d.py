from logic.generator import PolyWorld2D
import matplotlib.pyplot as plt


if __name__=="__main__":
    world = PolyWorld2D()
    perception = world.get_perception()
    plt.scatter(perception[:,0], perception[:,1])
    plt.show()

