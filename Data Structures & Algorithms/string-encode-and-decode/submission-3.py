class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        en = "randomshit".join(strs)
        if not len(en):
            en = "randomshit"
        return en

    def decode(self, s: str) -> List[str]:
        if not len(s):
            return []
        if s == "randomshit":
            return [""]
        return s.split("randomshit")
