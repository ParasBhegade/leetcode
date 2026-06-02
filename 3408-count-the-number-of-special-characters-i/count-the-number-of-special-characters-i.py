class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        w=''
        for i in word:
            if i.islower():
                if i not in w:
                    if i.upper() in word:
                        w+=i.lower()
                        count+=1
            if i.isupper():
                if i.lower() not in w:
                    if i.lower() in word:
                        w+=i.lower()
                        count+=1
        return count