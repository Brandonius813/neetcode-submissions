class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        vals = [[] for i in range(len(nums) + 1)]

        for value, count in counts.items():
            vals[count].append(value)
        
        res = []

        for i in range(len(vals) - 1, -1, -1):
            for c in vals[i]:
                res.append(c)
                if len(res) == k:
                    return res