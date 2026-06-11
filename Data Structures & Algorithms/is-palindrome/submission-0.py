class Solution:
    def isPalindrome(self, s: str) -> bool:
        t =  "".join(c.lower() for c in s if c.isalnum())

        j = len(t) -1
        i=0
        while i<j:
            if t[i] != t[j]:
                return False
            i+=1
            j-=1
        return True
