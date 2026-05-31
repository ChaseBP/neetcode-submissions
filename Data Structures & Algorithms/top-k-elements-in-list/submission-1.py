class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = {}

        for num in nums:
            hp[num] = hp.get(num,0)+1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in hp.items():
            buckets[freq].append(num)

        result = []

        for i in range(len(nums), -1 , -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
    