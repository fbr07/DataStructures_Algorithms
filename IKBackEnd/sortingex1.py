# Question: Given a list of numbers, sort it using the Selection Sort Algorithm


def selectionsort(arr):
    sortarr = 0
    for i in range(0, len(arr)):
        if arr[i] < arr[1 - 1]:
            sortarr += 1
    return sortarr
