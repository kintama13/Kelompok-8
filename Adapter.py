from abc import ABC, abstractmethod

class IUkPlug(ABC):
    
    @staticmethod
    @abstractmethod
    def electricity_220v():
        """electricity supply, in VOLT"""
        
class UkPlug(IUkPlug):
    
    def electricity_220v(self):
        print("220 Volt")
        
class IUsSocket(ABC):
    
    @staticmethod
    @abstractmethod
    def electricity_110v():
        """electricity supply"""
        
class UsSocket(IUsSocket):
    
    def electricity_110v(self):
        print("110 Volt")
        
class UktoUsAdapter(IUkPlug):
    
    def __init__(self):
        self.us_socket = UsSocket()
        
    def electricity_220v(self):
        self.us_socket.electricity_110v()

my_plug = UkPlug()
my_plug.electricity_220v()
my_plug = UktoUsAdapter()
my_plug.electricity_220v()