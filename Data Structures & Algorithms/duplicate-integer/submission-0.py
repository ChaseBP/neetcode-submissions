class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hp = {}
        for i in range(len(nums)):
            if nums[i] in hp:
                return True
            else: 
                hp[nums[i]] = 1
        return False
                