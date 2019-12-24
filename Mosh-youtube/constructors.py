# a constructor gets called when creating an object
#

class Point:
    # short for initialize.
    def __init__(self, x, y):  # this is a constructor
        self.x = x  # same as saying point.x = 10 in classes.py
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)
print(point.x)