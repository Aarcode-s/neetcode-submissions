class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        a = strs[0]
        res = ""

        if len(a) == 0:
            return res

        for i in range(len(a)):
            for s in strs[1:]:
                if i >= len(s) or a[i] != s[i]:
                    return res
            res += a[i]

        return res

