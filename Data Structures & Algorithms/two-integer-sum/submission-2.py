class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in hp:
                return [hp[complement], index]
            hp[num] = index
        


            
            