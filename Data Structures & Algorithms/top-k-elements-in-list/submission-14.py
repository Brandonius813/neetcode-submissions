# OHHH CRAP IT'S NOT SORTED and SORTING WOULD HELP YOU MORON

# I checked the solution at a few mins in.

# This is a bucket sort problem - sort biggest elements to the right, return the k rightmost elements


# And to make this O(n), you gotta do a tricky bucket sort where the result is in an "inverse mapped array" - instead of the indexes being the value of the number, then the values being the quantity of it, now our indexes are the quantity, and we store a list of values with that quantity at that index.

# We still determine the counts with a hashmap

# Then we dump the hashmap into this tricky array.  We have O(3n) which is O(n) ultimately.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            counts[num] += 1
        
        for value, count in counts.items():
            freq[count].append(value)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        