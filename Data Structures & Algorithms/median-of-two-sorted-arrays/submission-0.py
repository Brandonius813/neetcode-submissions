class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
    
        l, r = 0, len(A) - 1
        while True:
            ma = (l + r) // 2 # A midpoint
            mb = half - ma - 2 # B's left partition right index, -2 because 2 different zero-indexed arrays, and we're doing this based on a total of number of elements.

            # These are the end of the left partition, beginning of right partition, in each array
            # The edge case checks basically say "hey if we go out of bounds, make sure we still evaluate correctly in the greater or less than's."
            Aleft = A[ma] if ma >= 0 else float("-infinity")
            Aright = A[ma + 1] if (ma + 1) < len(A) else float("infinity")
            Bleft = B[mb] if mb >= 0 else float("-infinity")
            Bright = B[mb + 1] if (mb + 1) < len(B) else float("infinity")
            
            # This means our partitions are good!  Compute an answer inside this if statement.
            if Aleft <= Bright and Bleft <= Aright:
                # Are we computing median from even or odd total?
                if total % 2:
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # Partitions invalid?  Move pointers, run again.
            elif Aleft > Bright:
                r = ma - 1
            
            else:
                l = ma + 1