#!/usr/bin/python3

for index in range(0, 26):
    print("{}".format(chr(122 - index) if index % 2 == 0
                      else chr(90 - index)), end='')
