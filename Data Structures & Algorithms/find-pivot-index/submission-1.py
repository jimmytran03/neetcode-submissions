class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalNum = sum(nums)
        leftNum = 0

        for i in range(len(nums)):
            rightNum = totalNum - nums[i] - leftNum
            if rightNum == leftNum:
                return i
            else:
                leftNum += nums[i]
        return -1