from abc import ABC

class Polygon(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.A = None
        self.b = None

    @property
    def A(self):
        return self.A

    @property
    def b(self):
        return self.b
