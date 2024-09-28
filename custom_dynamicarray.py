from typing import Any, Iterator
from copy import deepcopy

class DynamicArray:
    def __init__(self, capacity: int = 1000) -> None:
        self.__size = 0
        self.__capacity = capacity
        self.__array = [None] * capacity
    
    def __len__(self) -> int:
        return self.__size
    
    def capacity(self) -> int:
        return self.__capacity
    
    def __getitem__(self, index: int) -> Any:
        if index >= self.__size:
            raise IndexError("Index must be positive number")
        else:
            return self.__array[index]
        
    def __setitem__(self, index: int, new_item: Any) -> None:
        if index < 0 or index >= self.__size:
            raise IndexError("Index must be positive number")
        else:
            self.__array[index] = new_item
    
    def resize(self, new_capacity: int) -> None:
        new_array = [None] * new_capacity
        for i in range(self.__size):
            new_array[i] = self.__array[i]
        self.__capacity = new_capacity
        self.__array = new_array

    def append(self, new_item: Any) -> None:
        if self.__size == self.__capacity:
            self.resize(2 * self.__capacity)
        self.__array[self.__size] = new_item
        self.__size += 1
    
    def __str__(self) -> str:
        return "[" + ", ".join(str(self.__array[i]) for i in range(self.__size)) + "]"
    
    def __repr__(self) -> str:
        return f"DynamicArray([{', '.join(repr(self.__array[i]) for i in range(self.__size))}])"
    
    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        result = DynamicArray(self.__size + other.__size)
        for i in range(self.__size):
            result.append(self.__array[i])
        for i in range(other.__size):
            result.append(other.__array[i])
        return result
    
    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        for i in range(other.__size):
            if self.__size == self.__capacity:
                self.resize(2 * self.__capacity)
            self.append(other.__array[i])
        return self

    def __eq__(self, other: 'DynamicArray') -> bool:
        if not isinstance(other, DynamicArray):
            return False
        if self.__size != other.__size:
            return False
        for i in range(self.__size):
            if self.__array[i] != other.__array[i]:
                return False
        return True
    
    def __lt__(self, other: 'DynamicArray') -> bool:
        return self.__size < other.__size
    
    def __le__(self, other: 'DynamicArray') -> bool:
        return self.__size <= other.__size
    
    def __gt__(self, other: 'DynamicArray') -> bool:
        return self.__size > other.__size
    
    def __ge__(self, other: 'DynamicArray') -> bool:
        return self.__size >= other.__size
    
    def __iter__(self) -> Iterator[Any]:
        self.__index = 0
        return self
    
    def __next__(self) -> Any:
        if self.__index < self.__size:
            result = self.__array[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration
    
    def __copy__(self) -> 'DynamicArray':
        new_array = DynamicArray(self.__capacity)
        new_array.__size = self.__size
        new_array.__array = self.__array[:self.__size]
        return new_array
    
    def __deepcopy__(self, memo) -> 'DynamicArray':
        new_array = DynamicArray(self.__capacity)
        new_array.__size = self.__size
        new_array.__array = deepcopy(self.__array[:self.__size], memo)
        return new_array

def main():
    arr1 = DynamicArray()
    print("Created an empty array:", arr1)
    
    arr1.append(1)
    arr1.append(2)
    arr1.append(3)
    print("Array after adding elements:", arr1)
    
    print("Length of the array:", len(arr1))
    
    print("Capacity of the array:", arr1.capacity())
    
    print("Element at index 1:", arr1[1])
    arr1[1] = 20
    print("Array after modifying the element at index 1:", arr1)
    
    print("User-friendly representation of the array:", str(arr1))
    print("Official representation of the array:", repr(arr1))
    
    for i in range(4, 11):
        arr1.append(i)
    print("Array after adding elements (triggering capacity increase):", arr1)
    print("Capacity after increase:", arr1.capacity())

    arr2 = DynamicArray()
    arr2.append(10)
    arr2.append(11)
    print("Second array:", arr2)
    
    arr3 = arr1 + arr2
    print("Result of adding arr1 and arr2:", arr3)

    arr1 += arr2
    print("Array arr1 after operation += with arr2:", arr1)

    print("arr1 == arr2?", arr1 == arr2)
    print("arr1 < arr2?", arr1 < arr2)
    print("arr1 <= arr2?", arr1 <= arr2)
    print("arr1 > arr2?", arr1 > arr2)
    print("arr1 >= arr2?", arr1 >= arr2)

    print("Iterating over array arr1:")
    for value in arr1:
        print(value, end=' ')
    print()

if __name__ == "__main__":
    main()
