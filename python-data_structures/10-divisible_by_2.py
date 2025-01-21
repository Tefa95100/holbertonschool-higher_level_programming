#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    verif_list = []

    for index in my_list:
        if my_list[index] % 2 == 0:
            verif_list.append(True)
        else:
            verif_list.append(False)

    return verif_list
