class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""

        for i in range(len(strs[0])):
            compare = set()
            
            for s in range(len(strs)):
                if len(strs[s]) == i:
                    return out

                compare.add(strs[s][i])
            
            if len(compare) == 1:
                out += strs[0][i]
            else:
                return out
        
        return out