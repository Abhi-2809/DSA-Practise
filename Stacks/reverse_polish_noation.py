from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operations = ['+','-',"/","*"]
        for i in tokens:
            if i in operations:
                b = int(stack.pop())
                a = int(stack.pop())
                if i=="+":
                    res=a+b
                elif i=="-":
                    res = a-b
                elif i=="*":
                    res = a*b
                else:
                    res=a/b
                    
                stack.append(int(res))
            
            else:
                stack.append(i)
        
        return int(stack[-1])

        