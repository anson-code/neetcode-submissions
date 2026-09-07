class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                hashMapS[s[i]] = 1 + hashMapS.get(s[i],0)
                hashMapT[t[i]] = 1 + hashMapT.get(t[i],0)
        
        return hashMapS == hashMapT

        