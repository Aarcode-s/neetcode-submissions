class Solution:
    def simplifyPath(self, path: str) -> str:
        # starting mai "/" hoga 
        # fir agr "/" aata h to ni lenge 
        # agar text & number aata h to lenge 
        # agar "." aayega ni lenge 
        # agar ".." ayega to piche wala pop kar denge 

        # fir stack pop karke reverse kardenge

        stack = []

        parts = path.split("/")

        for part in parts:
            if part == "":
                continue
            elif part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)