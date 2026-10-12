class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =  0
        current =  nums[0]
        for num in nums:
            if num == current:
                count += 1
            
            if num != current:
                if count > 0:
                    count -= 1
                if count <= 0:
                    current = num
                    count += 1
        
        return current