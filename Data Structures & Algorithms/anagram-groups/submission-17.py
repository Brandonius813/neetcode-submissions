class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramIndexes = {}
        res = []

        for s in range(len(strs)):
            counts = [0] * 26
            
            for c in range(len(strs[s])):
                counts[ord(strs[s][c]) - ord('a')] += 1
            
            counts = tuple(counts)

            if counts in anagramIndexes:
                res[anagramIndexes[counts]].append(strs[s])
            
            else:
                anagramIndexes[counts] = len(res)
                res.append([strs[s]])
        
        return res