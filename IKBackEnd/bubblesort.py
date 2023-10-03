# Given a list of numbers, sort it using the Bubble sort algorithm
# arr: [5, 8, 3, 9, 4, 1, 7]
# first find the number values in arr
def bubblesort(arr):
    n = len(arr)  # n is numberofvaluesinarray
    for i in range(
        0, n - 1
    ):  # n-1 is telling us to iterate and stop at the last value of arr=5 because by then in Bubble sort theory is that the last number will be sorted by that time so we only need to make 4 passes
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubblesort([5, 8, 3, 9, 4, 1, 7]))
