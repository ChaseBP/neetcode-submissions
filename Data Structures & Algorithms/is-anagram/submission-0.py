class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shp ={}
        thp ={}
        for letter in s:
            if letter in shp:
                shp[letter]+=1
            else:
                shp[letter]=1
        for letter in t:
            if letter in thp:
                thp[letter]+=1
            else:
                thp[letter]=1
        return True if (shp==thp) else False
        