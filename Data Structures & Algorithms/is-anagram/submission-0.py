class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sarr = [0 for i in range(26)]
        tarr = [0 for i in range(26)]
        
        for c in s:
            sarr[ord(c.lower()) - ord('a')] += 1
        
        for c in t:
            tarr[ord(c.lower()) - ord('a')] += 1
        
        for i in range(26):
            if tarr[i] != sarr[i]:
                return False
        
        return True