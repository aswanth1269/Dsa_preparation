class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            hea = stones.sort()
            n = len(stones)
            if stones[n-1] == stones[n-2]:
                stones.pop()
                stones.pop()
            elif stones[n-2] < stones[n-1]:
                stones[n-1] = stones[n-1] - stones[n-2]
                stones.pop(n-2)
        return stones[0] if stones else 0