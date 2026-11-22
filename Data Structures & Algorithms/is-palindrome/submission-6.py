class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        The string s can have alpha numeric characters including non-alphanumeric characters.
        ignore any non-alphanumeric characters
        case-insensitive

        - make everything lowercase
        - check if a current character is alphanumeric
        """
        l, r = 0, len(s) - 1

        while l < r:
            # make sure we are not looking at non-alphanum
            while l < len(s) and not s[l].isalnum():
                l += 1
            
            while r >= 0 and not s[r].isalnum():
                r -= 1
            
            # check if they are the same in lowercase
            if l < len(s) and r >= 0 and not s[l].lower() == s[r].lower(): return False

            l += 1
            r -= 1
        
        return True
