class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n-2):
            # Duplicate check 
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left, right = i+1, n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])

                    left +=1 
                    right -=1
                
                    while left < right and nums[left-1] == nums[left]:
                        left+=1
                    
                    while left < right and nums[right+1] == nums[right]:
                        right-=1 
                    
                elif total < 0:
                    left +=1 
                else:
                    right-=1                        
        return result 
