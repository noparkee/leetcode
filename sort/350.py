class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    nums2.remove(j)
                    r.append(i)
                    break
        
        return r
        