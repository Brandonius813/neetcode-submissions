class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in range(len(operations)):
            if operations[i].isdigit() or (
                operations[i][0] == "-" and operations[i][1:].isdigit()
            ):
                record.append(int(operations[i]))
            
            if operations[i] == "+":
                record.append(record[-1] + record[-2])
            
            if operations[i] == "D":
                record.append(record[-1] * 2)
            
            if operations[i] == "C":
                record.pop()
        
        return sum(record)
        