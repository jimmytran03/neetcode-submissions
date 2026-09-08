class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        sortedCount = []
        for n in count:
            cnt = count[n]
            sortedCount.append([n, cnt])
        sortedCount.sort()

        res = []
        while len(res) < k:
            res.append(sortedCount.pop()[0])
        return res