#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.
#For example, 121 is a palindrome while 123 is not.

def isPalindrome(int):
    forward = []
    backward = []
    for digit in str(int):
        forward.append(digit)
    for i in range(len(forward)):
        n = len(forward)-1-i
        backward.append(forward[n])
    if forward == backward:
        return True
    else:
        return False

print(isPalindrome(24882))

