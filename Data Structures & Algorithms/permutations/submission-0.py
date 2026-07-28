class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def helper(path):
            if len(path) == len(nums):
                res.append(path.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue
                #Choose
                used[i] = True
                path.append(nums[i])
                #Backtrack
                helper(path)
                #Remove
                used[i] = False
                path.pop()
        
        helper([])
        return res

