class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                # Next height limits the rectangle formed by the height at the top of the stack
                # So calculate the area with the height at the top of the stack as the smallest (or minimum height) bar 'h'
                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea