#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listLen = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            listLen += 1
        except IndexError:
            break
    print("")
    return (listLen)
