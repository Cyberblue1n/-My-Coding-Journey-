class animal:
    def sound(self):
        return "some sound"
class dog(animal):
    def sound(self):
        return "Bhaw bhaw"
class cat(animal):
    def sound(self):
        return "meaw"
    
animals = [dog(), cat(), animal()]
for i in animals:
    print(i.sound())