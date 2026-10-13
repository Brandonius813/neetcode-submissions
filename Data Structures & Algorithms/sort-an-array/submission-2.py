class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # MergeSort or QuickSort could do this, but QuickSort's worst case is worse than nlogn

        # Merge 2 Sorted Arrays
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0 

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                
                else:
                    arr[i] = right[k]
                    k += 1

                i += 1
            
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        # Perform merge sort, given the merge 2 sorted arrays function
        def mergeSort(arr, l, r):
            if l == r: # We have our bottom of the tree - 2 arrays of 1
                return arr
            
            m = (l+r) // 2
            mergeSort(arr, l, m) # MergeSort on the left
            mergeSort(arr, m + 1, r) # Merge sort the right
            merge(arr, l, m, r) # Merge 2 sorted arrays
            return arr
    
        return mergeSort(nums, 0, len(nums) - 1) # Actually call the function