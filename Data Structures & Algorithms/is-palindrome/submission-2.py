class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right, n = 0, len(s) - 1, len(s)
        s = s.lower()
        while left < right:
            while left < n and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
            
            if left >= right:
                return True

            if s[left] != s[right]:
                print(s[left], s[right])
                return False
            
            left += 1
            right -= 1
            
        return True