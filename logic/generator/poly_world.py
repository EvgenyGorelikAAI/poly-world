from abc import ABC, abstractmethod, abstractproperty

class PolyWorld(ABC):
    
    @abstractmethod
    def generate(self):
        raise NotImplementedError
    
    @abstractmethod
    def control_agent(self, action):
        raise NotImplementedError
    
    @abstractmethod
    def get_perception(self):
        raise NotImplementedError
    
    @abstractproperty
    def __agent(self):
        raise NotImplementedError

    @abstractproperty
    def __perception(self):
        raise NotImplementedError