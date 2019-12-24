# inheritance is good for reusing code.
#

class Dog:
    def walk(self):
        print("walk")

# what if you want to define another class in the future?
# you have to repeat the whole code
# if there is an error, or you want to change it, you have to go through and fix it in ALL the classes
class Cat:
    def walk(self):
        print("walk")


# multiple approaches to stop this, one of the approaches is inheritance.
