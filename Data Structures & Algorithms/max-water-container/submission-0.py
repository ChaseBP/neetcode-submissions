class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left
            limitingHeight = (
                heights[left] if heights[left] < heights[right] else heights[right]
            )

            area = limitingHeight * width

            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea