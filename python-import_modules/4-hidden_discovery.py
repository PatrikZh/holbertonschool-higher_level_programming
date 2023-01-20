#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    enter = dir(hidden_4)
    for i in enter:
        if i[:2] != "__":
            print("{}".format(enter))
