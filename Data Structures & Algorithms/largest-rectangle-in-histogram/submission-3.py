class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] # (i, h)
        res = 0
        
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                ii, hh = st.pop()
                res = max(res, (i - ii) * hh)
                start = ii
            st.append((start, h))
        
        n = len(heights)
        while st:
            ii, hh = st.pop()
            res = max(res, (n - ii) * hh)
        return res