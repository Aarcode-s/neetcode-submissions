class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for string in strs:
            x = len(string)
            encoded_string += str(x) + "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_string = []

        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1

            decoded_string.append(s[i:i + length])

            i = i + length

        return decoded_string