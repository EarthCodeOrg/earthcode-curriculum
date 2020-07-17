# Classes / Objects
# Most data structures in python are objects
# An object is anything that has class paramaters and/or functions
# aka it's anything that has certain features and certain methods to operate on

# A simple dog class could be:
# objects always have Capital first letters and otherwise follow function naming conventions
class Dog():
    # every Class must have an __init__ function, 
    # this describes the how the Object is created
    def __init__(self, name, furColor):
        #print("I am a Dog")
        # class parameter for the name of the dog
        self.name = name
        self.furColor = furColor
        self.noseState = "wet"
        self.paws = ["clean","clean","clean","clean"] 
        
    # this is a function that allows us to read the name of this dog
    def getName(self): # we need to use the self keyword for every clas function
        return self.name
    
    def setName(self, name):
        # we might want to have a whole function to setting any parameter 
        # because we want to check if that parameter is valid
        if (len(name) < 3):
            print("Name is too short: " + name)
            return
        self.name = name
        
dog_1  = Dog("hank", "pink")
#print(dog_1.name)
dog_2 = Dog("fred", "black")
#print(dog_1.name) # it's sometimes considered unsafe to access class parameters directly
#print(dog_2.getName()) 
    
# We can inherit from classes to keep class logic contained, extensible and modular
class ABigDog(Dog): # we write Dog in the ( ) of the class definition to indicate that ABigDog Inherits all the logic, all the methods from Dog
    def __init__(self, furColor):
        Dog.__init__(self, name, furColor)
        
    def jumpReallyHigh(self):
        print("Woof")
        
big_boi_1 = ABigDog("Big Hank")
print(big_boi_1.getName())
big_boi_1.jumpReallyHigh()
        
