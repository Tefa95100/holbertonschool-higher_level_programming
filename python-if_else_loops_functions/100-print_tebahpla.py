#!/usr/bin/python3

for index in range(0, 26):
	if index % 2 == 0:
		ascii = 122 - index
	else:
		ascii = 90 - index
	print("{}".format(chr(ascii)), end='')
