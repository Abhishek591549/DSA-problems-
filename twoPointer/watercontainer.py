class Solution:
    def maxArea(self, height):
      
        maxarea=0
        i=0
        j=len(height)-1
        while i<j:
            currentA=min(height[i],height[j])*(j-i)
            maxarea=max(maxarea,currentA)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxarea            

        