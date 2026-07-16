class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cut = 0
        for n in nums:
            if n == 0:
                res = max(res, cut)
                cut = 0
            else:
                cut += 1
        return max(cut, res)