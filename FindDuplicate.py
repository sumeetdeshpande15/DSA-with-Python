'''
You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these, there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.
Note :
Duplicate number is always present in the given array/list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.
Output Format :
For each test case, print the duplicate element in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
Time Limit: 1 sec
Sample Input 1:
1
9
0 7 2 5 4 7 1 3 6
Sample Output 1:
7
Sample Input 2:
2
5
0 2 1 3 1
7
0 3 1 5 4 3 2
Sample Output 2:
1
3
'''

import sys

def duplicateNumber(arr, n):
    d={}
    for i in arr:
        d[i] = d.get(i,0) + 1
    for key in d:
        if d[key] == 2:
            return key

'''
def duplicateNumber(arr,size):
    for i in range(size-1):
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                return arr[i]

    The function would never return form this line since the input array always contains a duplicate value.

    To avoid the ambiguity at the compile time, the function necessarily has to return a value in case the line number 51 doesn't return the desired value during the execution of the for loop.

    return sys.maxsize
'''

#Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0:

    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1