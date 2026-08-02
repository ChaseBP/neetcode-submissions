class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(num):
            if num < 0:
                return 0
            if num == 0:
                return 1
            
            if num in memo:
                return memo[num]
            
            memo[num] = dfs(num-1) + dfs(num-2)

            return memo[num]

        return dfs(n)
