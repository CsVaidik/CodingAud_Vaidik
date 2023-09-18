class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

if __name__ == "__main__":
    animal = Animal()
    dog = Dog()
    cat = Cat()

    animal.speak()  
    dog.speak()     
    cat.speak()     
