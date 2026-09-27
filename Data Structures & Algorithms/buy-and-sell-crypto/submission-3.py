class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers
        l = 0 # buy day
        r = 1 # sell day
        maxP = 0 # max profit
        while r < len(prices): # 1,2,3 = len 3, r hits only 2 for index
            if prices[r] > prices[l]: # as long as sell day > buy (positive)
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP) # compare existing maxP counter and take bigger profit
            else: # prices[r] <= prices[l]
                # drop in price at r, so we should move buying day to r
                l = r
            r +=1 # crawl r forward to find more cheaper days/increased profits
        return maxP



        