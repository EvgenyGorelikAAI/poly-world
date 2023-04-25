from abc import ABC, abstractmethod
from typing import Any

class PerceptionAgent(ABC):
    
    @abstractmethod
    def move(self, m: Any):
        raise NotImplementedError
    
    @abstractmethod
    def rotate(self, m: Any):
        raise NotImplementedError
    
    @abstractmethod
    def set_position(self, m: Any):
        raise NotImplementedError
    
    @abstractmethod
    def set_rotation(self, m: Any):
        raise NotImplementedError