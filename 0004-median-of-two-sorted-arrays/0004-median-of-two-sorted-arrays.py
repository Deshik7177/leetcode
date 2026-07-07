class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = nums1 + nums2
        num3.sort()
        n=len(num3)
        if n%2!=0:
            s=n//2
            return num3[s]
        else:
            f=n//2
            w=f-1
            q=num3[f]+num3[w]
            return q/2