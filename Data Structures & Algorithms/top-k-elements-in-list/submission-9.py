class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sortCount = []
        for num in count:
            cnt = count[num]
            sortCount.append([cnt, num])
        sortCount.sort()

        res = []
        while len(res) < k:
            res.append(sortCount.pop()[1])
        return res