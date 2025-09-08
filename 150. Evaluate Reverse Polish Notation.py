class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            if x == "+":
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(a + b)
            elif x == '-':
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(b - a)
            elif x == '*':
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(a * b)
            elif x == '/':
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(x))
        return stack[0]


print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
