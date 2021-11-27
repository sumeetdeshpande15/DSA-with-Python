def SelectionSort(arr):
    length = len(arr)
    # put correct element at the ith position
    for i in range(length-1):
        minIndex = i
        # calculating the index of minimum element for this iteration
        for j in range(i+1, length):
            if (arr[j] < arr[minIndex]):
                minIndex = j
            arr[i], arr[minIndex] = arr[minIndex],arr[i]

arr = [int(x) for x in input().split()]
SelectionSort(arr)
print(*arr)