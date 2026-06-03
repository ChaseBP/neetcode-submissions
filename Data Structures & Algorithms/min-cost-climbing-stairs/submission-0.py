class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def dp(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            

            takeOneStep = cost[i] + dp(i+1)
            takeTwoStep = cost[i] + dp(i+2)

            memo[i] = min(takeOneStep, takeTwoStep)
            return memo[i]
        
        return min(dp(0), dp(1))