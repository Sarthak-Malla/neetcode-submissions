class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(piles, k):
            if k == 0:
                return h+1
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / k)
            return hour
        
        l, r = 0, max(piles)
        min_ = r
        while l <= r:
            m = (l + r) // 2

            if hours(piles, m) <= h:
                min_ = min(min_, m)
                r = m - 1
            else:
                l = m + 1
        
        return min_
            

