class Dog:
    attr="Mammal"
    def __init__(self,name) -> None:
        self.name=name
        pass
    def speak(self):
        print(f"My name is {self.name} and I am a {self.attr} ")



Rodger = Dog("Rodger")
Tommy = Dog("Tommy")


Rodger.speak()
Tommy.speak()

