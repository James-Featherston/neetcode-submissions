class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def doOperation(num1, num2, op):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num2 - num1
            elif op == '*':
                return num2 * num1
            elif op == "/":
                return int(num2/num1)

        def isOp(op):
            return  op == '+' or op == '-' or op == '*' or op == '/'
        stack = []

        for s in tokens:
            if not isOp(s):
                stack.append(int(s))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(doOperation(num1, num2, s))
        return stack.pop()
                

