from abc import ABC, abstractmethod, abstractproperty
class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass