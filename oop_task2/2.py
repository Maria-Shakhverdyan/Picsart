class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.setPrice(price)
    
    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        return self.__author
    
    def getPrice(self):
        return self.__price
    
    def setTitle(self, title):
        self.__title = title
    
    def setAuthor(self, author):
        self.__author = author
    
    def setPrice(self, price):
        if price > 10:
            self.__price = price
        else:
            raise ValueError("The price must be greater 10.")
    
    def printInfo(self):
        print(f"Title -> {self.getTitle()}, author -> {self.getAuthor()}, price -> {self.getPrice()}.")


try:
    war_and_peace = Book("War and Peace", "Leo Tolstoy", 30)
    war_and_peace.printInfo()

    war_and_peace.setPrice(3)
    war_and_peace.printInfo()
except ValueError as e:
    print("Error", e)