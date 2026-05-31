from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k: int) -> bool:
            # Calculate total hours needed with eating rate k
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k  # ceiling division
                if total_hours > h:  # early exit optimization
                    return False
            return total_hours <= h
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if canEat(mid):
                # Can eat with rate mid, try to find smaller rate
                right = mid
            else:
                # Cannot eat with rate mid, need larger rate
                left = mid + 1
        
        return left