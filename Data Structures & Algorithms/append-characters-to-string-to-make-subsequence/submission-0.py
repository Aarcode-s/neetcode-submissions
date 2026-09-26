class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        # s = "coaching", t = "coding"

        # i in s and j in t
        # if i == j then both increase 
        # if i != j
        # then increase i and try to find j 
        # in the end let j =2 that means 2 elements are matched and 4 are unmatched
        # ans = 4

        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j