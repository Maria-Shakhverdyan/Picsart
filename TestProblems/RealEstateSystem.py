from typing import List
from abc import ABC, abstractmethod

class Property:
    def __init__(self, address, price, features):
        self.address = address
        self.price = price
        self.features = features

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("Address must be a string")
        if value == "":
            raise ValueError("Address cannot be empty")
        self.__address = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self.__price = value
    
    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        if not isinstance(value, str):
            raise TypeError("Features must be a string")
        if value == "":
            raise ValueError("Features cannot be empty")
        self.__features = value
    
    def property_info(self):
        return f"Address: {self.address}, Price: ${self.price}, Features: {self.features}"

    
class PropertyType(ABC):
    @abstractmethod
    def show_property_type(self):
        pass

class ResidentialProperty(Property, PropertyType):
    def show_property_type(self):
        return "Residential Property"

class CommercialProperty(Property, PropertyType):
    def show_property_type(self):
        return "Commercial Property"

class Agent:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.listings: List[Property] = []
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError("contact_info must be a string")
        if value == "":
            raise ValueError("contact_info cannot be empty")
        self.__contact_info = value

    def add_property(self, property: Property):
        self.listings.append(property)
    
    def manage_properties(self):
        return [property.property_info() for property in self.listings]

class Client:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.purchased_properties: List[Property] = []
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError("contact_info must be a string")
        if value == "":
            raise ValueError("contact_info cannot be empty")
        self.__contact_info = value
    
    def search_properties(self, properties: List[Property]):
        return [property.property_info() for property in properties]

    def purchase_property(self, property: Property):
        self.purchased_properties.append(property)
        return f"{self.name} purchased {property.property_info()}"



agent1 = Agent("John Doe", "john.doe@realestate.com")

property1 = ResidentialProperty("Azatutyan street", 3500000, "5 bed, 2 baths, 1500 sqft")
property2 = CommercialProperty("Charents street", 1000000, "3000 sqft, office space")

agent1.add_property(property1)
agent1.add_property(property2)

client1 = Client("Maria", "maria@gmail.com")

available_properties = agent1.manage_properties()
print("Available properties:", available_properties)

print(client1.purchase_property(property1))

print("Purchased properties:", [prop.property_info() for prop in client1.purchased_properties])
