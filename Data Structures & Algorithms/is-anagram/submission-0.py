class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sorted1 = sort(s)
        sorted2 = sort(t)

        if sorted1 == sorted2:
            return True
        return False