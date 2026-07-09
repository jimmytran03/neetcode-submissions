class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        leftIndex = 0

        for n in range(len(nums)):
            rightIndex = total - leftIndex - nums[n]
            if leftIndex == rightIndex:
                return n
            else:
                leftIndex += nums[n]
        return -1
