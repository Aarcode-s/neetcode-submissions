class Solution:
    def validPalindrome(self, s: str) -> bool:
        # count,j,i = 0,len(s)-1,0

        # if len(s) == 3 and s[i] != s[j]:
        #     return False
        # else:

        #     while i < j:
        #         if s[i] != s[j]:
        #             count += 1
        #             i +=1
        #             j -=1
        #         else:
        #             i +=1
        #             j -= 1
        #     if count >1:
        #         return False
        # return True
       
            i,j = 0,len(s)-1
            while i < j:
                if s[i] != s[j]:
                    sL, sR = s[i+1:j+1], s[i:j]
                    return sL == sL[::-1] or sR == sR[::-1]
                i, j = i + 1, j - 1

            return True