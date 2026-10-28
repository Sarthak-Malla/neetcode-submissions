class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        df = [0] * 26
        for i in range(len(s)):
            df[ord(s[i]) - ord('a')] += 1
            df[ord(t[i]) - ord('a')] -= 1
        
        return [0]*26 == df