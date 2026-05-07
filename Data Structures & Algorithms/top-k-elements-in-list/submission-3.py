class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = set()
        dupes = []
        added = set()

        for num in nums:
            if num in seen and num not in added:
                dupes.append(num)
                added.add(num)
                if len(dupes) == k:
                    break
            seen.add(num)

        return list(dupes)