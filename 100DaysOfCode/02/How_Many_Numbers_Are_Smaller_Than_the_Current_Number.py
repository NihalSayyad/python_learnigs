class Solution:
    def smallerNumbersThanCurrent(self, nums ):
        temp = sorted(nums)
        indexDict = {}
        out = []
        for i in range(len(temp)):
            if temp[i] not in indexDict:
                indexDict[temp[i]] = i
        for i in range(len(nums)):
            out.append(indexDict[nums[i]])
        return out

sol = Solution()
nums =  [8,1,2,2,3]
out = []
out = sol.smallerNumbersThanCurrent(nums)

print(out)
