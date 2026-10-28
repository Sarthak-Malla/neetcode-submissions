class Solution:

    def encode(self, strs: List[str]) -> str:
        # length#word
        res = ""

        for s in strs:
            length = len(s)
            res += str(length) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0
        j = 0
        while i < n:
            j = i
            while i<n and s[i].isnumeric():
                i += 1
            
            if s[i] == "#":
                num = int(s[j:i])
                word = s[i + 1:i+1+num]

                i += num
                res.append(word)
            
            i += 1
        
        return res
