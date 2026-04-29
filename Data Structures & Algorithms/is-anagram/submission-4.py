class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        if len(s) != len(t):
            return False 
        
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        for char in hashS:
            if hashS[char] != hashT.get(char, 0):
                return False
        return True


        