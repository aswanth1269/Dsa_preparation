class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        sumi = 0
        h = set()
        for i in s:
            if i not in h:
                h.add(i)
                count += 1
                sumi = count
            else:
                h = set()
                count = 0
                h.add(i)
                count += 1
        if sumi > count:
            return sumi
        else:
            return count


        