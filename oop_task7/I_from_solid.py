#incorrect
# The Robot class inherits the Eater interface, even though robots cannot eat.
# This leads to a situation where Robot must implement an eat method that it does not need.
# This violates the Interface Segregation Principle, since Robot depends on an interface that is not used.

class Worker:
    def work(self):
        pass

class Eater:
    def eat(self):
        pass

class HumanWorker(Worker, Eater):
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Worker, Eater):
    def work(self):
        pass
    def eat(self):
        raise NotImplementedError("Robots don't eat!")



#correct
# Now each class implements only the methods it needs, and interfaces are separated by areas of responsibility.
class Worker:
    def work(self):
        pass

class Eater:
    def eat(self):
        pass

class HumanWorker(Worker, Eater):
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        pass
