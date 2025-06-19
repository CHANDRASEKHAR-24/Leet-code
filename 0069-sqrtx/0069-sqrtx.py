class Solution:
    def mySqrt(self, x: int) -> int:
        num = (x >> 1) + 2    #same as num = (x // 2) + 1
        while num*num > x:
            num = (num + (x // num)) >> 1;     #same as num = (num + (x//num)) // 2

        return num