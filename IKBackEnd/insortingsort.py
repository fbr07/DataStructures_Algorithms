# Given a list of numbers, sort it using the Insertion Sort Algorith


def insertionSort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        left_j_checker = i - 1
        while left_j_checker >= 0 and current_element < arr[left_j_checker]:
            tmp = arr[left_j_checker + 1]
            arr[left_j_checker + 1] = arr[left_j_checker]
            arr[left_j_checker] = tmp
            left_j_checker -= 1
    return arr


print(insertionSort([5, 8, 3, 9, 4, 1, 7]))
