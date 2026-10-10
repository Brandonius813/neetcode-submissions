class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1 # Bumps index (letter) in count by 1
            
            res[tuple(count)].append(s) # Append count array:string into the result dict.  Each count will have a list of its strings.

        return list(res.values()) # Return all the lists, in a row, of strings that match the count of letters in the alphabet