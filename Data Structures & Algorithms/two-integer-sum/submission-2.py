class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}

        for i, n in enumerate(nums):
            diff = target - i
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[n] = i