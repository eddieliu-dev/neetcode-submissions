class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            if token == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            if token == '*':
                stack.append(stack.pop() * stack.pop())
            if token == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
        return stack[-1]