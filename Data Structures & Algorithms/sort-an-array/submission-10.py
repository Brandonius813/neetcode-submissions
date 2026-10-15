class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # This requires me to implement merge sort or quicksort, I'll do merge

        # Merge sort is split an array into 2, then keep splitting until I have an array size 1.  Then, merge the 2 arrays, lowest to highest.  Then, merge all arrays on the way up in ascended sorting order.

        # Mistake: 
    
        def Merge(left, right):
            l, r = 0, 0
            out = []

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    out.append(left[l])
                    l += 1
                
                else:
                    out.append(right[r])
                    r += 1
                
            while l < len(left):
                out.append(left[l])
                l += 1

            while r < len(right):
                out.append(right[r])
                r += 1
            
            return out

        def MergeSort(arr):

            if len(arr) <= 1:
                return arr

            l, r = 0, len(arr) - 1
            m = (len(arr) - 1) // 2

            left, right = arr[:m+1], arr[m+1:]

            left = MergeSort(left)
            right = MergeSort(right)

            return Merge(left, right)
        
        return MergeSort(nums)