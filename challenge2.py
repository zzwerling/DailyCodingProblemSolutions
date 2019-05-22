# Problem 2
# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the original array except the one at i.

def new_array(array):
    result = []

    for e_index, e in enumerate(array):
        value = 1
        for e_index2, elem2 in enumerate(array):

            if e_index2 != e_index:
                value *= elem2

        result.append(value)

    return result


