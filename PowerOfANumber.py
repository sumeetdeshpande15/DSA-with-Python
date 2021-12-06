'''
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1


Input format :
Two integers x and n (separated by space)
Output Format :
x^n (i.e. x raise to the power n)
Constraints:
0 <= x <= 8 
0 <= n <= 9
Sample Input 1 :
3 4
Sample Output 1 :
81
Sample Input 2 :
2 5
Sample Output 2 :
32
'''

li = input().split()
x = int(li[0])
n = int(li[1])


ans = 1

while n > 0:
    ans *= x
    n -= 1

print(ans)


# a, b = input().split()
# a = int(a)
# b = int(b)

# if b == 0:
#     print("1")
# else:
#     print(a**b)