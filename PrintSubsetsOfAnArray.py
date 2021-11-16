'''
Given an integer array (of length n), find and print all the subsets of input array.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.

Note : The order of subsets are not important. Just print the subsets in different lines.
Input format :
Line 1 : Integer n, Size of array
Line 2 : Array elements (separated by space)

Constraints :
1 <= n <= 15

Sample Input:
3
15 20 12

Sample Output:
[] (this just represents an empty array, don't worry about the square brackets)
12 
20 
20 12 
15 
15 12 
15 20 
15 20 12 
'''

import sys
sys.setrecursionlimit(10**6)


def printsubsetHelper(arr, lst):
    n = len(arr)
    if (n==0):
        for number in lst:
            print(number, end = ' ')
        print()
        return

    printsubsetHelper(arr[1:], lst)
    newlst = lst.copy()
    newlst.append(arr[0])
    printsubsetHelper(arr[1:], newlst)
    return


def printsubset(arr):
    printsubsetHelper(arr,[])

n = int(input())
arr = list(int(i) for i  in input().strip().split(' '))
printsubset(arr)