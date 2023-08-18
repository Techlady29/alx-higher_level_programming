#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for b in list_ord:
        print("{}: {}".format(b, a_dictionary.get(b)))
