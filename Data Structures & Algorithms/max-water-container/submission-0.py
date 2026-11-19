class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        area = 0

        while l < r:
            height = min(heights[l], heights[r])
            area = max(height * (r - l), area)

            if heights[l] <= heights[r]:
                l += 1
                continue
            
            if heights[r] < heights[l]:
                r -= 1
                continue
        
        return area