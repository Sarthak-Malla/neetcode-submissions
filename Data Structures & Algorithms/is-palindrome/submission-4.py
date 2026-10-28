class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filer the string
        new_s = ""
        for let in s:
            if let.isalnum():
                new_s += let.lower()
        
        return new_s == "".join(list(new_s)[::-1])