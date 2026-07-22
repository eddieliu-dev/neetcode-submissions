class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                res = int(token)
            if token == '+':
                res = stack.pop() + stack.pop()
            if token == '-':
                b, a = stack.pop(), stack.pop()
                res = a - b
            if token == '*':
                res = stack.pop() * stack.pop()
            if token == '/':
                b, a = stack.pop(), stack.pop()
                res = int(a / b)
            stack.append(int(res))
        return stack[-1]