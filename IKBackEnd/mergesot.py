def merge(arr, start, middle, end):
    lefthalf = arr[start : middle + 1]  # Corrected slice notation
    righthalf = arr[middle + 1 : end + 1]  # Corrected slice notation
    i = 0  # The index for the left half
    j = 0  # The index for the right half
    k = start  # The index for the original array

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        arr[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        arr[k] = righthalf[j]
        j += 1
        k += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2  # Use integer division
        merge_sort(arr, start, mid)  # Recursively sort the left half
        merge_sort(arr, mid + 1, end)  # Recursively sort the right half
        merge(arr, start, mid, end)  # Merge the sorted halves


# Example usage:
examplearray = [5, 8, 3, 9, 4, 1, 7]
merge_sort(examplearray, 0, len(examplearray) - 1)
print(examplearray)
