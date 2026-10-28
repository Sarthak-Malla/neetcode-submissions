class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkPermutation(s1: str, s2:str) -> bool:
            bit = [0 for _ in range(26)]
            for i in range(len(s1)):
                bit[ord(s1[i]) - ord('a')] += 1
                bit[ord(s2[i]) - ord('a')] -= 1
            
            for i in range(26):
                if bit[i] != 0:
                    return False
            
            return True

        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        
        l = 0
        while l < m - n + 1:
            if checkPermutation(s1, s2[l:l+n]):
                return True
            
            l += 1
        
        return False
