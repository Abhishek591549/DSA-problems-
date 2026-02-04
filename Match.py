class Solution:
    def diStringMatch(self, s: str):
        low=0
        high=len(s)
        li=[]
        for i in s:
            if i=="I":
                li.append(low)
                low+=1
            elif i=="D":
                li.append(high)
                high-=1
        li.append(low)        
        return li            