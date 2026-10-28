class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            Aleft = A[m1] if m1 >= 0 else float("-inf")
            Aright = A[m1 + 1] if m1 + 1 < len(A) else float("inf")
            Bleft = B[m2] if m2 >= 0 else float("-inf")
            Bright = B[m2 + 1] if m2 + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Bright:
                if total % 2:
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = m1 - 1
            else:
                l = m1 + 1
        