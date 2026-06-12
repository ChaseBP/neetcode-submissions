class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prevDayIndex = stack.pop()
                res[prevDayIndex] = index - prevDayIndex
            
            stack.append(index)
        return res
