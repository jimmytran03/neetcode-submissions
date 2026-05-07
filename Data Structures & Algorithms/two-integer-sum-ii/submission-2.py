class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            while L < R and L + R != target:
                L += 1

            while L < R and L + R != target:
                R -= 1

            L += 1
            R -= 1

            if L + R == target:
                return [L, R]
        
        return [L, R]