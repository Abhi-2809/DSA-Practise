class MinStack:

    def __init__(self):
        self.stack= []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # At every point store the new minimum value that corresponds in min_stack
        # to the minimum when a new element is appended
        new_min = min(val,self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()