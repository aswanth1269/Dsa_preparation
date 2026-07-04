class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = Counter(nums)
       top_k = count.most_common(k)
       return [num for num, freq in top_k]
