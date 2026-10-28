class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not st or (st and st[-1][1] > temp):
                st.append((i, temp))
                continue
            
            while st and st[-1][1] < temp:
                j, t = st.pop()
                res[j] = i - j
            st.append((i, temp))

        return res