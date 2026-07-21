class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            res = 0
            if token == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                res = a - b
                stack.append(res)
            elif token == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                res = int(a / b)
                stack.append(res)
            else:
                stack.append(int(token))
        return int(stack[-1])
