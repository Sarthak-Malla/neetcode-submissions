class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        l, r = 1, maxK

        def check(k):
            s = 0
            for num in piles:
                s += math.ceil(num / k)
            
            return s <= h

        res = float("inf")
        while l <= r:
            k = l + (r-l) // 2

            if check(k):
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res