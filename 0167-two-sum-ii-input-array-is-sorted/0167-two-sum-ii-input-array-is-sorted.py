class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary={}
        for index, value in enumerate(numbers):
            x=target-value
            if x in dictionary:
                return sorted([index+1,dictionary[x]+1])
            else:
                dictionary[value]=index
