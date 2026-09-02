class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sortedCount = []
        for num in count:
            cnt = count[num]
            sortedCount.append([cnt, num])
        sortedCount.sort()

        res = []
        while len(res) < len(sortedCount):
            res.append(sortedCount.pop()[1])
        return res