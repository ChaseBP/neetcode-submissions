class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}

        for i , num in enumerate(nums):
            rem = target - num
            if rem in hp:
                return [hp[rem],i]
            else:
                hp[num] = i 
            
