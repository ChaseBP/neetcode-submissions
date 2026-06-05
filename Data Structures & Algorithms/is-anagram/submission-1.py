class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def returnHashmap(string : str):
            hp = {}
            for i in string:
                if i in hp:
                    hp[i] += 1
                else:
                    hp[i] = 0
            
            return hp

        shp = returnHashmap(s)
        thp = returnHashmap(t)
        
        return shp == thp
            