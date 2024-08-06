#!/usr/bin/env python3
print("Enter a number")
n = int(input())
x = 0
while x <= 10:
	print(str(n) + " " + "x" + " " + str(x) + " " + "=" + " " + str(n * x))
	x += 1