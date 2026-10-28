class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)
        if n < 2:
            return 0

        res = 0
        while r < n:
            res = max(res, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return res