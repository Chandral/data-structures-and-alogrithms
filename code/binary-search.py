"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    start = 0
    end = len(input_array)
    midpoint = int(((end-start)/2) + start)
    while end != midpoint:
        print("~")
        mid_val = input_array[midpoint]
        if value < mid_val:
            end = midpoint
            midpoint = int(((end - start) / 2) + start)
        elif value > mid_val:
            start = midpoint+1
            midpoint = int(((end - start) / 2) + start)
        elif value == mid_val:
            return midpoint
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
# print([binary_search(test_list, i) for i in test_list])
# print(binary_search(test_list, -1))
# print(binary_search(test_list, 30))
print(binary_search(test_list, 1))