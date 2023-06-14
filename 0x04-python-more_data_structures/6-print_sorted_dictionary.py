#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_k = sorted(a_dictionary.key())
    for key in sorted_k:
        print("{}: {}".format(k, a_dictionary[key]))
