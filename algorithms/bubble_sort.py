## author: Kunj Shukla
## Project: github.com/kunjshukla/Project3
## file: bubble_sort.py
## license: MIT license


def __bubble_sort(array: list) -> list:
    '''
    __bubble_sort uses the the bubble sort algorithm to sort a given array/list in incrementing order and returns it.

    @param: name: array
            type: list
            The array to be sorted.
    @return: returns the sorted array.
    '''
    array_size = len(array)
    swapped = False
    sorted_array = array

    for i in range(array_size - 1):
        for j in range(array_size - i - 1):
            if sorted_array[j] > sorted_array[j + 1]:
                swapped = True
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
        
        if not swapped:
            break

    return sorted_array
                   
