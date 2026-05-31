class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            freq = [0] * 26
            for ch in string:
                freq[ord(ch)-ord('a')] +=1
            key = tuple(freq)

            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        
        return list(groups.values())

