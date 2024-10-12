#incorrect
# In this example, the Penguin class inherits from Bird, but the penguin cannot fly,
# which violates the Liskov principle. If the code assumes that any bird can fly, then calling the
# fly() method on the Penguin object will cause incorrect behavior.
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")

#correct
# To follow the Liskov principle, one must either revise the class hierarchy or make
# a more correct division into classes with different abilities (for example,
# divide birds into those that fly and those that do not).
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying")

class Penguin(Bird):
    def move(self):
        print("Penguin is walking")
