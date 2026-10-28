class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = dict()
        n = len(s)
        
        res = 1
        l = 0
        for i in range(n):
            if s[i] in hash:
                l = max(l, hash[s[i]] + 1)

            res = max(res, i - l + 1)
            hash[s[i]] = i
        
        return res if s else 0