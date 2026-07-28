class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def helper(index, path, currSum):
                if currSum == target:
                    result.append(path.copy())
                    return
                
                for i in range(index, len(candidates)):
                    
                    if currSum + candidates[i] > target:
                        break
                    if i > index and candidates[i] == candidates[i-1]:
                        continue

                    path.append(candidates[i])
                    helper(i+1, path,currSum+candidates[i])
                    path.pop()
                
        helper(0,[],0)

        return result