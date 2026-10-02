class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for ch in s:

            if ch != "]":
                stack.append(ch)
                continue

            # Get substring inside []
            substring = ""

            while stack and stack[-1] != "[":
                ch = stack.pop()
                substring = ch + substring

            # Remove "["
            stack.pop()

            # Get number before "["
            number = ""

            while stack and stack[-1].isdigit():
                number = stack.pop() + number

            # Multiply substring
            substring = int(number) * substring

            # Put decoded string back into stack
            for c in substring:
                stack.append(c)

        return "".join(stack)