# inheritance is good for reusing code.


class Mammal:
    def walk(self):
        print("walk")


# just need to call the main class
class Dog(Mammal):
    def bark(self):
        print("bark")
        # this is specific to Dog only


# what if you want to define another class in the future?
# you have to repeat the whole code
# if there is an error, or you want to change it, you have to go through and fix it in ALL the classes
class Cat(Mammal):
    pass  # this is needed because python does not like empty classes. It basically says, "skip this line"


dog1 = Dog()
dog1.walk()
dog1.bark()


# multiple approaches to stop this, one of the approaches is inheritance.
