class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0
        for num in nums:
            count = 1
            temp = num
            while temp - 1 in hashSet:
                temp -= 1
                count +=1 
            maxCount = max(count, maxCount)
        
        return maxCount
            