#!/usr/bin/env python3

nbs = [2, 8, 9, 48, 8, 22, -12, 2]

print(nbs)

i = 0
nbs.reverse()

while i < len(nbs):
	if nbs[i] < 5:
		nbs.pop(i)

	elif nbs[i] > 5:
		nbs[i] = nbs[i] + 2
		i+=1
	
nbs_pro = set(nbs)

print(nbs_pro)