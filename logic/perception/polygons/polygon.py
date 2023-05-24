from abc import ABC

class Polygon(ABC):
    def __init__(self) -> None:
        super().__init__()

    @property
    def A(self):
        return self._A

    @property
    def b(self):
        raise self._b
