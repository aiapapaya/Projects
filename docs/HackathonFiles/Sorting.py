"""
Author: Thelma Ofoegbu
Purpose: Sorting Algorithms implementation
"""

# Bubble Sort Algorithm
def bubble_sort(arr, key=lambda x: x):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Insertion Sort Algorithm
def insertion_sort(arr, key=lambda x: x):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key_val = key(arr[i])
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and key(arr[j]) > key_val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_val
    return arr



# Selection Sort Algorithm
def selection_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if key(arr[j]) < key(arr[min_idx]):
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Quick Sort Algorithm
def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []
    for x in arr:
        if key(x) < key(pivot):
            left.append(x)
        elif key(x) == key(pivot):
            middle.append(x)
        else:
            right.append(x)
    # Recursively sort the left and right sublists, and concatenate them with the middle list
    return quick_sort(left, key) + middle + quick_sort(right, key)


# Merge Sort Algorithm

def mergesort(arr, key=lambda x: x):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        mergesort(left_arr, key)
        mergesort(right_arr, key)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if key(left_arr[i]) <= key(right_arr[j]):
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):#To check if there are elements remaining in the left array
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):# To check if there are elements remaining in the right array
            arr[k] = right_arr[j]
            j += 1
            k += 1



#HeapSort Algorithm
def heap_sort(arr, key = lambda x: x ):
    len_arr = len(arr)
    # Build a max heap
    for i in range(len_arr // 2 - 1, -1, -1):
        max_heapify(arr, len_arr, i, key)

    # Extract elements one by one
    for i in range(len_arr - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        max_heapify(arr, i, 0, key)

def max_heapify(arr, len_arr, i, key):
    largest = i
    l_child = 2 * i + 1
    r_child = 2 * i + 2

    if l_child < len_arr and key(arr[l_child]) > key(arr[largest]):
        largest = l_child

    if r_child < len_arr and key(arr[r_child]) > key(arr[largest]):
        largest = r_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, len_arr, largest, key)