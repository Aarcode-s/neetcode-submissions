class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []

        for op in operations:
            if op == "+":
                value = record[-1] + record[-2]
                record.append(value)
            elif op == "D":
                value = record[-1]
                record.append(2*value)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))

        return sum(record)
