class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def helper(index, path,currSum):
            if currSum == target:
                res.append(path[:])
                return

            for i in range(index, len(nums)):
                if currSum + nums[i] > target:
                    break
        
                path.append(nums[i])
                helper(i,path,currSum+nums[i])
                path.pop()
             
        helper(0,[],0)
        return res