#__str__, __repr__, __ad__, __sub__, __mul__, __truediv__, __eq__, __hash__, __float__, __int__, __neg__

from math import gcd
from typing import Union

class Custom_fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ZeroDivisionError
        common = gcd(numerator, denominator)
        self.__numerator = numerator // common * (1 if denominator > 0 else -1)
        self.__denominator = abs(denominator) // common
    
    def __str__(self) -> str:
        return f"{self.__numerator}/{self.__denominator}"
    
    def __repr__(self) -> str:
        return f"Fraction({self.__numerator},{self.__denominator})"
    
    def __ad__(self, other: Union['Custom_fraction', int]) -> 'Custom_fraction':
        if isinstance(other, int):
            other = Custom_fraction(other, 1)
        if not isinstance(other, Custom_fraction):
            return NotImplemented
        num = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        den = self.__denominator * other.__denominator
        return Custom_fraction(num, den)
    
    def __sub__(self, other: Union['Custom_fraction', int]) -> 'Custom_fraction':
        if isinstance(other, int):
            other = Custom_fraction(other, 1)
        if not isinstance(other, Custom_fraction):
            return NotImplemented
        num = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        den = self.__denominator * other.__denominator
        return Custom_fraction(num, den)
    
    def __mul__(self, other: Union['Custom_fraction', int]) -> 'Custom_fraction':
        if isinstance(other, int):
            other = Custom_fraction(other, 1)
        if not isinstance(other, Custom_fraction):
            return NotImplemented
        num = self.__numerator * other.__numerator
        den = self.__denominator * other.__denominator
        return Custom_fraction(num, den)
    
    def __truediv__(self, other: Union['Custom_fraction', int]) -> 'Custom_fraction':
        if isinstance(other, int):
            other = Custom_fraction(other, 1)
        if not isinstance(other, Custom_fraction):
            return NotImplemented
        if other.__numerator == 0:
            raise ZeroDivisionError
        num = self.__numerator * other.__denominator
        den = self.__denominator * other.__numerator
        return Custom_fraction(num, den)
    
    def __eq__(self, other: Union['Custom_fraction', int]) -> bool:
        if isinstance(other, int):
            other = Custom_fraction(other, 1)
        if not isinstance(other, Custom_fraction):
            return NotImplemented
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator

    def __hash__(self) -> int:
        return hash((self.__numerator, self.__denominator))
    
    def __float__(self) -> float:
        return self.__numerator / self.__denominator
    
    def __int__(self) -> int:
        return self.__numerator // self.__denominator
    
    def __neg__(self) -> 'Custom_fraction':
        return Custom_fraction(-self.__numerator, self.__denominator)
    
if __name__ == "__main__":
    fraction1 = Custom_fraction(1, 2)
    fraction2 = Custom_fraction(-2, 5)
    fraction3 = Custom_fraction(3, 4)
    fraction4 = Custom_fraction(5, 3)

    print(f"fraction1: {fraction1}")
    print(f"fraction2: {fraction2}")
    print(f"fraction3: {fraction3}")
    print(f"fraction4: {fraction4}")

    print(f"fraction1 + fraction2 = {fraction1.__ad__(fraction2)}")
    print(f"fraction3 - fraction1 = {fraction3 - fraction1}")
    print(f"fraction1 * fraction4 = {fraction1 * fraction4}")
    print(f"fraction4 / fraction2 = {fraction4 / fraction2}")

    print(f"fraction1 == fraction3: {fraction1 == fraction3}")
    print(f"fraction1 == Custom_fraction(2, 4): {fraction1 == Custom_fraction(2, 4)}")

    print(f"float(fraction1) = {float(fraction1)}")
    print(f"int(fraction1) = {int(fraction1)}")

    print(f"Negative of fraction1: {-fraction1}")
    print(f"Hash of fraction1: {hash(fraction1)}")

    fraction_set = {fraction1, fraction2, Custom_fraction(2, 4)}
    print(f"Set with fractions: {fraction_set}")
