class Solution:
    def isValid(self, s: str) -> bool:
        dict_close_open = { ')': '(', '}':'{' , ']':'['}
        stack =[]
        for c in s:
            if c in dict_close_open:
                if stack and stack[-1]==dict_close_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

        