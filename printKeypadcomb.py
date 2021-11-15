'''
Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.
Note : The order of strings are not important. Just print different strings in new lines.
Input Format :
Integer n
Output Format :
All possible strings in different lines

Sample Input:
23

Sample Output:
ad
ae
af
bd
be
bf
cd
ce
cf
'''

def getString(digit):
    if digit == 2:
        return 'abc'
    if digit == 3:
        return 'def'
    if digit == 4:
        return 'ghi'
    if digit == 5:
        return 'jkl'
    if digit == 6:
        return 'mno'
    if digit == 7:
        return 'pqrs'
    if digit == 8:
        return 'tuv'
    if digit == 9:
        return 'wxyz'
    else:
        return ' '


def printKeypadComb(n, output):
    if n == 0:
        print(output)
        return

    smallint = n//10
    remDigit = n%10

    optionsForLastDigit = getString(remDigit)
    for c in optionsForLastDigit:
        newOutput = c + output
        printKeypadComb(smallint, newOutput)

printKeypadComb(23,'')

## CN Solution

'''
def printKeypadHelper(num, str):
    options = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    if (num == 0):
        print(str)
        return

    small = num//10
    remainder = num%10
    optionslen = len(options[remainder])
    if (optionslen == 0):
        printKeypadHelper(num, str)
        return

    for i in range(0, optionslen):
        printKeypadHelper(small, options[remainder][i] + str)

def printKeypad(num):
    printKeypadHelper(num, '')

n = int(input())
printKeypad(n)     
'''