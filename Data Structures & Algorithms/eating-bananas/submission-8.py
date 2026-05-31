from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k: int) -> bool:
                total_hours = 0

                for pile in piles:
                    total_hours += math.ceil(pile/k)
                    
                    if total_hours > h:
                        return False

                return total_hours <= h

        left, right = 1, max(piles)

        while left <= right:
                mid = (left + right) // 2

                if canEat(mid):
                    right = mid -1
                else:
                    left = mid+1 
        return left
