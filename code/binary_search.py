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
    end = len(input_array) - 1
    first = True
    while start != end:
        if end - start == 1 and first:
            first = False
        elif end-start == 1:
            end = start
        dividing = end - start
        half_way = int(dividing/2)
        mid_point = start + half_way
        if value == input_array[mid_point]:
            return mid_point
        elif value < input_array[mid_point]:
            end = mid_point
        elif value > input_array[mid_point]:
            start = mid_point
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val2 = 25
test_val1 = 15
print(binary_search(test_list, test_val1))
print("~" * 25)
print(binary_search(test_list, test_val2))
