class Solution(object):
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]
        x=int(input())
        if isPalindrome(x):
            return True
        else:
            return False