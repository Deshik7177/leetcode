class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:]
        z=[]
        for i in range(n):
            z.append(x[i])
            z.append(y[i])
        return z