#!/usr/bin/env python
__author__ = 'Viktor Filinskij'


def main():
    a = float('inf')   # infinity
    b = float('-inf')  # infinity
    print(f"a = a^2: { a == a ** 2 }")
    print(f"a = a * 2: { a == a * 2 }")
    print(f"a > 99999: { a > 99999 }")


if __name__ == '__main__':
    main()
