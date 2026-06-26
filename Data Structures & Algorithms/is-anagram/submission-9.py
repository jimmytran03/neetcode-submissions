class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = {}
        stringT = {}

        for char in s:
            if char in stringS:
                stringS[char] += 1
            else:
                stringS[char] = 1

        for char1 in t:
            if char1 in stringT:
                stringT[char1] += 1
            else:
                stringT[char1] = 1

        if stringS == stringT:
            return True
        return False