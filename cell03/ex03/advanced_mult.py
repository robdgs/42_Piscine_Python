#!/usr/bin/env python3

"""
try:

	n = int(input())
	multiplier = 0

		print("Table de "+ str(n) + ":", end=" ")
		while multiplier <= 10:
			print(n * multiplier, end=" ")
			multiplier += 1

except ValueError:
    print("none")

the issue here may be that input() in py always return a string.
so the int(input()) call will raise a ValueError if the input is not a number,
and in that case i can't use an if statement to check the input, 
because the ValueError will be raised before the if statement is executed.
so i have to use a try/except block to catch the ValueError and print "none" 
"""

try:

	n = int(input())
	multiplier = 0
	i = 0
		


	while i <= n:
		print("Table de "+ str(i) + ":", end=" ")
		multiplier = 0
		while multiplier <= 10:
			print(i * multiplier, end=" ")
			multiplier += 1
		print()
		i += 1



except ValueError:
    print("none")