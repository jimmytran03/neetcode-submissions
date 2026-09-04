class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            anagram[sortedS].append(s)
        return anagram