class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def eat(self):
        print(f'{self.name} eats')
    
    def walk(self):
        print(f'{self.name} walks')
    
    def run(self):
        print(f'{self.name} runs')

class Male(Person):
    pass

class Female(Person):
    pass

ram = Male("Ram", 27, "Ayodhya")
sita = Female("Sita", 25, "Janakpur")

ram.eat()
sita.eat()
ram.walk()
sita.run()