#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    outcome = []
    for i in range(list_length):
        try:
            div_total = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_total = 0
        except ZeroDivisionError:
            print("division by 0")
            div_total = 0
        except IndexError:
            print("out of range")
            div_total = 0
        finally:
            outcome.append(div_total)
        return outcome

