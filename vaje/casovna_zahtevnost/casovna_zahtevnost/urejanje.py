from merilnik import *

def bubbleSort(arr):
    n = len(arr)
    bol = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                bol = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]     
        if not bol:
            return
        
        
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1
 
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
 
        
