from typing import *


def is_number(element: Any) -> bool:
    return isinstance(element, int) or isinstance(element, float)


class Complex:

    def __init__(self, real: Union[int, float], imaginary: Union[int, float]):
        assert is_number(real) and is_number(imaginary)
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: Union["Complex", int, float]):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        assert is_number(other)
        return self + Complex(other, 0)

    def __mul__(self, other: Union["Complex", int, float]):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)
        assert is_number(other)
        return self + Complex(other, 0)

    def __repr__(self):
        return f"Complex(real={self.real}, imaginary={self.imaginary})"

    def __str__(self):
        return f"{self.real} + i * {self.imaginary}"


def main():
    print(str(Complex(1, 0) + Complex(-4, 0)))
    first = Complex(1, 2)
    second = Complex(4, 5)
    print(str(first + second))
    print(str(first * second))


if __name__ == '__main__':
    main()
