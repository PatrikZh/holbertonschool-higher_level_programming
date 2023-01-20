#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv) - 1
    if arg == 0:
        print("0 arguments:")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(l))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
