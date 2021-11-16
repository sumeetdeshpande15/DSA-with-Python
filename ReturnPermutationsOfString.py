'''
Return Permutations of a String
Send Feedback
Given a string, find and return all the possible permutations of the input string.
Note : The order of permutations are not important.

Sample Input :
abc
Sample Output :
abc
acb
bac
bca
cab
cba

'''

def permutations(string, i):
    if i == len(string):
        output.append(''.join(string))
    for j in range(i, len(string)):
        string[i], string[j] = string[j], string[i]
        permutations(string, i+1)
        string[i], string[j] = string[j], string[i]

output = []
string = input()
permutations(list(string), 0)
for i in output:
    print(i)