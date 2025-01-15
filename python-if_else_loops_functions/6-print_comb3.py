#!/usr/bin/python3
for decade in range(10):
    for digit in range(10):
        if decade != digit and decade < digit:
            if decade != 8 and digit or digit != 9:
                print("{}{}".format(decade, digit), end=', ')
            else:
                print("{}{}".format(decade, digit))
