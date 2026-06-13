class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alpha= "zyxwvutsrqponmlkjihgfedcba"
        wet=''
        result=0
        for i in words:
            for j in i:
                result+=weights[ord(j)-ord('a')]
                result=result%26
            wet+=alpha[result]
            result=0
        return wet