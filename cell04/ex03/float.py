#!/usr/bin/env python3

x = input("Give me a number: ")

try:
    float_x = float(x)
    if float_x.is_integer():
        print("This number is an Integer")
    else:
        print("This number is a decimal")
except ValueError:
    print("NaN")