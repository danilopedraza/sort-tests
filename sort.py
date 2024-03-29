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
def countingSort(arr, leftLimit=1, rightLimit=5000):
    freqs = [0] * (rightLimit - leftLimit + 1)
    ordered = [0] * len(arr)

    for i in range(len(arr)):
        freqs[arr[i] - leftLimit] += 1
    
    for i in range(1, len(freqs)):
        freqs[i] += freqs[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        ordered[freqs[arr[i] - leftLimit] - 1] = arr[i]
        freqs[arr[i] - leftLimit] -= 1
    
    #for i in range(len(arr)):
    #    arr[i] = new[i]
    arr[:] = ordered

# heap-sort and its subroutines
def siftDown(arr, length, i):
    maxIndex = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < length and arr[left] > arr[maxIndex]:
        maxIndex = left
    if right < length and arr[right] > arr[maxIndex]:
        maxIndex = right

    if i != maxIndex:
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
        siftDown(arr, length, maxIndex)

def heapSort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        siftDown(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        siftDown(arr, i, 0)

# quick-sort and its subroutines
def partition(arr, left, right):
    x = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quickSortHelper(arr, left, right):
    if left >= right:
        return
    # else...
    pivot = partition(arr, left, right)
    
    quickSortHelper(arr, left, pivot - 1)
    quickSortHelper(arr, pivot + 1, right)

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)


sortingAlgorithms = [
    insertionSort,
    mergeSort,
    countingSort,
    heapSort,
    quickSort
]
