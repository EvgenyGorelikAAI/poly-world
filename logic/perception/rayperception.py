from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class RayPerception(ABC):

    @abstractmethod
    def get_hits(self, m: Any):
        raise NotImplementedError

    @abstractmethod
    def get_rays(self):
        raise NotImplementedError
    
    @abstractproperty
    def stochastic(self):
        raise NotImplementedError