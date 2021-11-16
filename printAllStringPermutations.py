'''
Given a string, find and print all the possible permutations of the input string.
Note : The order of permutations are not important. Just print them in different lines.

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

def printPermutationsHelper(string, permutation):
    if len(string)==0:
        print(permutation)
        return

    for i in range(len(string)):
        currChar = string[i]
        newStr = string[:i] + string[i+1:]
        printPermutationsHelper(newStr, permutation+currChar)

def printPermutation(string):
    return printPermutationsHelper(string, '')


## CN Solution

'''
def printPermutationsHelper(string, output):
    if len(string) == 0:
        print(output)
        return
        
        
    for i in range(len(string)):
        printPermutationsHelper(string[:i] + string[i+1:], output + string[i])
        
def printPermutations(string):
    printPermutationsHelper(string, '')
    
'''

string = input() 
printPermutation(string)