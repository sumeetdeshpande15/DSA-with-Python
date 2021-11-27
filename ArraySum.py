'''
Given an array of length N, you need to find and print the sum of all elements of the array.

Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Sample Input :
3
9 8 9

Sample Output :
26
'''

def ArraySum(arr):
    sum = 0
    for i in arr:
        sum += i
    print(sum)

n = int(input())
arr = [int(x) for x in input().split()]
ArraySum(arr)

'''
n = int(input())

li = [int(x) for x in input().split()]
sum = 0
for ele in li:
    sum += ele
print(sum)
'''