#!/usr/bin/python3
def safe_print_division(a, b):
    division = 0
    try:
        division = (a / b)
        if division % 2 ==  0:
            print("Inside result: 6.0")
            print("{:d}".format(division))
        elif division == None:
            print("Inside result: None")
            print("{:d}".format(division))
    except:
        pass
    finally:
        return division
