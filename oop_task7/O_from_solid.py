#incorrect
# If you need to add a new shipping method, you need to change the class code, which violates the OCP principle.

class ShippingCostCalculator:
    def calculate(self, shipping_method, weight):
        if shipping_method == "ground":
            return weight * 1.5
        elif shipping_method == "air":
            return weight * 3.0
        else:
            raise ValueError("Unknown shipping method")


#correct
# Instead of changing the class every time a new delivery method is added, we can
# use polymorphism and extend functionality with new classes without touching the existing code.
from abc import ABC, abstractmethod

class ShippingMethod(ABC):
    @abstractmethod
    def calculate_cost(self, weight):
        pass

class GroundShipping(ShippingMethod):
    def calculate_cost(self, weight):
        return weight * 1.5

class AirShipping(ShippingMethod):
    def calculate_cost(self, weight):
        return weight * 3.0

class ShippingCostCalculator:
    def __init__(self, method: ShippingMethod):
        self.method = method

    def calculate(self, weight):
        return self.method.calculate_cost(weight)
