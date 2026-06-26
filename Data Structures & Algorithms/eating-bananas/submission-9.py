class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high  # Default to max speed

        while low <= high:
            mid = (low + high) // 2
            
            # Calculate hours needed for speed 'mid'
            currSum = sum(math.ceil(pile / mid) for pile in piles)
            
            if currSum <= h:
                ans = mid       # This speed works! Save it as a candidate...
                high = mid - 1  # ...but keep looking left for a smaller speed!
            else:
                low = mid + 1
        return ans