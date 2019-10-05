#using attributes
class Dog():
    species = "mammal" #class object attribute
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "Lab", name = "Scooby")
print(mydog.breed)
print(mydog.name)
print(mydog.species)

#using methods
class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * Circle.pi
mycirc = Circle(5)
print(mycirc.area())

#inheritance
class Animal():
    def __init__(self):
        print("Animal created")
    def whoAmI(self):
        print("Animal")
    def food(self):
        print("beef")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def food(self):
        print("dog mash")

mydog = Dog()
mydog.whoAmI()
mydog.food()


#special methods

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: {}, Author: {} Pages: {}".format(self.title,self.author,self.pages)
    
b = Book("javascript","Millern",300)
print(b)
        
