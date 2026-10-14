class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            L, R, out = 0, 0, []

            while len(left) > L and len(right) > R:
                if left[L] <= right[R]:
                    out.append(left[L])
                    L += 1
                
                else:
                    out.append(right[R])
                    R +=1
            
            while len(left) > L:
                out.append(left[L])
                L += 1
                
            while len(right) > R:
                out.append(right[R])
                R +=1
            
            return out

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
        
            out = []
            l, r, m = 0, len(arr) - 1, (len(arr) - 1) // 2
            left, right = arr[0:m + 1], arr[m + 1:r + 1]

            if len(left) == len(right) == 1:
                return merge(left, right)
            
            left = mergeSort(left)
            right = mergeSort(right)

            out = merge(left, right)
            
            return out

        return mergeSort(nums)

