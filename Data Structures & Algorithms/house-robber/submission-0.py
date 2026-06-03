class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            robHouse = nums[i] + dp(i+2)
            skipHouse = dp(i+1)

            memo[i] = max(robHouse,skipHouse)

            return memo[i]
        
        return dp(0)