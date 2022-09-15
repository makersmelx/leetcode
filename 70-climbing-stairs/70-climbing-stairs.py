class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2
        if n < 3:
            return n
        for i in range(3,n+1):
            tmp = first + second
            first = second
            second = tmp
        
        return tmp