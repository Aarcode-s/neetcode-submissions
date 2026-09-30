class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tkn in tokens:

            if tkn not in "+-*/":
                stack.append(int(tkn))

            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if tkn == "+":
                    stack.append(val2 + val1)

                elif tkn == "-":
                    stack.append(val2 - val1)

                elif tkn == "*":
                    stack.append(val2 * val1)

                else:
                    stack.append(int(val2 / val1))

        return stack.pop()