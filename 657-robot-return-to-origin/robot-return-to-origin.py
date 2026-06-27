class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=[0,0]
        for i in moves:
            if i=="R":
                x[1]+=1
            elif i=="L":
                x[1]-=1
            elif i=="U":
                x[0]+=1
            elif i=="D":
                x[0]-=1
        if x==[0,0]:
            return True 
        else :
            return False