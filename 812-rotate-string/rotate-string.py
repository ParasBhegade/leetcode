class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        else:
            rot=s+s
            if goal in rot:
                return True
            else:
                return False