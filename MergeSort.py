'''
Sort an array A using Merge Sort.
Change in the input array itself. So no need to return or print anything.
Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)
Output format :
Array elements in increasing order (separated by space)
Constraints :
1 <= n <= 10^3
Sample Input 1 :
6 
2 6 8 5 4 3
Sample Output 1 :
2 3 4 5 6 8
Sample Input 2 :
5
2 1 5 2 3
Sample Output 2 :
1 2 2 3 5 
'''


def merge(arr1, arr2, arr):
    i = 0
    j = 0
    k = 0
    n = len(arr1)
    m = len(arr2)

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr[k] = arr2[j]
            k += 1
            j += 1
    while i < n:
        arr[k] = arr1[i]
        k += 1
        i += 1

    while j < m:
        arr[k] = arr2[j]
        k += 1
        j += 1


def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    mergeSort(arr1)
    mergeSort(arr2)
    merge(arr1, arr2, arr)

# def mergeSort(arr, start, end):
#     size = end -start
#     if size<=1:
#         return

#     mid = (start+end)//2
#     mergeSort(arr,start,mid)
#     mergeSort(arr,mid,end)

#     result = [0]*size
#     i = start
#     j = mid
#     k = 0

#     while i<mid and j<end:
#         if arr[i]<arr[j]:
#             result[k] = arr[i]
#             k+=1
#             i+=1
#         else:
#             result[k] = arr[j]
#             k+=1
#             j+=1
#     while i<mid:
#         result[k] = arr[i]
#         k+=1
#         i+=1
#     while j<end:
#         result[k] = arr[j]
#         k+=1
#         j+=1
#     for i in range(0,size):
#         arr[start + i] = result[i]



# main
n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
mergeSort(arr)
for num in arr:
    print(num, end=" ")
print()