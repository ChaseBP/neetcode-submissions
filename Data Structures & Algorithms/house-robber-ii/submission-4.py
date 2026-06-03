class Solution:
    def rob(self, nums: List[int]) -> int:
        

        if len(nums) == 1:
            return nums[0]
        def robSlice(houseSlice):
            memo = {}
            def dp(i):
                
                if i >= len(houseSlice):
                    return 0
                
                if i in memo:
                    return memo[i]
                
                robHouse = houseSlice[i] + dp(i+2)
                skipHouse = dp(i+1)

                memo[i] = max(robHouse,skipHouse)

                return memo[i]
            return dp(0)
        
        includeFirst= robSlice(nums[:len(nums)-1])
        includeLast = robSlice(nums[1:]) 

        return max(includeFirst, includeLast)