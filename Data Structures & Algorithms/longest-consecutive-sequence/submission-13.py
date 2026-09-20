class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numCount = set(nums)
        longest = 0

        for num in numCount:
            if (num - 1) not in numCount:
                length = 1
                while (num + length) in numCount:
                    length += 1
                longest = max(longest, length)
        return longest