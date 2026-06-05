class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqDict = {}

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            
            key = tuple(count)

            if key not in freqDict:
                freqDict[key] = []
            freqDict[key].append(string)

        return list(freqDict.values())
        
                 

        