# Sort the array
# 2 pointers and a pointer at leftmost point, iterate thru all triplets
# To avoid duplicate outputs, if a pointer advances onto a duplicate number, skip it.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            if nums[i] == nums[i-1] and i > 0:
                continue

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    continue

                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    continue


                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    continue
        
        return res




        