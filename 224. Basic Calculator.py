# class Solution:
#     def calculate(self, s: str) -> int:
#         stack=[]
#         i=0
#         while i<len(s):
#             x=s[i]
#             if x == '+':
#                 if s[i+1]!='(':
#                     a=stack[-1]
#                     stack.pop()
#                     while i+1<len(s) and s[i+1]==" ":
#                         i+=1
#                     nums=[]
#                     while i+1<len(s) and s[i+1]!='+' and s[i+1]!='-':
#                         nums.append(s[i+1])
#                         i+=1
#                     stack.append(a+int(nums))
#                     i+=1
#                 else:
#                     stack.append(x)
#             elif x == '-':
#                 if s[i+1]!='(':
#                     a=stack[-1]
#                     stack.pop()
#                     while i+1<len(s) and s[i+1]==" ":
#                         i+=1
#                     stack.append(a-int(s[i+1]))
#                     i+=1
#                 else:
#                     stack.append(x)
#             elif x == '(':
#                 stack.append(x)
#             elif x == ')':
#                 b = stack.pop()
#                 while stack[-1]!='(':
#                     ops=stack.pop()
#                     a=stack.pop()
#                     if ops=='+':
#                         stack.append(a+b)
#                     elif ops=='-':
#                         stack.append(a-b)
#                     b = stack.pop()
#                 stack.pop()
#                 stack.append(b)
#             elif x == ' ':
#                 i+=1
#                 continue
#             else:
#                 stack.append(int(x))
#             i+=1
#
#         if len(stack)>1:
#             stack=[str(x) for x in stack]
#             return self.calculate(''.join(stack))
#         return stack[0]
#
# print(Solution().calculate("9+14"))


class Solution:
    def calculate(self, s: str) -> int:
        res = 0        # 当前括号层的结果
        sign = 1       # 当前符号（+1 / -1）
        num = 0        # 当前正在读的数
        stack = []     # 交替压入 [之前的res, 之前的sign]

        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + ord(ch) - 48   # 读多位数
            elif ch == '+' or ch == '-':
                res += sign * num               # 结算前一个数
                sign = 1 if ch == '+' else -1  # 更新当前符号
                num = 0
            elif ch == '(':
                # 进入括号：把当前状态压栈，并重置
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                num = 0
            elif ch == ')':
                # 先把括号内最后一个数结算到 res
                res += sign * num
                num = 0
                # 弹出进入括号前的 sign 和 res
                prev_sign = stack.pop()
                prev_res = stack.pop()
                # 用之前的状态合并
                res = prev_res + prev_sign * res
            # 空格直接跳过
            i += 1

        return res + sign * num  # 收尾：把最后一个数结算进去
