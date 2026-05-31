class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hp = {}
        
        for i in nums:
            if i in hp:
                return True
            else:
                hp[i]=0
        return False