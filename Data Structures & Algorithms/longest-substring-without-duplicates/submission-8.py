class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = {}

        l = 0
        n = len(s)
        res = 0

        for r in range(n):
            if s[r] not in dp:
                dp[s[r]] = 1
                res = max(res, r - l + 1)
                continue
            
            # find s[r]
            while l < r and s[l] != s[r]:
                del dp[s[l]]
                l += 1
            l += 1
        
        return res