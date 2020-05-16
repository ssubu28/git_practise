
class Aquatic:
    def __init__(self, name):
        print("Aquatic INIT")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming."

    def greet(self):
        return f"{self.name} says 'Hi!'"



class Ambulatory:
    def __init__(self, name):
        print("Ambulatory INIT")
        self.name = name

    def walk(self):
        return f"{self.name} is walking."

    def greet(self):
        return f"{self.name} says 'Hello!'"



class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("Penguin INIT")
        super().__init__(name=name)
        #Aquatic.__init__(name=name)



p = Penguin('Blue')

print(p.greet()) # prints from Ambulatory class since it it defined first in python. Also init only runs for ambulatory, not aquatic
print(p.swim())
print(p.walk())

# to check method of order resolution for inheritance - use __mro__ or mro() or help(<class name>)
#help(Penguin)

print(Penguin.__mro__)