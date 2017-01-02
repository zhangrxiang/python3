
class Animal:
    def run(self):
        print("Animal run")


animal = Animal()
animal.run()

class Dog(Animal):
    def run(self):
        print("Dog run")


class Cat(Animal):
    pass
dog = Dog()
dog.run()

cat = Cat()
cat.run()
print(isinstance(animal, Animal))
print(isinstance(dog, Dog))
print(issubclass(Dog, Animal))



def run_two(animal):
    animal.run()
    animal.run()
run_two(animal)
run_two(dog)

def dog_run(dog):
    dog.run()
    dog.run()
dog_run(dog)
dog_run(cat)
