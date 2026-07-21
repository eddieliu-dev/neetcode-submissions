class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            res = 0
            if token == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            if token == "-":
                b, a = stack.pop(), stack.pop()
                res = a - b
                stack.append(res)
            if token == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            if token == "/":
                b, a = stack.pop(), stack.pop()
                res = int(a / b)
                stack.append(res)
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
        return int(stack[-1])
