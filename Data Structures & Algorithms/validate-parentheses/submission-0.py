class Solution:
    def isValid(self, s: str) -> bool:
        for i in s:
            if s[0] == '(' and s[-1] == '(':
                return True
            return False
