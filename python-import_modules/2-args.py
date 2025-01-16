#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) - 1 == 1:
        print("{} argument:".format(len(argv) - 1))
    elif len(argv) - 1 > 1:
        print("{} arguments:".format(len(argv) - 1))
    else:
        print("{} arguments.".format(len(argv) - 1,))
    for arg_number in range(1, len(argv)):
        print("{}: {}".format(arg_number, argv[arg_number]))
