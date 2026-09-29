class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        s_count = {}
        t_count = {}

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        i = 0

        have = 0
        need = len(t_count)

        min_size = float("inf")
        res = ""

        for j in range(len(s)):
            s_count[s[j]] = s_count.get(s[j], 0) + 1

            if s[j] in t_count and s_count[s[j]] == t_count[s[j]]:
                have += 1

            while have == need:
                size = j - i + 1

                if size < min_size:
                    min_size = size
                    res = s[i : j + 1]

                s_count[s[i]] -= 1

                if s[i] in t_count and s_count[s[i]] < t_count[s[i]]:
                    have -= 1

                i += 1

        return res
