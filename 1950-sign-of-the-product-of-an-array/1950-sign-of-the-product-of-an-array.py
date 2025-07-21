class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s=1
        for num in nums:
            s*=num
        if s==0:
            return 0
        if s>=1:
            return 1
        if s<0:
            return -1

        