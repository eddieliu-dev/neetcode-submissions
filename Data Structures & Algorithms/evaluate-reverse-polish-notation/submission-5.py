class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        for i in range(len(tokens)):
            res = 0
            if tokens[i] in operators:
                if tokens[i] == "+":
                    res = stack.pop() + stack.pop()
                elif tokens[i] == "-":
                    b, a = stack.pop(), stack.pop()
                    res = a - b
                elif tokens[i] == "*":
                    res = stack.pop() * stack.pop()
                else:
                    b, a = stack.pop(), stack.pop()
                    res = int(a / b)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return int(stack[-1])
