class Solution:
    def minOperations(self,boxes:str)->List[int]:
        n=len(boxes)
        res=[0]*n
        balls=moves=0
        for i in range(n):
            res[i]+=moves
            if boxes[i]=='1':balls+=1
            moves+=balls
        balls=moves=0
        for i in range(n-1,-1,-1):
            res[i]+=moves
            if boxes[i]=='1':balls+=1
            moves+=balls
        return res