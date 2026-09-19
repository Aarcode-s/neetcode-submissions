class Solution:
    def isPalindrome(self, s: str) -> bool:

        x = ""
        y = ""

        # Reverse
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                x = x + s[i].lower()

        # Normal
        for i in range(len(s)):
            if s[i].isalnum():
                y = y + s[i].lower()

        return x == y