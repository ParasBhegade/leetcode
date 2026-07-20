class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count=0
        d=set()
        C=[]
        for i in range(len(A)):
            if A[i] in d:
                count+=1
            else:
                d.add(A[i])
            if B[i] in d:
                count+=1
            else:
                d.add(B[i])
            C.append(count)
        return C