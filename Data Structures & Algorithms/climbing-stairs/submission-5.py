class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev, curr = 1, 2
        for _ in range(3, n+1):
            temp = prev
            prev = curr
            curr = temp + prev
        
        return curr
        
