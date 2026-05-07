class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sorted1 = s.sort()
        sorted2 = t.sort()

        if sorted1 == sorted2:
            return True
        return False