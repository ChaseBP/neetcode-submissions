class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqDict = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in freqDict:
                freqDict[sortedString].append(string)
                continue
            freqDict[sortedString] = [string]
        print(freqDict)
        return list(freqDict.values())
        
                 

        