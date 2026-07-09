class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        topK = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]
        result = [num for num, count in topK]

        return result