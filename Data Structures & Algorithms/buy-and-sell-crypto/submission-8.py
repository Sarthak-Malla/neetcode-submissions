class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        currMax = 0
        n = len(prices)

        for r in range(n):
            if prices[r] < prices[l]:
                l = r
            
            currMax = max(currMax, prices[r] - prices[l])
        
        return currMax