"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one: list, list_two: list):
    if len(list_one) == len(list_two):
        i = 0
        while i < len(list_one):
            if list_one[i] != list_two[i]:
                return UNEQUAL
            i += 1
        return EQUAL
    elif len(list_one) < len(list_two):
        i = 0
        while i <= len(list_two) - len(list_one):
            j = 0
            while j < len(list_one) and list_two[i + j] == list_one[j]:
                j += 1
            if j == len(list_one):
                return SUBLIST
            i += 1
        return UNEQUAL
    else:
        i = 0
        while i <= len(list_one) - len(list_two):
            j = 0
            while j < len(list_two) and list_one[i + j] == list_two[j]:
                j += 1
            if j == len(list_two):
                return SUPERLIST
            i += 1
        return UNEQUAL

        
