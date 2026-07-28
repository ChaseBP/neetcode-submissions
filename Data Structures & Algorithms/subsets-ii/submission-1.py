class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(index, path):
            res.append(path.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                helper(i+1,path)
                path.pop()
        helper(0,[])
        return res

        