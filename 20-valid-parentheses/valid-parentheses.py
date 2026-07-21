class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)==1:
            return False
        for i in s:
            if i=="(":
                stack.append(i)
            elif i==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            elif i=="{":
                stack.append(i)
            elif i=="}":
                if stack and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            elif i=="[":
                stack.append(i)
            elif i=="]":
                if stack and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
        return len(stack)==0
            
            