class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        arr = []
        for n in count:
            cnt = count
            arr.append([cnt, n])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res