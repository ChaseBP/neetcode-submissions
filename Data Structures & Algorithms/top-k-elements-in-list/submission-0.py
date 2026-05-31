class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = {}
        for num in nums:
            if num in hp:
                hp[num]+=1
            else:
                hp[num]=1
        pairs = list(hp.items())
        pairs.sort(key=lambda x:x[1], reverse = True)

        result = []
        for i in range(k):
            result.append(pairs[i][0])

        return result