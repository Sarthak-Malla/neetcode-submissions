class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dp = {}
        l = 0
        n = len(s)
        maxf = 0
        res = 0
        for r in range(n):
            dp[s[r]] = 1 + dp.get(s[r], 0)
            maxf = max(maxf, dp[s[r]])
            while r - l + 1 - maxf > k:
                dp[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res