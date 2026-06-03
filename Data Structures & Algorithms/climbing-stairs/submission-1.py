class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} # knyabaga petti

        def dp(i):
            # Overstepped 
            if i > n:
                return 0
            # yayy we reached
            if i == n:
                return 1 
            
            if i in memo:
                return memo[i]
            
            takeOneStep = dp(i+1)
            takeTwoStep = dp(i+2)

            memo[i] = takeOneStep + takeTwoStep
            return memo[i]
        return dp(0)

