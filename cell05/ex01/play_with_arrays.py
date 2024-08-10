#!/usr/bin/env python3

nbs = [25, 42, 333, -45, 3734, 2, 25]
print(nbs)

i = 0
while i < len(nbs):
	nbs[i] = nbs[i] + 2
	i += 1
	
print(nbs)