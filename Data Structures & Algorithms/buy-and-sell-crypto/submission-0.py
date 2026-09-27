class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy single day at prices[i] and sell on another day prices[j]
        # Goal is maximum diff = prices[j] - prices[i]

        res = 0
        for i in range(len(prices)):
            buy = prices[i] # i for index positions
            for j in range(i, len(prices)):
                sell = prices[j]
                res = max(sell-buy , res)

        return res
        