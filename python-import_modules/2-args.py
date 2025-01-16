#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) - 1 > 0:
        separator_arg = ":"
    else:
        separator_arg = "."
    print("{} argument{}".format(len(argv) - 1, separator_arg))
    for arg_number in range(1, len(argv)):
        print("{}: {}".format(arg_number, argv[arg_number]))
