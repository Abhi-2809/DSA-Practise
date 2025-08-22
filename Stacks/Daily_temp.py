class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        answers=[0]*len(temperatures)

        for idx,temp in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stacktemp, stackI = stack.pop()
                answers[stackI] =  idx - stackI
            
            stack.append((temp,idx))
        
        return answers





        