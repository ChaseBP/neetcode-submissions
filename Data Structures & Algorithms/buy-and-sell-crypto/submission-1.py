class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, left, right = 0, 0, 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
            right += 1
        return maxProfit


      