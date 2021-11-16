'''Given an array A of size n and an integer K, return all subsets of A which sum to K.

Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.

Note : The order of subsets are not important.

Input format :
Line 1 : Integer n, Size of input array
Line 2 : Array elements separated by space
Line 3 : K 

Sample Input :
9 
5 12 3 17 1 18 15 3 17 
6

Sample Output :
3 3
5 1
'''

import sys
sys.setrecursionlimit(10**6)

def subsetsSumKHelper(arr, startIndex, k):
    if startIndex == len(arr):
        if k == 0:
            return [list()]
        else:
            return list()

    OutputWfe = subsetsSumKHelper(arr, startIndex + 1, k - arr[startIndex])
    OutputWOfe = subsetsSumKHelper(arr, startIndex + 1, k)
    

    output = (len(OutputWOfe) + len(OutputWfe)) * [0]
    index = 0
    for i in range(len(OutputWOfe)):
        output[index] = OutputWOfe[i]
        index+=1

    for i in range(len(OutputWfe)):
        output[index] = (len(OutputWfe[i]) + 1) * [0]
        output[index][0] = arr[startIndex]
        for j in range(len(OutputWfe[i])):
            output[index][j+1] = OutputWfe[i][j]

        index += 1
    return output

def subsetsSumK(arr, k):
    return subsetsSumKHelper(arr,0,k)


# taking input
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr,n

# printint the list of lists
def printListofLists(liOfli):
    for li in liOfli:
        for ele in li:
            print(ele, end=' ')
        print()


# main
arr, n = takeInput()
if n != 0:
    k = int(input().strip())
    liOfli = subsetsSumK(arr, k)

    printListofLists(liOfli)

