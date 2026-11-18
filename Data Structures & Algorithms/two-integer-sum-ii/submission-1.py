
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = [0, 0]
        small = 0
        big = len(numbers) - 1
        
        while small < big:
            if numbers[small] + numbers[big] == target:
                out[0] = small + 1
                out[1] = big + 1
                break
            
            if numbers[small] + numbers[big] > target:
                big -= 1
            
            if numbers[small] + numbers[big] < target:
                small += 1
        
        return out