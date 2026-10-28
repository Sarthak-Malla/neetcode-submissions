class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        db = {}
        n = len(s)
        l, r = 0, 1
        if n < 2:
            return n
        db[s[l]] = 1

        res = 1
        while r < n:
            if db.get(s[r]) != None:
                del db[s[r]]
                while s[l] != s[r] and l < r:
                    del db[s[l]]
                    l += 1
                while s[l] == s[r] and l < r:
                    l += 1
            db[s[r]] = 1
            res = max(res, r - l + 1)
            r += 1
        
        return res
