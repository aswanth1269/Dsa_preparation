class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minbuy = prices[0]

        for i in range(1,len(prices)):
            profit2 = prices[i] - minbuy
            if profit2 >profit:
                profit = profit2
            minbuy = min(minbuy,prices[i])
        return profit