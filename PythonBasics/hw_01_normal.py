#!/usr/bin/env python
__author__ = 'Viktor Filinskij'

import random
from math import sqrt

def main():

    def find_max(num):
        max_digest = 0
        while num != 0:
            if max_digest < num % 10:
                max_digest = num % 10
            num //= 10
        return max_digest

    def swap_val(v1, v2):
        # in case v1 and v2 are integers we can use:
        # a = a*b
        # b = int(a / b)
        # a = int(a / b)
        # return f"a = { a }, b = { b }"
        v3 = v1
        v1 = v2
        v2 = v3
        return v1, v2

    def find_x(ax, bx, cx):
        # a*x^2 + b*x + c = 0
        # D = b^2 - 4*a*c
        d = bx ** 2 - 4 * ax * cx
        if d > 0:
            x1 = (-bx + sqrt(d)) / (2 * ax)
            x2 = (-bx - sqrt(d)) / (2 * ax)
            return f"x1 = { x1 }, x2 = { x2 }"
        elif d == 0:
            x = -(bx/2 * ax)
            return f"x1=x2 = { x }"
        else:
            return "no solution without complex numbers"

    number = random.randint(1, 999999)
    val1 = input("Enter 1st value to swap: ")
    val2 = input("Enter 2nd value to swap: ")
    print("Describe square equations")
    a = float(input("Enter ax: "))
    b = float(input("Enter bx: "))
    c = float(input("Enter ax: "))

    print(f"Largest digit in { number }: { find_max(number) }")
    print(f"Swapping values { val1 }, { val2 }: { swap_val(val1,val2) }")
    print(f"quadratic equation solution: { find_x(a, b, c) }")


if __name__ == '__main__':
    main()
