#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0

    for a in range(x):
        try:
            print("{}".format(my_list[a]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            n += 1
    print('')
    return(n)
