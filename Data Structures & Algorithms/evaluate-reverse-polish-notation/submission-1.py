class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(["*", "+", "-", "/"])
        def makeOperation(token, a, b):
            if token == "*":
                return a * b
            if token == "/":
                return a / b
            if token == "+":
                return a + b
            if token == "-":
                return a - b
        
        stack = []

        for token in tokens:
            if token in operations:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(makeOperation(token, a, b))
                continue
            stack.append(token)

        return int(stack.pop())