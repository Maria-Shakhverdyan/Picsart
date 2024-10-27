from abc import ABC, abstractmethod
from typing import List

class CarInterface(ABC):
    @abstractmethod
    def car_info(self):
        ...

class Car(CarInterface):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__make = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__model = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self.__price = value
    
    def car_info(self):
        return f"The car make: {self.make}, model: {self.model}, price: {self.price}"

class ElectricCar(Car):
    def __init__(self, make, model, price, battery):
        super().__init__(make, model, price)
        self.battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self.__battery = value
    
    def car_info(self):
        return f"Electric car, make: {self.make}, model: {self.model}, price: {self.price}, battery: {self.battery}"

class HybridCar(Car):
    def __init__(self, make, model, price, fuel):
        super().__init__(make, model, price)
        self.fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self.__fuel = value

    def car_info(self):
        return f"Hybrid car, make: {self.make}, model: {self.model}, price: {self.price}, fuel: {self.fuel}"

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.purchased_cars: List[Car] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__contact_info = value
    
    def search_car(self, model_name):
        for car in self.purchased_cars:
            if model_name == car.model:
                return car
        return None

    def buy_car(self, car):
        self.purchased_cars.append(car)

class SalesOperations(ABC):
    @abstractmethod
    def sell_car(self, customer, car):
        ...
    
    @abstractmethod
    def add_car(self, car):
        ...
    
    @abstractmethod
    def view_sales_history(self):
        ...

class Salesperson(SalesOperations):
    def __init__(self, name: str, commission_rate: float):
        self.name = name
        self.commission_rate = commission_rate
        self.sales_history: List[Car] = []
        self.inventory: List[Car] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def commission_rate(self):
        return self.__commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self.__commission_rate = value
    
    def sell_car(self, customer, car):
        if car in self.inventory:
            customer.buy_car(car)
            self.sales_history.append(car)
            self.inventory.remove(car)
            print(f"{self.__name} sold {car.car_info()}")
        else:
            print(f"{car.car_info()} is not in inventory")
    
    def add_car(self, car):
        self.inventory.append(car)
    
    def view_sales_history(self):
        print("Sales history: ")
        for car in self.sales_history:
            print(car.car_info())

if __name__ == "__main__":
    salesperson = Salesperson("Maria", 5)

    car1 = ElectricCar("Wolkswagen", "Model ID4", 40000, 450)
    car2 = HybridCar("Audi", "A6", 30000, 20)

    salesperson.add_car(car1)
    salesperson.add_car(car2)

    customer = Customer("Maria", "maria@example.com")

    salesperson.sell_car(customer, car1)

    salesperson.view_sales_history()
