#incorrect
# In this code, the Switch class depends directly on the Lamp class. If we want to change the lamp
# to another type of device, such as a fan, we would have to change the code in the Switch class.
# This violates the Dependency Inversion Principle, since the high-level module (Switch) depends on the low-level module (Lamp).
class Lamp:
    def turn_on(self):
        print("Lamp is on")
        
    def turn_off(self):
        print("Lamp is off")

class Switch:
    def __init__(self, lamp):
        self.lamp = lamp
        
    def operate(self, command):
        if command == "on":
            self.lamp.turn_on()
        elif command == "off":
            self.lamp.turn_off()



#correct
# Now if we want to use a fan instead of a light bulb, we don't need to change the switch code,
# we just pass it another object that implements the Device interface.
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class Lamp(Device):
    def turn_on(self):
        print("Lamp is on")
        
    def turn_off(self):
        print("Lamp is off")

class Fan(Device):
    def turn_on(self):
        print("fan is on")
        
    def turn_off(self):
        print("fan is off")

class Switch:
    def __init__(self, device: Device):
        self.device = device
        
    def operate(self, command):
        if command == "on":
            self.device.turn_on()
        elif command == "off":
            self.device.turn_off()

lamp = Lamp()
fan = Fan()

switch1 = Switch(lamp)
switch2 = Switch(fan)

switch1.operate("on")
switch2.operate("on")
