'''
Given an array A of random integers and an integer k, find and return the kth largest element in the array.
Note: Try to do this question in less than O(N * logN) time.


Sample Input 1 :
6
9 4 8 7 11 3
2
Sample Output 1 :
9

Sample Input 2 :
8
2 6 10 11 13 4 1 20
4
Sample Output 2 :
10
'''

import heapq
def kthLargest(lst, k):
    for i in range(k-1):
        heapq._heapify_max(lst)
        heapq._heappop_max(lst)
    return lst[0]

## CN Solution ##
'''
def kthLargest(lst,k):
    minHeap = []
    heapq.heapify(minHeap)
    n = len(lst)
    for i in range(0,k):
        heapq.heappush(minHeap,lst[i])
    for i in range(k,n):
        if lst[i]>minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap,lst[i])
        return minHeap[0]
'''
# Main
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
k = int(input())
ans = kthLargest(lst,k)
print(ans)