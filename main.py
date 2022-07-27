## author: Kunj Shukla
## Project: github.com/kunjshukla/Project3
## file: main.py
## license: MIT license

# Importing required libiraies.
from time import time

# Importing Project src code.
from algorithms.bubble_sort import __bubble_sort 

def main():
    test_array = [1, 3, 5, 45, 6, 57, 67, 8, 65, 7, 34]
    print(f"\nOriginal Array: {test_array}"); start = time()
    print(f"Sorted Array: {__bubble_sort(test_array)}")
    print(f"Time Taken: {time()-start} seconds\n")

if __name__ == "__main__":
    main()

