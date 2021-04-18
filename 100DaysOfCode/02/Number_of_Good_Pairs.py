class Solution:
    def numIdenticalPairs(self, nums) :
        hashdict = {}
        num = 0
        
        for v in nums:
            if v in hashdict :
                if hashdict[v] == 1:
                    num += 1
                else:
                    num += hashdict[v]

                hashdict[v] += 1
            else:
                hashdict[v] = 1

        return num

nums =  [1,2,3,1,1,3]
sol = Solution()
out = sol.numIdenticalPairs(nums)
print(out)