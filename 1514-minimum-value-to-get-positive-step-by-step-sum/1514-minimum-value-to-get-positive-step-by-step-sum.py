class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runningsum=0
        minsum=0
        for num in nums:
            runningsum+=num
            minsum=min(runningsum,minsum)
        return -minsum+1 if minsum<0 else 1
                

            

        