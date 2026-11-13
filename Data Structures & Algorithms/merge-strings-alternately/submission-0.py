class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        point1 = 0
        point2 = 0
        out = ""

        while len(word1) > point1 and len(word2) > point2:
            out += f"{word1[point1]}"
            point1 += 1

            out += f"{word2[point2]}"
            point2 += 1
        
        while len(word1) > point1:
            out += f"{word1[point1]}"
            point1 += 1

        while len(word2) > point2:
            out += f"{word2[point2]}"
            point2 += 1
        
        return out
