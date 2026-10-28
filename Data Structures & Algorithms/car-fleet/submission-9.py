class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        times = [target] * n

        for i, (p, s) in enumerate(zip(position, speed)):
            times[i] = (target - p) / s
        
        pt = sorted(zip(position, times))

        st = []
        for p, t in pt:
            if not st or (st and st[-1] > t):
                st.append(t)
                continue

            while st and st[-1] <= t:
                st.pop()
            st.append(t)

        return len(st) if st else 1
