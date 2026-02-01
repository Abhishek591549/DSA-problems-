class Solution:
    def flipAndInvertImage(self, image):

        li=[]
        for i in image:
            i.reverse()
            temp=[]
            for j in i:
                if j==0:
                    temp.append(1)
                else:
                    temp.append(0)
            li.append(temp)       
          
        return li                 



        