from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class cow(animal):
    def sound(self):
        print("Moo")

a = cow()
a.sound()
