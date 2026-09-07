class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        f = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for i, cu in count.items():
            f[cu].append(i)

        res = []
        for i in range(len(f) - 1, 0, -1):
            for n in f[i]:
                res.append(n)
                if len(res) == k:
                    return res
