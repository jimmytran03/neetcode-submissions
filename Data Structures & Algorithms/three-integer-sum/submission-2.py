from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # Skip duplicate values for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early exit: smallest value is positive, no triplet can sum to 0
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res