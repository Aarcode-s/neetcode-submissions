class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_set = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            h_set[s[i]] = h_set.get(s[i], 0) + 1
            h_set[t[i]] = h_set.get(t[i], 0) - 1

        return all(v == 0 for v in h_set.values())