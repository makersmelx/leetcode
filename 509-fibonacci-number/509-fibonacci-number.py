class Solution:
    def fib(self, n: int) -> int:
        first, second = 1,1 
        
        if n == 0 or n == 1:
            return n
        
        for i in range(2, n):
            num = first + second
            first = second
            second = num
        
        return second
        