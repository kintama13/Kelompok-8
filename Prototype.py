from abc import ABC, abstractmethod
import time

# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(3)
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass  
