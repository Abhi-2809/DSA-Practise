# Fruits in a basket : Leetcode 904
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l,res = 0,0
        count = {}
        for r,t in enumerate(fruits):
            count[t] = count.get(t,0)+1

            while len(count)>2:
                element = fruits[l]
                count[element]-=1
                if count[element]==0:
                    del count[element]
                l+=1        
            
            res = max(r-l+1,res)
        return res
