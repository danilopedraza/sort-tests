# insertion-sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

# merge-sort and its subroutines
def merge(arr, copy, start, mid, end):
    i, j, k = start, mid, start
    while i < mid and j < end:
        if arr[i] <= arr[j]:
            copy[k] = arr[i]
            i += 1
        else:
            copy[k] = arr[j]
            j += 1
        k += 1
    
    while i < mid:
        copy[k] = arr[i]
        i += 1
        k += 1
    while j < end:
        copy[k] = arr[j]
        j += 1
        k += 1
    for i in range(start, end):
        arr[i] = copy[i]

def mergeSortHelper(arr, copy, start, end):
    if (start + 1 >= end):
        return
    # else...
    mid = (start + end) // 2

    mergeSortHelper(arr, copy, start, mid)
    mergeSortHelper(arr, copy, mid, end)
    merge(arr, copy, start, mid, end)

def mergeSort(arr):
    copy = [0] * len(arr)
    mergeSortHelper(arr, copy, 0, len(arr))

# counting-sort
def countingSort(arr, leftLimit, rightLimit):
    freqs = [0] * (rightLimit - leftLimit + 1)
    new = [0] * len(arr)

    for i in range(len(arr)):
        freqs[arr[i] - leftLimit] += 1
    
    for i in range(1, len(freqs)):
        freqs[i] += freqs[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        new[freqs[arr[i] - leftLimit] - 1] = arr[i]
        freqs[arr[i] - leftLimit] -= 1
    
    #for i in range(len(arr)):
    #    arr[i] = new[i]
    arr[:] = new
