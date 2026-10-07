class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        nextgreatest = greatest

        for i in range(len(arr)-2, -2, -1):
            if arr[i] > greatest:
                nextgreatest = arr[i]
            
            arr[i] = greatest
            greatest = nextgreatest
        
        arr[-1] = -1

        return arr