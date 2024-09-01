class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range( len(prices)):
            cost = prices[i] - buy
            profit = max(cost, profit)
            buy = min(buy, prices[i])

        return profit