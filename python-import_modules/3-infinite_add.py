#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    result = 0
    if len(argv) == 1:
        print("{}".format(result))
    else:
        for number_arg in range(1, len(argv)):
            result += int(argv[number_arg])
        print("{}".format(result))
