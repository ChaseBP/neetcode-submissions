class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLength = 0
        for num in numSet:
            if num-1 not in numSet:
                currLength = 1
                currNum = num

                while currNum + 1 in numSet:
                    currLength += 1
                    currNum += 1
                maxLength = max(currLength,maxLength)
        
        return maxLength

