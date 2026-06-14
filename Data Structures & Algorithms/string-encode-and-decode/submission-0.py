class Solution:
    def __init__(self):
        self.length = []
        self.n = 0
    def encode(self, strs: List[str]) -> str:
        self.length = []
        self.n = len(strs)

        encoded_str = ""

        for s in strs:
            self.length.append(len(s))
            encoded_str += s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        output = []
        left = 0

        for i in range(self.n):
            right = left + self.length[i]
            output.append(s[left:right])
            left = right

        return output
        

