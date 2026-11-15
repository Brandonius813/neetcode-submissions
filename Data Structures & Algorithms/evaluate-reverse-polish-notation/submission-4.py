class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(var1 + var2)

            elif i == "-":
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(var2 - var1)

            elif i == "*":
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(var1 * var2)

            elif i == "/":
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(int(var2 / var1))

            else:
                stack.append(int(i))
        
        out = int(stack.pop())
        return out