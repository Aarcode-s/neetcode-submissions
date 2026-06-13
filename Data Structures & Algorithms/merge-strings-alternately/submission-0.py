class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans = []

        n = min(len(word1), len(word2))

        for i in range(n):
            ans.append(word1[i])
            ans.append(word2[i])

        for j in range(n, len(word1)):
            ans.append(word1[j])

        for k in range(n, len(word2)):
            ans.append(word2[k])

        return "".join(ans)