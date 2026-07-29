class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_dict={}
        for i in magazine:
            hash_dict[i]=hash_dict.get(i,0)+1
        for i in ransomNote:
            if hash_dict.get(i,0)==0:
                return False
            else:
                hash_dict[i]-=1
        return True