class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alpha= "zyxwvutsrqponmlkjihgfedcba"
        wet=''
        for i in words:
            result=0
            for j in i:
                result+=weights[ord(j)-ord('a')]
                result=result%26
            wet+=alpha[result]
        return wet