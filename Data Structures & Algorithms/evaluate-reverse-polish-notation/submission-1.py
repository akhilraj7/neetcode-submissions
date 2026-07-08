class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opers = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token not in opers:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:
                    result = int(a / b)

                stack.append(result)

        return stack[0]