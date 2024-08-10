#!/usr/bin/env python3

nbs = [3, 42, 333, -45, 3734, 2, 25]

print(nbs)

i = 0
while i < len(nbs):
	if nbs[i] < 5:
		nbs.pop(i)

	if nbs[i] > 5:
		nbs[i] = nbs[i] + 2
	i+=1
	
print(nbs)