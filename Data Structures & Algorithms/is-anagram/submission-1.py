class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sarr = [0 for i in range(26)]
        
        for c in s:
            sarr[ord(c.lower()) - ord('a')] += 1
        
        for c in t:
            sarr[ord(c.lower()) - ord('a')] -= 1
        
        for i in range(26):
            if sarr[i] > 0:
                return False
        
        return True