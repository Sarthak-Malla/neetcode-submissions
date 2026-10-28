class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        left = 0
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - 97] += 1
            s2Count[ord(s2[i]) - 97] += 1
        
        for right in range(len(s1), len(s2)):
            if s1Count == s2Count: return True
            s2Count[ord(s2[left]) - 97] -= 1
            s2Count[ord(s2[right]) - 97] += 1
            left += 1
        
        return s1Count == s2Count