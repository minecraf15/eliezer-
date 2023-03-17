import abc
from abc import ABC

class Animal():
    def set_name(self,nombre):
        pass
    
    def get_name(self):
        pass

    name=abc.abstractproperty(get_name,set_name)

class gato (Animal):
    def __init__(self):
        pass

    def name(self):
        return self._name()
        
    
    def name(self,name):
        self.name= name


gato=gato()
gato.name= "princesa"
print(gato.name)



