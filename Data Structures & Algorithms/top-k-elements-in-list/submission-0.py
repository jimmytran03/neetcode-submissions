class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = set()
        dupes = set()

        for num in nums:
            if num in seen:
                dupes.add(num)

            else:
                seen.add(num)

        return list(dupes)