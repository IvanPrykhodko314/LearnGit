class myClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old")

p1 = myClass("John", 36)
# Call the greet method
myClass.greet(p1)
