#!/usr/bin/env python3

input_string = input("Enter a string: ")
i = 0
while i < len(input_string):
	if input_string[i].isupper():
		print(input_string[i].lower(), end="")
	else:
		print(input_string[i].upper(), end="")
	i += 1
