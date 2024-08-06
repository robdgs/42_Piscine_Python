#!/usr/bin/env python3
print("Enter the first number: ")
x = input ()
print(x)
print("Enter the second number: ")
y = input ()
print(y)
mult = int(x) * int(y)
print(x + " * " + y + " = " + str(mult))
if mult < 0:
	print("The result is negative.")
elif mult > 0:
	print("The result is positive.")
else:
	print("The result is both positive and negative.")