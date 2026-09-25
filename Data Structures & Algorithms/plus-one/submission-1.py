class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        position = 10 ** (n-1)
        number = 0

        for i in range(n):
            number = number + (digits[i] * position)
            position //= 10
        
        output = []

        finalValue = str(number + 1)

        for i in finalValue:
            output.append(int(i))
        
        return output