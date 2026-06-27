class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapS = {}
        mapT = {}

        for i in s:
            if i in mapS:
                mapS[i] += 1
            else:
                mapS[i] = 1
        
        for j in t:
            if j in mapT:
                mapT[j] += 1
            else:    
                mapT[j] = 1

        if mapS == mapT:
            return True
        
        return False