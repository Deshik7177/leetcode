class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        items = sorted(count.keys(),key=count.get,reverse=True)

        return items[:k]
        